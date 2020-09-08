#CopyRight Apache-2.0
#Powered By Python 3.X
#Author : @Aμιρ-0x0 (AMJ)

#import libs

import os , sys ,readline , configparser ,re , platform,signal
from colorama import Fore
from os.path import expanduser
from lib.banner import banner 
from lib.update import update
from lib.version import version
from lib.completor import *
from lib.upgrade import upgrade
from core.listener import *
from core.rsmaker import RSMaker
from datetime import datetime

##################################################
environ = os.environ['SHELL']
environ = environ.split('/')
environ = environ[0:-2]
environ = '/'.join(environ)
locbin = environ+'/bin/sandsploit'

config = configparser.ConfigParser()
confloc = os.readlink(locbin)
confloc = confloc[0:-11]+"/lib/config.ini"
config.read(confloc)
pwd = config["DEFAULT"]
SANDpwd = pwd["SANDPWD"]


def controlc_signal(signal,frame):
    print ("\nInterrupt: use the 'exit' command to quit")



#Console Function
def console():
    path = None
    toolpart =None
    #File lists Function
    def mp(path):
        for root,dirs,files in os.walk(path): 
            for f in files: 
                print (f)
    #list Function
    def list():
        print ("\nTools\n===============")
        mp(path)
    try:
    
        while True:
            signal.signal(signal.SIGINT,controlc_signal)
            #Get PWD
            getcwd = os.getcwd()
            getdir = getcwd.split("/")
            pwd =  getdir[-1]
            #Get LocalHost Name
            plat = platform.node()
            #Nothing Special :)
            point = "→"
            #Check Tools Part Directory
            if path == None:
                None
            else:
                pth = path.split("/")
                toolpart = pth[-1]
            #Promot
            option = input (Fore.RESET+"\n[SSF@%s](%s){%s} %s "%(plat,pwd,toolpart,point))
            
            option2 = option.split(" ")
            #Conditions
            if option2[0] == "cd":
                
                def cd(path):
                    os.chdir(os.path.expanduser(path))
                try:
                    cd(option2[1])
                
                except:
                    print ("ERROR: No such file or directory: ",option2[1])
            elif option2[0] == 'run':
                
                    try:
                        
                        if option == "run":
                            print ("enter help to see how to use this command")
                        else:
                            run = option.split("run ")[1]
                            run2 = "%s/%s"%(path,run)
                            #exec(open(run2).read())
                            exst = os.path.isfile(run2) 
                            if exst:
                                os.system(run2)
                            else :
                                print ("Cannot find executable file")
                    except:
                        print ("Error !!!")
            
            elif option2[0] == 'use':
                try:
                    Spwd = SANDpwd.replace("'","")
                    check = '%s/module/%s'%(Spwd,option2[1])
                    exist = os.path.isdir(check) 
                    if exist:
                        path = check
                    else:
                        print ("Part not Found")
                    
                except:
                    print ("Part Not Found")
            elif option == 'list':
                if path == None:
                    print("\nTools\n===============")
                    print ("Tools NotFound")
                else:
                    list()


            elif option == 'help':
                #Menu
                print ('''

Command     Description
========    ============
banner      Change Banner
bash        Run Bash Shell
list        List of tools for each section
listener    Sniffing Port
python      Interactive Shell(Debuging Purposes)
RSMaker     Make Reverse Shell For Desktop Operating Systems
run         Run Tools In modules
use         Interact With Different Parts of Penetration Testing Tools
version     Show version of SandSploit
upgrade     Full Upgrade Freamworks
update      Update Exploits & Scripts Parts
exit        Exit From SSF
                ''')
            elif option == "version":
                version()
            elif option == "update":
                update()
            elif option == "upgrade":
                upgrade()
            elif option == "banner":
                banner()
            elif option == "RSMaker":
                RSMaker()
            elif option == "listener":
                listener()
            elif option == "exit":
                sys.exit()
            else:
                os.system(option)

    except EnvironmentError:
        print ("\nUnknown Error......")
        print ("Enter ""help"" to show commands....")

