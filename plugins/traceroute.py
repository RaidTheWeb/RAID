from __future__ import print_function
from requests import get

def traceroute(inp):
  result = get('https://api.hackertarget.com/nping/?q=' + inp).text
  print(result)