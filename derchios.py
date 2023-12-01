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
3 ---> Ip More Info
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
 os.system("nmap -sC -sV " + ip)

if(tool == "2"):
 os.system("clear")
 os.system("python tl1.py")
if(tool == "3"):
 rabite = input("İP daxil et")
 url = "https://ipinfo.io/" + rabite
 response = urlopen(url)
 data = json.load(response)
      
 table_data = [
  ["IP", data["ip"]],
  ["city", data["city"]],
  ["Region", data["region"]],
  ["Country", data["country"]],
  ["Postal Code", data["postal"]],
  ["Organization", data["org"]],
  ["ASN", data.get("asn", ["N/A"])[0]],
  ["IP Range", data.get("ip_range", "N/A")],
  ["Local Time", data.get("timezone", "N/A")],
  ["Timezone", data.get("timezone", "N/A")],
  ["Coordinates", data.get("loc", "N/A")],
  ["Privacy Detection", data.get("privacy", "N/A")]
  ]
      
 from tabulate import tabulate
 table = tabulate(table_data, headers=["Field", "Value"], tablefmt="grid")
 print_colored(table, Colors.BLUE)

 



                                    
