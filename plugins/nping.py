from __future__ import print_function
from requests import get

def nping(target):
  result = get('https://api.hackertarget.com/nping/?q=' + target).text
  print(result)