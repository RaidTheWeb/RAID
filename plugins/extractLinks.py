from __future__ import print_function
from requests import get

def extractLinks(url):
  result = get('https://api.hackertarget.com/pagelinks/?q=' + url).text
  print(result)