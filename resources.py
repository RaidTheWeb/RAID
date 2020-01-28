from __future__ import print_function
from platform import python_version
from colors import *
import hq, os


import sys
import logging


if sys.version_info < (3, 0):
  input = raw_input

version = '1.4'
pyversion = python_version()

platform = sys.platform

def logo():
  sys.stdout.write('''\u001b[32;1m
            -/oyhdmmmdhys+-`                                                                        
        -odMMMMNdhyyyhdmMMMMds:          .dddddddddhy/       `ydds       ydd-  hdddddddhs/`         
     `+mMMNy+-    ```    ./ymMMNo.       yMMhsssssyNMMo     .mMMMN      -MMm  /MMmyyyyhmMMm.        
     mMMy:  .+ydNMMMMMNdy+-  -sNMN      .MMN       yMMs    /NMhdMM:     hMM/  mMM-      yMMy        
     `:` .omMMMdyo+++oshNMMNs. `:`      yMMy:::::+hMMh`   sMMs oMMs    :MMm  /MMh       +MMy        
        `MMNs:  `-:::-`  -sNMM-        .MMMMMMMMMNds-   `hMM+``:MMN    hMM/  mMM-       mMM:        
         .:` .smMMMMMMMms-  :-         yMMo.../NMMo    -mMMMMMMMMMM-  :MMm  /MMh       sMMy         
            :MMNs/-.-/smMM+           .MMm     -MMM+  +MMd::::::dMMs  hMM/  mMM-     -hMMs          
             ::  /yhy+  ::            yMM+      +MMM:yMMy       +MMm -MMm  +MMMhhhddNMMh-           
                oMMMMMy              `yyy        oyyhyy+        .yyy`+yy:  syyyyyyyso:`             
                :MMMMM+                                                                             
                 `/+/.    
                                                                      
''')
  sys.stdout.write('━'*100 + '\u001b[0m \n')

def menu():
  sys.stdout.write('''
[1] \u001b[38;5;22mCensys\u001b[0m
[2] \u001b[38;5;22mDNS Lookup\u001b[0m
[3] \u001b[38;5;22mNmap\u001b[0m
[4] \u001b[38;5;22mDetect CMS\u001b[0m
[5] \u001b[38;5;22mWhois Lookup\u001b[0m
[6] \u001b[38;5;22mDetect Honeypot\u001b[0m
[7] \u001b[38;5;22mFind Subdomains\u001b[0m
[8] \u001b[38;5;22mReverse IP Lookup\u001b[0m
[9] \u001b[38;5;22mDetect Technologies\u001b[0m
[10] \u001b[38;5;22mGeoIP\u001b[0m
[11] \u001b[38;5;22mNPing\u001b[0m
[12] \u001b[38;5;22mHeaders\u001b[0m
[13] \u001b[38;5;22mExtract Links\u001b[0m
[14] \u001b[38;5;22mSubnet Calculator\u001b[0m
[15] \u001b[38;5;22mAS Lookup\u001b[0m
[16] \u001b[38;5;22mAnalytics Lookup\u001b[0m
[17] \u001b[38;5;22mTraceroute\u001b[0m
[18] \u001b[38;5;22mSISP DoS\u001b[0m
[19] \u001b[38;5;22mSIMP DDoS\u001b[0m
[20] \u001b[38;5;22mMISP DDoS\u001b[0m
[21] \u001b[38;5;22mMIMP DDoS\u001b[0m
[22] \u001b[38;5;22mHalf-Open Scan\u001b[0m
[23] \u001b[38;5;22mFIN Scan\u001b[0m
[24] \u001b[38;5;22mACK Flag Scan\u001b[0m
[25] \u001b[38;5;22mPing Of Death\u001b[0m
''')
  sys.stdout.write('━'*100 + '\n') 



def console():
  os.system('clear')
  logo()
  sys.stdout.write('Welcome To RAID ' + version + '\n' + 'Python ' + pyversion + '\n')
  sys.stdout.write('\n')
  while True:
    menu()
    result = False
    option = input('\u001b[38;5;88m$ \u001b[0m')
    hq.hq(option)
  



