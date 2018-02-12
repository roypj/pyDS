#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request


def CustSort(s):
  pat = r'/puzzle/\w+-\w+-(\w+)'
  key = re.search(pat,s)
  return key.group(1)


f = open('place_code.google.com','rU')
urlP = r'(GET\s\S+puzzle\S+)\sHTTP'
urlLst = re.findall(urlP,f.read())
urlLst = sorted(list(set(urlLst)),key=CustSort)
print('\n'.join(urlLst)+'\n')



