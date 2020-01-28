from __future__ import print_function
from requests import get

def headers(domain):
  result = get('https://api.hackertarget.com/httpheaders/?q=' + domain).text
  print(result)