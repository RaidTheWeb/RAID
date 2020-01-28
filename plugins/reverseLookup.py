import sys
from requests import get


def reverseLookup(inp):
    lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % inp
    try:
        result = get(lookup).text
        sys.stdout.write(result)
    except:
        sys.stdout.write('%s Invalid IP address' % '\u001b[31;1m[-]\u001b[0m')