#!/usr/bin/python3
#Author @Aμιρ-0x0(AMJ)
import os  , sys , time , shutil , subprocess
from distutils.dir_util import copy_tree

def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)

#Global Vars
pwdold = None
pwdnew = None
dirPath = None
major = sys.version_info.major
minor = sys.version_info.minor
global pwdinit
global pwddesktop
global config
global confloc
global environ
global locbin
global locicon
global loclib
environ = os.environ['SHELL']
environ = environ.split('/')
environ = environ[0:-2]
environ = '/'.join(environ)
locbin = environ+'/bin/sandsploit'
locicon = '/usr/share/applications/sandsploit.desktop'
loclib = environ+'/lib'


class install:
    def setup(self,pwdnew,pwddesktop,pwdinit,config,confloc):
        if os.path.isdir(pwdnew):
            pass
        else:
            os.mkdir(pwdnew)

        py = ("%s/python%s.%s"%(loclib,major,minor))
        os.mkdir(py+"/ssf")
        src = "docs/ssf/"
        dst = py+"/ssf/"

        copytree(src,dst)
        copy_tree("project/",pwdnew)
        os.symlink(pwdinit,locbin)
        os.chmod(pwdinit,0o755)
        if os.path.isfile(locicon):
            shutil.copy(pwddesktop,locicon)
        cp = "%s/module"%pwdnew

        for root, dirs, files in os.walk(cp):
            for d in dirs:
                os.chmod(os.path.join(root, d),0o755)
            for f in files:
                os.chmod(os.path.join(root, f), 0o755)

        os.system("python3 -m pip install -r docs/requirements.txt")
        f = open(confloc,'w')
        f.write(config)
        f.close()
        
        print ("Installation completed successfully.....")

    def uninstall(self,dirPath):
        exist = os.path.isdir(dirPath) 
        major = sys.version_info.major
        minor = sys.version_info.minor
        
        py = ("%s/python%s.%s"%(loclib,major,minor))
        ppp = py+"/ssf/"
        exist = os.path.isdir(dirPath)
        if exist :

            shutil.rmtree(ppp)
            shutil.rmtree(dirPath)

            os.remove(locbin)
            #os.remove(locicon)
            print ("Uninstalled...")
            return None        
        else:
            print ("Sandsploit is not installed.....")




def main():

    uname =  subprocess.check_output("uname -o", shell=True)
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    elif sys.argv[1] == "install":
        pwdnew = input("Enter Installation Location <Default : /opt/sandsploit> : ")
        if pwdnew == "":
            pwdnew = "/opt/sandsploit/"
        pwdinit = "%s/__init__.py"%pwdnew
        pwddesktop = "%s/sandsploit.desktop"%pwdnew
        config ="[DEFAULT]\nSANDPWD='%s'"%pwdnew
        confloc = "%s/lib/config.ini"%pwdnew
        if os.geteuid() != 0:
            sys.exit("\n Run only with root access \n")
        install.setup(None,pwdnew,pwddesktop,pwdinit,config,confloc)
        
        print(pwdnew)
    elif sys.argv[1] == "uninstall":
        if os.geteuid() != 0:
            sys.exit("\n Run only with root access \n")
        dirPath = os.readlink('/usr/bin/sandsploit')
        dirPath = dirPath[0:-11]
        #print(dirPath)
        ui = install
        ui.uninstall(None,dirPath)

    else:
        print_usage()
        sys.exit(1)


def print_usage():
    print ('''usage :
    [!] - python3 setup.py install            Start installation
    [!] - python3 setup.py uninstall          Start uninstallation''')



if __name__ == '__main__':
    main()
