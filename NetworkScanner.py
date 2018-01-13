import subprocess
import re

child = subprocess.Popen(["arp", "-a"],stdout=subprocess.PIPE)
outputs =child.stdout.readlines()

for output in outputs:
    mystring=output
    sub=re.compile(' ').split(mystring)
    ipAddrss=sub[1]
    print sub
    print "****************** SYSTEM CONNECTED ******************"
    #Formatting IPAddress
    ipAddrss=re.compile('\\(').split(ipAddrss)[1]
    ipAddrss=re.compile('\\)').split(ipAddrss)[0]
    print "IP Address: "+ipAddrss
    
    #Mac Address
    macAddress=sub[3]
    print "MAC Address: "+macAddress
    
    #Printing interface
    connectionInterface=sub[5]
    print "Printing Interface: "+connectionInterface
    
    #Printing Scope
    scope=sub[6]
    print "Scope: "+scope
    
    #Connection Through
    connectionThrough=sub[7]
    print "Connected Through: "+connectionThrough
