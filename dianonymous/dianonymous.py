#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import dicom
import hashlib
import os
import sys

from . import anonymizer

PATIENT_ID = (0x0010, 0x0020)

def anonymize(inputs, output="anonymized", anon_id=None, anon_name=None, recurse=False, private=True, curves=True, log=None):
    """
    Anonymize DICOM files and write new DICOM files to the output directory.
    The original files will be untouched.

    inputs: An iterable of file and directory names.  If one of the inputs
    is a directory, all DICOM files in that directory will be anonymized.

    output: Directory to place output files. If it doesn't exist, it will be
    created.

    recurse: Recurse over all subdirectoies. Default is False.

    private: Anonymize all private tags. Default is True.

    curves: Remove all curves. Default is True.

    log: object with a .write method or None. Default is None

    """

    output_dir = get_output_dir(output)
    completed = []

    for inp in get_input_paths(inputs, recurse):
        try:
            dcm = dicom.read_file(inp, force=True)
            patient_id = dcm[PATIENT_ID].value or "not provided" # also serves as check for valid DICOM file
            patient_name = dcm.PatientsName or "not provided"
            anon_id = anon_id or hashlib.sha512(patient_id).hexdigest()[:10]
            anon_name = anon_name or hashlib.sha512(patient_name).hexdigest()[:10]

            anonymizer.anonymize(dcm, patient_id=anon_id, patient_name=anon_name)

            rel_path = inp.replace(patient_id, anon_id).replace(patient_name, anon_name)
            rel_path = rel_path.replace(".." + os.path.sep, "").replace("." + os.path.sep, "")
            out_path = os.path.join(output_dir, rel_path)
            out_dir = os.path.split(out_path)[0]
            try:
                os.makedirs(out_dir)
            except OSError:
                pass
            dcm.save_as(out_path)
            if log:
                log.write("Anonymized & wrote %s to %s\n" % (inp, out_path))
        except (MemoryError, KeyError):
            pass


#---------------------------------------------------------------
def get_output_dir(output):
    """
    return full path of directory where outputs are to be stored.

    If the directory doesn't exist an attempt will be made to create it.
    """

    path = os.path.abspath(output)

    try:
        os.mkdir(path)
    except OSError:
        #Directory exists already
        pass

    return path


#---------------------------------------------------------------
def get_input_paths(inputs, recurse):
    """
    a generator for all input files requested
    """

    if isinstance(inputs, basestring):
        inputs = [inputs]

    for inp in inputs:
        path = os.path.relpath(inp)

        if os.path.isdir(path) and recurse:
            all_paths = os.walk(path) if recurse else []
        elif os.path.isdir(path):
            all_paths = [(path,"", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))])]

        else:
            root, fname = os.path.split(path)
            all_paths = [(root, "", [fname])]

        for root, _, files in all_paths:
            for f in files:
                yield os.path.join(root,f)


if __name__ == "__main__": #pragma nocover

    parser = argparse.ArgumentParser(description="Anonymize DICOM files")

    parser.add_argument(
        '-r', '--recurse',
        default=False,
        action="store_true",
        help="If input is a directory all DICOM files including"
            "subdirectories will be anonymized"
    )

    parser.add_argument(
        '-o', '--output',
        default="./anonymized/",
        help="Directory to place output files. If it doesn't exist it will be created."
    )

    parser.add_argument(
        '-p', '--patient-id',
        default=None,
        help="Anonymous patient id to use"
    )

    parser.add_argument(
        '-n', '--patient-name',
        default=None,
        help="Anonymous patient name to use"
    )

    parser.add_argument( 'files', nargs="+", help="Input files and directories")

    args = parser.parse_args()

    anonymize(args.files, output=args.output, anon_id=args.patient_id, anon_name=args.patient_name, recurse=args.recurse, log=sys.stdout)
