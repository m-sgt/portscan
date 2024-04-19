'''
Matt Sargent
4/17/24
portscan.py

Accepts an IP address and checks if ports 22, 53, and 80 are open or closed. The port numbers can be changed in the 'tPorts' argument of pScan() function.
'''

# Import socket library for connecting to IPs
from socket import *

# connectionScan function. Accepts a host 'tHost' and a list of ports 'tPort'
def conScan(tHost, tPort):
    try:
        conskt = socket(AF_INET, SOCK_STREAM)
        # Attempt to connect to tHost on tPort
        conskt.connect((tHost, tPort))

        # If successful
        print("[+] %s /tcp open\n" % tPort)
        conskt.close()

    except:
       # Otherwise, let the user know the connection failed
       print("[-] %s /tcp closed\n" % tPort)
       conskt.close()

# portScan function. Accepts the user inputted target host 'tHost' and list of ports from pScan() function call 'tPorts'
def pScan(tHost, tPorts):

    # Loop through the list of port numbers and call a conScan() for each
    for tPort in tPorts:
        print("Scanning port %d on IP: %s" % (tPort, tHost))
        # Call conScan() and attempt a connection
        conScan(tHost, int(tPort))
        # Set timeout to 1 second before trying the next port
        setdefaulttimeout(1)

# Use range(1, 1023) to scan every port
pScan(input("Enter IP address to be scanned: "), [22, 53, 80])