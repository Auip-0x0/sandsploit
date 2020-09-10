#!/usr/bin/python3
#CopyRight Apache-2.0 
#Author : @Aμιρ-0x0 (AMJ)

#Import Libs
import sys ,os , time , readline , subprocess
from os.path import expanduser
from lib.__init__ import *

#Create main Function
def main():
    #Check User ID
    if  os.geteuid() == 0:
        print ("\n\033[91m Warning! you run Framework with root user! \n")
    #slow print Function
    def slowprint(s):
        for c in s + '\n' :
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(3. / 100)

    #Set Terminal Window Size
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=110))
    slowprint("\033[91m[!] Starting The Sandsploit Framework console... ")
    time.sleep(4)
    #Clear Page
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    """
    uname = subprocess.check_output("uname -o", shell=True)
    if 'Android' in str(uname):
        banner()
        termux_console()
    else:
        banner()
        console()
    """
    banner()
    console()
if __name__ == "__main__":
    main()
    