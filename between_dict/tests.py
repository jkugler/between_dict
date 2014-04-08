#!/usr/bin/env python

import os
import unittest2 as unittest

from between_dict import BetweenDict

class TestBetweenDict(unittest.TestCase):
    """Tests Class Functionality"""

    def test_relation_lower_exclusive(self):
        """Test ("""
        (name, op) = BetweenDict.char_to_relational('(')
        self.assertTrue(op(1,2))
        self.assertFalse(op(1,1))
        self.assertTrue(op(1,1.000001))
        self.assertFalse(op(2,1))

    def test_relation_upper_exclusive(self):
        """Test )"""
        (name, op) = BetweenDict.char_to_relational(')')
        self.assertTrue(op(1,2))
        self.assertTrue(op(1,1.000001))
        self.assertFalse(op(1,1))
        self.assertFalse(op(2,1))

    def test_relation_lower_inclusive(self):
        """Test ["""
        (name, op) = BetweenDict.char_to_relational('[')
        self.assertTrue(op(1,2))
        self.assertTrue(op(1,1))
        self.assertTrue(op(1,1.000001))
        self.assertFalse(op(2,1))

    def test_relation_upper_inclusive(self):
        """Test ]"""
        (name, op) = BetweenDict.char_to_relational(']')
        self.assertTrue(op(1,2))
        self.assertTrue(op(1,1.000001))
        self.assertTrue(op(1,1))
        self.assertFalse(op(2,1))

    def test_invalid_relation(self):
        self.assertRaises(ValueError, BetweenDict.char_to_relational, '.')

    def test_short_interval(self):
        """Throw an error if not given a two-element interval"""
        self.assertRaises(ValueError, BetweenDict, {}, '.')

    def test_non_iterable(self):
        """Throw an error if not given a non iterable for interval"""
        self.assertRaises(TypeError, BetweenDict, {}, BetweenDict)

    def test_invalid_first_operator(self):
        """Throw an error if not given an invalid first operator"""
        self.assertRaises(ValueError, BetweenDict, {}, '.]')

    def test_invalid_second_operator(self):
        """Throw an error if not given an invalid second operator"""
        self.assertRaises(ValueError, BetweenDict, {}, '[.')

    def test_valid_operators(self):
        """Make sure we get an valid object, given valid inputs"""
        d = BetweenDict(d={(1,3):'var'}, interval='[)')
        self.assertTrue(isinstance(d, BetweenDict))

    def test_get_item(self):
        """Does __getitem__ work"""
        d = BetweenDict(d={(1,3):'var'}, interval='[)')
        self.assertEqual('var', d[2])

    def test_key_error(self):
        """Does __getitem__ throw correct KeyErrors"""
        d = BetweenDict(d={(1,3):'var'}, interval='[)')
        self.assertRaises(KeyError, d.__getitem__, '4')

    def test_bad_setitem(self):
        """Given backwards values, what does __setitem__ do"""
        d = BetweenDict(d={(1,3):'var'}, interval='[)')
        self.assertRaises(RuntimeError, d.__setitem__, (6,1), 1)

    def test_setitem_bad_key_one(self):
        """What happens when __setitem__ gets a bad key"""
        d = BetweenDict(d={(1,3):'var'}, interval='[)')
        self.assertRaises(RuntimeError, d.__setitem__, (6,1), 1)

    def test_setitem_bad_key_two(self):
        """What happens when __setitem__ gets a bad key, part two"""
        d = BetweenDict(d={(1,3):'var'}, interval='[)')
        self.assertRaises(TypeError, d.__setitem__, BetweenDict, 1)

    def test_short_setitem_key(self):
        """Given an invalid key, does __setitem__ raise an error"""
        d = BetweenDict(d={(1,3):'var'}, interval='[)')
        self.assertRaises(ValueError, d.__setitem__, '.', 1)

    def test_closed_open(self):
        d = BetweenDict(d={(1,3):'var'}, interval='[)')
        self.assertFalse(0 in d)
        self.assertTrue(1 in d)
        self.assertTrue(2 in d)
        self.assertFalse(3 in d)
        self.assertFalse(6 in d)

    def test_open_open(self):
        d = BetweenDict(d={(1,3):'var'}, interval='()')
        self.assertFalse(0 in d)
        self.assertFalse(1 in d)
        self.assertTrue(2 in d)
        self.assertFalse(3 in d)
        self.assertFalse(6 in d)

    def test_closed_closed(self):
        d = BetweenDict(d={(1,3):'var'}, interval='[]')
        self.assertFalse(0 in d)
        self.assertTrue(1 in d)
        self.assertTrue(2 in d)
        self.assertTrue(3 in d)
        self.assertFalse(6 in d)

    def test_open_closed(self):
        d = BetweenDict(d={(1,3):'var'}, interval='(]')
        self.assertFalse(0 in d)
        self.assertFalse(1 in d)
        self.assertTrue(2 in d)
        self.assertTrue(3 in d)
        self.assertFalse(6 in d)
