import os
import sys
import time
print("""\033[32m
######   #######  ######    #####   ### ###   ######   #####    #####   
 ## ###   ##  ##   ##  ##  ##   ##   ## ##      ##    ### ###  ##   ##  
 ##  ##   ##       ##  ##  ##   ##   ## ##      ##    ##   ##  ##       
 ##  ##   ####     #####   ##        #####      ##    ##   ##   #####   
 ##  ##   ##       ##  ##  ##   ##   ## ##      ##    ##   ##       ##  
 ## ###   ##  ##   ##  ##  ##   ##   ## ##      ##    ### ###  ##   ##  
######   #######  #### ###  #####   ### ###   ######   #####    #####   
                                                                        
########  #####    #####   ###      
## ## ## ### ###  ### ###   ##      
   ##    ##   ##  ##   ##   ##      
   ##    ##   ##  ##   ##   ##      
   ##    ##   ##  ##   ##   ##      
   ##    ### ###  ### ###   ##  ##  
  ####    #####    #####   #######  
""")
import sys
import time

def loading_animation():
    symbols = ["-", "|", "/", "\\"]
    
    for i in range(1, 16):
        sys.stdout.write('\r')
        sys.stdout.write('-' * i + symbols[i % len(symbols)])
        sys.stdout.flush()
        time.sleep(0.2)

print("\033[35m\nYüləmələr yoxlanılır:")
loading_animation()
print("\033[32m\nYüləmələr yoxlanıldı: ok!")
os.system("clear")
print("""\033[33mSalam dəyərli istifadəçi! DERCHİOS toolunu istifadə etdiyiniz üçün təşəkkürlər!
Bir öncəki Red Tool proyektimdə Multiplatforma xüsusiyyəti var idi.və zaman alan bir boot sistemi var idi.
Burada isə Platformaya görə kod ayrımına az yer verilib.Və mümkünlük çərçivəsində bütün xüsusiyyətlər 
termux\linux\cloud shell və s. də çalışacaq.""")
import sys
import time

import sys
import time

class TerminalColors:
    BLUE = "\033[34m"
    RESET = "\033[0m"
def loading_animation2():
    symbols = ["|", "/","~", "\\"]
    
    for _ in range(3):
        for symbol in symbols:
            sys.stdout.write('\r' + TerminalColors.BLUE + symbol + TerminalColors.RESET)
            sys.stdout.flush()
            time.sleep(0.4)

loading_animation2()
os.system("clear")
import json
from urllib.request import urlopen
import os
import socket
import random
import time
import subprocess
import signal
import requests
print("""\033[32m
  _______________________________________
 /             DERCHIOS QALASI           \
/   _   _      from warband   _   _   _   \
|  | |_| |_| |   _   _   _   | |_| |_| |  |
|   \   _   /   | |_| |_| |   \   _   /   |
|    | | | |     \       /     | | | |    |
|    | |_| |______|     |______| |_| |    |
|    |              ___              |    |
|    |  _    _    (     )    _    _  |    |
|    | | |  |_|  (       )  |_|  | | |    |
|    | |_|       |       |       |_| |    |
|   /            |_______|            \   |
|  |___________________________________|  |
\              Derchios Tool              /
 \             By RED BITH               /
  \_____________________________________/
  """)
print("""\033[34m
Öncəliklə Derchiosu təcrübə etdiyiniz üçün təşəkkürlər!""")
print("""\033[33mChange:(rəqəm)
1 ---> Site adress\Ip port-scan\scan
2 ---> Telefon Nomresi Scan
3 --->
""")
tool = input("--->")
if(tool == "1"):
 os.system("clear")
 print("""\033[31mSeçiminiz: (1)
 #####################################
 # Method : port\scan                #
 # By RED-BITH                       #
 # Visit Our site! www.cyberdark.org #
 #####################################
 """)
 ip = input("Website\Ip --->")
 import os
 os.system("nmap -sC -sV -sS" + ip)

if(tool == "2"):
 import phonenumbers
 from phonenumbers import carrier, timezone, geocoder
 
 def clear_console():
  import os
  if os.name == 'posix':
   os.system('clear')
  elif os.name == 'nt':
   os.system('cls')
 
 def main():
  clear_console()
  print("""\033[37m
  ###################################
  # Method: Telefon Nomresi Scan(2) #
  ###################################
  """)
  number = input("Telefon nömrəsini girin:")
  if number.startswith("+"):
   try:
    parsed_number = phonenumbers.parse(number, None)
    if phonenumbers.is_valid_number(parsed_number):
     print("Yazılan nömrə doğrudur.")
     time_zones = timezone.time_zones_for_number(parsed_number)
     carrier_name = carrier.name_for_number(parsed_number, "az")
     region = geocoder.description_for_number(parsed_number, "az")
     print("Sim Şəbəkəsi:", carrier_name)
     print("Nömrənin Ölkəsi:", region)
     print("Nömrənin Bölgəsi:", time_zones)

    else:
     print("Yazılan nömrə səhvdir!")
   except phonenumbers.phonenumberutil.NumberFormatException:
    print("Xətalı nömrə formatı.")
  else:
   print("+Ölkə kodunu yazmaği unutdunuz!.")

 if __name__ == "__main__":
  main()




                                    
