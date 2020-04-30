# Tool Name :- InfinitiServer
# Author :- Sathish Infiniti
# Date :- 25/4/2020


import sys
import os
from time import sleep
from core.system import *
from modules.php import *
from modules.pyweb import *

def default_s():
  if os.path.exists(bpath+"php"):
    php()
  else:
    pyweb()