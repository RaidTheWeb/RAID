from __future__ import print_function
from requests import get

def geoip(inp):
  result = get('https://api.hackertarget.com/geoip/?q=' + inp).text
  print(result)