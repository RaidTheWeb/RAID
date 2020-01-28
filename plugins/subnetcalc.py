import sys
from requests import get


def subnetcalc(inp):
    result = get('https://api.hackertarget.com/subnetcalc/?q=' + inp).text
    sys.stdout.write(result)