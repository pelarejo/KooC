#!/usr/bin/env python3

import unittest
from KoocGrammar import KoocG

class Unittest_Classe(unittest.TestCase):
    """
        Doc: https://docs.python.org/3/library/unittest.html
    """

    def setUp(self):
    	self.kooc_g = KoocG()

    def test_ClasseEmpty(self):
    	self.assertEqual((self.kooc_g.parse("""
    		struct Kyouma
    		{}
    		""")).to_c(), (self.kooc_g.parse("""
    		struct Kyouma
    		{}
    		""")).to_c())

if __name__ == "__main__":
    unittest.main()