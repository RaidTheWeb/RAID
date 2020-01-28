from __future__ import print_function
import re
import sys, os
import requests
from plugins.censys import censys
from plugins.dnsLookup import dnsLookup
from plugins.nmap import nmap
from plugins.detectCMS import detectCMS
from plugins.whois import whois
from plugins.honeypot import honeypot
from plugins.Subdomains import subdomains
from plugins.reverseLookup import reverseLookup
from plugins.detectTech import detectTech
from plugins.geoip import geoip
from plugins.nping import nping
from plugins.headers import headers
from plugins.extractLinks import extractLinks
from plugins.subnetcalc import subnetcalc
from plugins.aslookup import aslookup
from plugins.analytics import analytics
from plugins.traceroute import traceroute


if sys.version_info < (3,0):
  input = raw_input

def hq(option):
  option = option
  if option == '1':
    ip = input('\u001b[38;5;88mIP$ \u001b[0m')
    censys(ip)
  if option == '2':
    inp = input('\u001b[38;5;88mDomain/IP$ \u001b[0m')
    dnsLookup(inp)
  if option == '3':
    inp = input('\u001b[38;5;88mDomain/IP$ \u001b[0m')
    nmap(inp)
  if option == '4':
    domain = input('\u001b[38;5;88mDomain$ \u001b[0m')
    detectCMS(domain)
  if option == '5':
    inp = input('\u001b[38;5;88mDomain/IP$ \u001b[0m')
    whois(inp)
  if option == '6':
    inp = input('\u001b[38;5;88mDomain/IP$ \u001b[0m')
    honeypot(inp)
  if option == '7':
    domain = input('\u001b[38;5;88mDomain$ \u001b[0m')
    subdomains(domain)
  if option == '8':
    inp = input('\u001b[38;5;88mDomain/IP$ \u001b[0m')
    reverseLookup(inp)
  if option == '9':
    url = input('\u001b[38;5;88mURL$ \u001b[0m')
    detectTech(url)
  if option == '10':
    inp = input('\u001b[38;5;88mDomain/IP$ \u001b[0m')
    geoip(inp)
  if option == '11':
    inp = input('\u001b[38;5;88mDomain/IP$ \u001b[0m')
    nping(inp)
  if option == '12':
    domain = input('\u001b[38;5;88mDomain$ \u001b[0m')
    headers(domain)
  if option == '13':
    url = input('\u001b[38;5;88mURL$ \u001b[0m')
    extractLinks(url)
  if option == '14':
    inp = input('\u001b[38;5;88mDomain/IP$ \u001b[0m')
    subnetcalc(inp)
  if option == '15':
    iap = input('\u001b[38;5;88mIP/ASN$ \u001b[0m')
    aslookup(iap)
  if option == '16':
    domup = input('\u001b[38;5;88mDomain/UA/pub$ \u001b[0m')
    analytics(domup)
  if option == '17':
    inp = input('\u001b[38;5;88mDomain/IP$ \u001b[0m')
    traceroute(inp)
  if option == '18':
    os.system('python3 plugins/sisp.py')
  if option == '19':
    os.system('python3 plugins/simp.py')
  if option == '20':
    os.system('python3 plugins/misp.py')
  if option == '21':
    os.system('python3 plugins/mimp.py')
  if option == '22':
    os.system('python3 plugins/halfopen.py')
  if option == '23':
    os.system('python3 plugins/fin.py')
  if option == '24':
    os.system('python3 plugins/ack.py')
  if option == '25':
    os.system('python3 plugins/pingofdeath.py')