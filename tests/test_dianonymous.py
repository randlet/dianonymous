#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dianonymous
----------------------------------

Tests for `dianonymous` module.
"""
import os
import shutil
import unittest

from dianonymous import dianonymous


class TestDianonymous(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.join(os.path.dirname(__file__),"testfiles")
        self.anonymous_dir = os.path.join(os.path.dirname(__file__),"anonymized")
        if os.path.exists(self.anonymous_dir):
            shutil.rmtree(self.anonymous_dir)
        os.mkdir(self.anonymous_dir)

    def test_output_dir_exists(self):
        output = dianonymous.get_output_dir(self.anonymous_dir)
        self.assertEqual(output, self.anonymous_dir)

    def test_output_dir_doesnt_exist(self):
        out_dir = os.path.join(self.anonymous_dir,"doesntexist")
        output = dianonymous.get_output_dir(out_dir)
        self.assertEqual(output, out_dir)

    def test_input_paths_no_recurse(self):
        input_paths = os.listdir(self.test_dir)
        expected = set([i for i in input_paths if not os.path.isdir(i)])
        self.assertSetEqual(expected, set(dianonymous.get_input_paths(input_paths, False)))

    def test_input_paths_recurse(self):
        input_paths = []
        for root, _, files in  os.walk(self.test_dir):
            root = os.path.relpath(root)
            input_paths.extend(os.path.join(root,f) for f in files)

        expected = set(input_paths)
        self.assertSetEqual(expected, set(list(dianonymous.get_input_paths(self.test_dir, True))))

    def test_anonymize(self):
        dianonymous.anonymize(self.test_dir, recurse=True)

    def tearDown(self):
        shutil.rmtree(self.anonymous_dir)

if __name__ == '__main__':
    unittest.main()
