import sys
from requests import get


def dnsLookup(inp):
    result = get('http://api.hackertarget.com/dnslookup/?q=' + inp).text
    sys.stdout.write(result)