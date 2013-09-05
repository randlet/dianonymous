===============================
Dianonymous
===============================

A Python package for anonymizing DICOM files.  ***DISCLAIMER*** the
anonymization provided this package is not guaranteed to be complete! In
particular no effort is made to remove *burned-in* information from image
files.  Use at your own risk and you alone are responsible for ensuring your
patient data is properly anonymized.

This is currently alpha level quality at best and may (probably?) not
fully anonymize your DICOM files.

* Free software: BSD license

Features
--------

* TODO

Install
-------

This will install dianonymous in your Python packages directory
as well as a script called dianon in your Python scripts directory.  ::

    git clone git@github.com:randlet/dianonymous.git
    cd dianonymous
    python setup.py install

Run Tests
---------

Running the dianonymous tests ::

    git clone git@github.com:randlet/dianonymous.git
    cd dianonymous
    python setup.py nosetests

Usage
-----

From The Command Line
=====================

Anonymize a DICOM file and write to ./anonymize/ ::

    dianon path/to/file.dcm

Recursively anonymize all DICOM files in path/to/folder and write them to ./anonymize/ ::

    dianon -r path/to/folder

Recursively anonymize all DICOM files in path/to/folder and write them to different/output/path/ ::

    dianon -r -o different/output/path path/to/folder

Anonymize a DICOM file and write to ./anonymize/::

    dianon -r -o different/output/path path/to/folder


From Python
===========

From a Python script or interpreter ::

    import dianonymous
    paths_to_files_and_dirs = ["dir1/","dir2/","file1.dcm", "dir3/file2.dcm",...]
    output_dir = "./anonymized"

    dianonymous.anonymize(
        paths_to_files_and_dirs,
        output_dir,
        anon_id = None,    # optional string to use for output patient id
        anon_name = None,  # optional string to use for output patient name
        recurse = False,   # recurse any input subdirectories looking for dicom files
        private = True,    # delete any private tags
        curves = True,     # delete all curves
        log    = None,     # optional object with a .write method
    )



Acknowledgements
----------------

Ideas for the anonymizer were taken from both the pydicom and dicompyler packages
