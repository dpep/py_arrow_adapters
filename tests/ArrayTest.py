#!/usr/bin/env python

import os
import sys
import unittest

sys.path = [ os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')) ] + sys.path



class ArrowTypeTest(unittest.TestCase):
    def test_basic(self):
        pass



if __name__ == '__main__':
    unittest.main()
