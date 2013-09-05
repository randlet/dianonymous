#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import dicom
import sys

if __name__ == "__main__": #pragma nocover

    from dianonymous.dianonymous import anonymize
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
