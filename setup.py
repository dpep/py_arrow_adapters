#!/usr/bin/env python
"""
    Time Adapters - time should play nicely with others

    Copyright (c) 2020 Daniel Pepper

    The MIT License (MIT)

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.
"""

__author__ = 'dpepper'
__version__ = '0.0.1'

import setuptools
import unittest


def discover_tests():
    return unittest.TestLoader().discover(
        'tests',
        pattern='*Test.py',
    )


if __name__ == '__main__':

    setuptools.setup(
        name='time_adapters',
        version=__version__,
        url='https://github.com/dpep/py_time_adapters',
        license='MIT',
        author='Daniel Pepper',
        description='time adapters',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        platforms='any',

        packages=[
            'time_adapters',
        ],

        install_requires=[
            'arrow',
        ],

        test_suite='setup.discover_tests',
        tests_require=[
            'graphene',
            'sqlalchemy',
            'sqlite3',
        ],

        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Topic :: Utilities',
        ],
    )
