#!/usr/bin/env python3
# 01_functional_test.py
#2014-08-03

__author__ = 'Walter Kummer'

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

if __name__ == "__main__":
    pass