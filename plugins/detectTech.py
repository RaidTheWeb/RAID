import sys
import json
from requests import get


def detectTech(url):
    data = get('https://api.wappalyzer.com/lookup-basic/beta/?url=' + url).text
    jsoned_data = json.loads(data)
    technologies = []
    if not data == '':
      sys.stdout.write(data)
    else:
      sys.stdout.write('No Response')