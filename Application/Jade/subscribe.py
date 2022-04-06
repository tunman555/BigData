import socket
import struct
import threading
import json
import time
mcst_prt={} 

with open('/home/system/asterix_collection/config/radar_port_mcast','r') as f :
    for line in f :
        mcst_prt[line.split()[0]] = int(line.split()[1]) ,line.split()[2] 

#with open('./config/mcst_prt.json','w') as f:
#    json.dump(mcst_prt,f)

def sub_mcast(MCAST_PORT,MCAST_ADDR):
    #create sock object
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)

    # allow multiple socket to  use the same port number
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    #bind portdd
    sock.bind((MCAST_ADDR,MCAST_PORT))

    #tell kernel that this is m.cast socket
    mreq = struct.pack('4sl',socket.inet_aton(MCAST_ADDR),socket.INADDR_ANY)

    sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)

    #set timeout 0 => poll the socket 
    #sock.setblocking(0)
    
    while True:
        time.sleep(10000)
       # pass


#threading part
for key in mcst_prt :
    x = threading.Thread(target=sub_mcast,args=(mcst_prt[key]))
    x.start()
