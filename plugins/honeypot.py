import sys
from requests import get


def honeypot(inp):
    honey = 'https://api.shodan.io/labs/honeyscore/%s?key=C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by' % inp
    try:
        result = get(honey).text
    except:
        result = None
        sys.stdout.write('%s No information available' % '\u001b[31;1m[-]\u001b[0m' + '\n')
    if result:
        if float(result) < 0.5:
            color = '\u001b[32;1m'
        else:
            color = '\u001b[31;1m'
        probability = str(float(result) * 10)
        sys.stdout.write('%s Acquired HoneyScore: %s%s%%%s' %
                         ('\u001b[34;1m[i]\u001b[0m', color, probability, '\u001b[0m') + '\n')