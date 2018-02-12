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

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def CustSort(s):
  pat = r'/puzzle/\w+-\w+-(\w+)'
  key = re.search(pat,s)
  return key.group(1)

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  idx = filename.find('_')
  srvrNm = 'http://'+filename[idx+1:]
  urlF = open(filename,'rU')
  urlPattern = r'GET\s(\S+puzzle\S+)\sHTTP'
  urlLst = re.findall(urlPattern,urlF.read())
  urlLst = list(set(urlLst))
  if srvrNm =='animal':
    urlLst = sorted(urlLst)
  else:
    urlLst = sorted(urlLst, key=CustSort)
  urlLst = [srvrNm+s for s in urlLst]
  return urlLst
  # +++your code here+++
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
    f = open(dest_dir+'/index.html','w')
  else:
    f = open(dest_dir+'/index.html','w')
  for i in range(len(img_urls)):
    print("retrieving....")
    urllib.request.urlretrieve(img_urls[i],dest_dir+'/img'+str(i)+'.jpg')
    
  f.write('<html><body>')
  for i in range(len(img_urls)):
    f.write('<img src="img'+str(i)+'.jpg">')
  f.write('</body></html>')
  f.close()

  
  #sys.exit(0)
    
   
             
  
  # +++your code here+++
  

def main():
  args = sys.argv[1:]

  if not args:
    print ('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])
  

  if todir:
    download_images(img_urls, todir)
  else:
    print ('\n'.join(img_urls))

if __name__ == '__main__':
  main()
