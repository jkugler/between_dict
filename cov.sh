#!/bin/sh

python-coverage run "--omit=/usr/share/*,/usr/local/*,*run_tests*" ./run_tests.py
python-coverage report -m
