#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
import subprocess
import sys
from datetime import datetime


# In[2]:


#Blank your screen
subprocess.call('clear', shell = True)


# In[ ]:


#Ask for input
remoteServer = input('Enter a remote host to scan:')
remoteServerIP = socket.gethostbyname(remoteServer)


# In[ ]:


#Print a nice banner with information on which host we are about to scan
print ('' * 60)
print ('please wait, scanning remote host', remoteServerIP)
print ('' * 60)


# In[ ]:


#Check the date and time the scan was started
t1 = datetime.now()


# In[ ]:


#Using the range function specify ports.
#Also we will do error hadnling
try:
    for port in range (5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ('Port {}: Open'.format(port))
        sock.close()

except KeyboardInterrupt:
    print ('you pressed Ctrl+C')
    sys.close ()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()
    
except socket.error:
    print ('couldnt connect to server')
    sys.exit ()


# In[ ]:


#Checking time again
t2 = datetime.now()


# In[ ]:


#calculate the difference in time to know how long the scan took
total = t2 - t1


# In[ ]:


#printing the information on the screen
print ('scanning ompleted in: ', total)

