# Tool Name :- InfinitiServer
# Author :- Sathish Infiniti
# Date :- 25/4/2020


import sys
import os
from time import sleep
from core.system import *
from modules.logo import *

class upd(object):
  def chk_upd(self):
    while True:
      Mylogo()
      askv = input("\n\033[1;33m Do you want to Update InfinitiServer [\033[01;32mY/n\033[01;33m] >> \033[1;36m")
      if askv == "n" or askv == "N":
        break
      elif askv == "Y" or askv == "y":
        Mylogo()
        print("\n\033[01;32mUpdating InfinitiServer .........\033[01;36m")
        if os.path.exists(bpath+"git"):
          print("\033[01;32mDone ....\033[01;36m")
        else:
          os.system(pac+" update")
          os.system(pac+" install git -y")
        if system=="ubuntu":
          os.system("cd "+home+" && sudo git clone https://github.com/sathish-infiniti/InfinitiServer.git")
        else:
          os.system("cd "+home+" && git clone https://github.com/sathish-infiniti/InfinitiServer.git")
        if os.path.exists(home+"InfinitiServer"):
          os.system("cd "+home+"InfinitiServer && sh install")
          os.system("clear")
          os.system("infinitiserver start")
          sys.exit()
        else:
          Mylogo()
          print("\n\n\033[01;37m    [+] \033[01;31mSorry We can't update InfinitiServer !!\033[00m")
          print("\033[01;37m    [+] \033[01;31mYou are \033[01;33moffline \033[01;31m!!!\033[00m")
          print("\033[01;37m    [+] \033[01;31mCheck your \033[01;33mnetwork \033[01;31mconnection !!!\033[00m")
          print("\033[01;37m    [+] \033[01;31mTry again after sometime.\033[00m\n\n")
          sleep(4)
          break
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+askv+"\'")
        sleep(1)

def update():
  upd().chk_upd()