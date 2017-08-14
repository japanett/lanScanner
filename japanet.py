# Python 2.7.13
# pip install pyfiglet, termcolor, colorama

#!/usr/bin/env python
import sys
import subprocess
import urllib2
import json
import codecs
import termcolor
from datetime import datetime
from scapy.all import srp, Ether, ARP, conf
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from pyfiglet import figlet_format


def banner():
    subprocess.call('clear', shell = True) # Clear shell
    # print termcolor.colored('string', 'color')
    print termcolor.colored((figlet_format('Japanet', font = 'larry3d')), 'green')
    print termcolor.colored(("\t\t\t\t\tLAN Scanner v0.1"), 'red')
    return

def scanLAN():
    try:
        banner()
        interface = raw_input("\n[*] Interface (IE: wlan0): ") #Gets interface to scan
        ips = raw_input("[*] Enter range of IPs (IE: 192.168.2.0/24): ") # Gets IP or IP range to scan
        # Write results to a file ?
        yorn = str(raw_input("\n[*] Create a file to store the results? (y/n): "))
        if yorn == 'y':
            path = str(raw_input("Path (IE: /root/folder/test.txt): "))
    except KeyboardInterrupt: # Discontinue the scan
        exit()
    
     
    print "\n[*] Scanning, please wait..." 
    start_time = datetime.now() # Starting time counter

    conf.verb = 0 # Start Scanning
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), timeout = 2, iface = interface, inter=0.1)

    # Setting up results display
     
    banner()
    print "\n\t\t [ LIVE HOSTS ]"
    print "\n\tMAC\t\t  IP\t\tCompany"

    # Printing results
    url = "http://macvendors.co/api/"

    for snd, rcv in ans:

        ip = rcv.sprintf(r"%ARP.psrc%")
        mac = str(rcv.sprintf(r"%Ether.src%"))
        
        # Consults MAC vendor API
        request = urllib2.Request(url+mac, headers={'User-Agent' : "API Browser"}) 
        response = urllib2.urlopen(request)
        reader = codecs.getreader("utf-8")
        obj = json.load(reader(response))

    
        print  mac, " - ", ip, " - ", (obj['result']['company'])
        # Displaying MAC - IP - Company
        if yorn == 'y': 
            teste = (mac, str(ip), str((obj['result']['company'])))
            writeFile(path, teste) # Writing to file
            print "\n[*] File stored as: ", path   

    stop_time = datetime.now() # Stop clock for total duration
    total_time = stop_time - start_time
    print "\n[*] Scan Completed (TIME: %s)" %(total_time)
    return

def writeFile(path, string):
    with open(path, 'a') as outfile:
        json.dump(string, outfile, indent = 2)
    return

def portScan():
   banner()
   print "[*] (Port Scanner)\nStill not implemented :("
   return

def serviceScan():
    banner()
    print "[*] (Service Scanner)\nStill not implemented :("
    return

def osScan():
    banner()
    print "[*] (Operational System Scanner)\nStill not implemented :("
    return

def exit():
    banner()
    print "\n[*] Shutting down, thank you for using Japanet's LAN Scanner. "
    sys.exit(1)
    return

def main():
    banner()
    opt_list = [scanLAN,
                portScan,
                serviceScan,
                osScan,
                exit]

    while(True):
        try:
            print "\nTell me what to do: "
            print termcolor.colored("\n\t[1]", "red"), "Scan LAN"
            print termcolor.colored("\t[2]", "blue"), "Port Scan"
            print termcolor.colored("\t[3]", "blue"), "Service Scan"
            print termcolor.colored("\t[4]", "blue"), "OS Scan"
            print termcolor.colored("\t[5]", "red"), "Exit"
            opt_choice = int(raw_input("\nChoose: "))
            opt_choice -= 1
            opt_list[opt_choice]()
        except KeyboardInterrupt:
            exit()
    return

if __name__ == "__main__":
    main()
