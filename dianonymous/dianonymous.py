#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import dicom
import os
import sys

import anonymizer

PATIENT_ID = (0x0010, 0x0020)

def anonymize(inputs, output="anonymized", recurse=False, private=True, curves=True):
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

    """

    output_dir = get_output_dir(output)

    for inp in get_input_paths(inputs, recurse):
        try:
            dcm = dicom.read_file(inp, force=True)
            dcm[PATIENT_ID] # serves as check for valid DICOM file
            anonymizer.anonymize(dcm, get_anonymized_path(inp))
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

        if os.path.isdir(path):
            all_paths = os.walk(path) if recurse else []
        else:
            root, fname = os.path.split(path)
            all_paths = [(root, "", [fname])]

        for root, _, files in all_paths:
            for f in files:
                yield os.path.join(root,f)

#---------------------------------------------------------------
def get_anonymized_path(inp_path, ):
    """return an anonymized path """


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Anonymize DICOM files")

    parser.add_argument(
        '-r', '--recurse',
        default=False,
        help="If input is a directory all DICOM files including"
            "subdirectories will be anonymized"
    )

    parser.add_argument(
        '-o', '--output',
        default="./anonymized/",
        help="Directory to place output files. If it doesn't exist it will be created."
    )
    parser.add_argument( '<files>', nargs="+", help="Input files and directories")

    args = parser.parse_args()
    print args
