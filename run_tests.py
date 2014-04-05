#!/usr/bin/env python

import os
import sys
import unittest2 as unittest

# Set up the test environment
opd = os.path.dirname
sys.path.insert(0, opd(os.path.abspath(__file__)))

import between_dict_tests

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(between_dict_tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
