#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='dianonymous',
    version='0.1.0',
    description='A Python package for anonymizing DICOM files.  ***DISCLAIMER*** the anonymization provided this package is not guaranteed to be complete! In particular no effort is made to remove *burned-in* information from image files.  Use at your own risk and you alone are responsible for ensuring your patient data is properly anonymized.',
    long_description=readme + '\n\n' + history,
    author='Randle Taylor',
    author_email='randle.taylor@gmail.com',
    url='https://github.com/randlet/dianonymous',
    packages=[
        'dianonymous',
    ],
    package_dir={'dianonymous': 'dianonymous'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='dianonymous',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)