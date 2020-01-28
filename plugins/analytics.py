import sys
from requests import get


def analytics(domain):
    result = get('https://api.hackertarget.com/analyticslookup/?q=' + domain).text
    sys.stdout.write(result)