import pyfiglet 
import sys 
import socket
import argparse
import json

from datetime import datetime 

# load json port list
with open('portlist.json') as json_file:
    data = json.load(json_file)
    
parser = argparse.ArgumentParser()
parser.add_argument("host",  help="Nombre de archivo a procesar")
parser.add_argument("protocol",  help="Nombre de archivo a procesar")
parser.add_argument("init", help="Nombre de archivo a procesar")
parser.add_argument("end", help="Nombre de archivo a procesar")

args = parser.parse_args()
 
# Aquí procesamos lo que se tiene que hacer con cada argumento
if args.protocol:
    protocol = args.protocol
 
if args.host:
    target = args.host

if args.init:
    x = int(args.init)

if args.end:
    y = int(args.end)

ascii_banner = pyfiglet.figlet_format("portScan") 
print(ascii_banner) 
   
# Eligiendo target
#target = input(print("Set hostname"))
#x = int(input(print("Set lower port: ")))
#y = int(input(print("Set higher port: ")))
#y = y+1
#protocol = input(print("Set protocol 'tcp/udp': "))


protocol = protocol.lower()

if protocol != "tcp" and protocol !="udp":
    print("Invalid protocol, trying whith TCP")
    protocol = "tcp"

#if len(sys.argv) == 2: 
      
    # translate hostname to IPv4 
    #target = socket.gethostbyname(sys.argv[1])  
#else: 
    #print("Invalid ammount of Argument") 
  
# Banner 
print("-" * 50)
print("Scanning Target: " + target)
print("Target port range: " + str(x) + " to " + str(y))
print("protocol: " + protocol ) 
print("Scanning started at:" + str(datetime.now()))
print("-" * 50) 

# Scan TCP
if protocol == "tcp":
    try: 
      
        # escanea los puertos elegidos 
        for port in range(x,y): 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            socket.setdefaulttimeout(1) 
            description = data[str(x)][0]['description']
            
        # returns an error indicator 
            result = s.connect_ex((target,port)) 
            if result ==0: 
                print("Port "+str(x)+" open : " + description + " ".format(port)) 
            s.close()
        
            
       
    except KeyboardInterrupt: 
            print("\n Exitting Program !!!!") 
            sys.exit() 
    except socket.gaierror: 
            print("\n Hostname Could Not Be Resolved !!!!") 
            sys.exit() 
    except socket.error: 
            print("\ Server not responding !!!!") 
            sys.exit()
            
# Scan UDP
if protocol == "udp":
    try: 
      
        # escanea los puertos elegidos 
        for port in range(x,y): 
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            socket.setdefaulttimeout(1) 
          
        # returns an error indicator 
            result = s.connect_ex((target,port)) 
            if result ==0: 
                print("Port {} is open".format(port)) 
            s.close() 
          
    except KeyboardInterrupt: 
            print("\n Exitting Program !!!!") 
            sys.exit() 
    except socket.gaierror: 
            print("\n Hostname Could Not Be Resolved !!!!") 
            sys.exit() 
    except socket.error: 
            print("\ Server not responding !!!!") 
            sys.exit() 
