#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name = "between_dict",
    version = "0.1",
    packages = find_packages(),
    exclude_package_data = {'':['README.md', 'LICENSE']},

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    tests_require = ['unittest2'],

    # metadata for upload to PyPI
    author = "Joshua Kugler",
    author_email = "joshua@azariah.com",
    description = "a dictionary except the key is in a range between two values",
    license = "BSD",
    keywords = "dict range",
    url = "http://azariah.com/",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
