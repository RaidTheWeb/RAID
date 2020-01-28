import sys
from scapy.all import *

if sys.version_info < (3,0):
  input = raw_input

src = input('Enter Spoofed IP:\t')
dst = input('Enter Target IP:\t')

IP1 = IP(src=src, dst=dst)
sy1 = TCP(sport=1024, dport=80, flags='F', seq=12345)
pkt = IP1 / sy1
p = sr1(pkt)
p.show()