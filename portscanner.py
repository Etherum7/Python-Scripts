#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import socket
from datetime import datetime


# In[ ]:


if len(sys.argv) ==2 :
    target =  socket.gethostbyname(sys.argv[1])
else :
    print('You didnt give required number of arguements')
    print('Syntax $ python3 portscanner.py <ip>')
    sys.exit()
# Banner
print("-" * 50)
print("Scanning  Target" , target)
print("Time Started " + str(datetime.now()))
print("-" * 100)
try:
    print('Checking ports between 20 and 85')
    for port in range(20, 85):
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result==0:
            print('PORT {} IS OPEN'.format(port))
        s.close()
except KeyboardInterrupt:
    print("-" * 50)
    print('\n User has interrupted')
    sys.exit()
except socket.gaierror:
    print('Host Name could not bbe resolved')
    sys.exit();
except socket.error:
    print("Couldn't connect to server")

