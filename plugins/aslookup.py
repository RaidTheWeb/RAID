import sys
from requests import get


def aslookup(ip):
    result = get('https://api.hackertarget.com/aslookup/?q=' + ip).text
    sys.stdout.write(result)