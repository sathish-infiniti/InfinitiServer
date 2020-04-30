# Tool Name :- InfinitiServer
# Author :- Sathish Infiniti
# Date :- 25/4/2020


import sys
import os
from time import sleep
from system import *
from logo import *

class Un(object):
  def Uni(self):
    while True:
      Mylogo()
      ask = input("\n\n\033[1;33m Do you want to uninstall InfinitiServer [\033[01;32mY/n\033[01;33m] >> \033[00m")
      if ask == "n" or ask == "N":
        break
      elif ask == "Y" or ask == "y":
        if system=="ubuntu":
          os.system("cd "+spath+" && sudo rm -rf InfinitiServer")
          os.system("sudo rm -rf "+bpath+"infinitiserver")
          os.system("cd "+spath+" && sudo rm -rf .host.aex .port.aex .path.aex .serv.lock .h.lock")
        else:
          os.system("rm -rf "+bpath+"infinitiserver")
          os.system("cd "+spath+" && rm -rf InfinitiServer")
          os.system("cd "+spath+" && rm -rf .host.aex .port.aex .path.aex .serv.lock .h.lock")
        exit()
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+ask+"\'")
        sleep(1)

Un().Uni()