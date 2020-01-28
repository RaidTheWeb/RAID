import sys
from requests import get


def nmap(inp):
    result = get('http://api.hackertarget.com/nmap/?q=' + inp).text
    sys.stdout.write(result)