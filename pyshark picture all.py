from math import sqrt
from pyshark import LiveCapture
from scapy.all import conf,get_if_addr
from PIL import Image
own=get_if_addr(conf.iface)
cap=LiveCapture(display_filter='ip and((not string(ip.src) matches "^192.168*")or(not string(ip.dst) matches "^192.168*"))')
n=int(input('Picture size (square): '))**2
downlink=[]
uplink=[]
for packet in cap.sniff_continuously():
   if len(downlink)<n and packet.ip.dst==own:downlink.append(tuple(int(i) for i in packet.ip.src.split('.')[:-1]))
   elif len(uplink)<n and packet.ip.src==own:uplink.append(tuple(int(i) for i in packet.ip.dst.split('.')[:-1]))
   elif len(downlink)==len(uplink)==n:break
inin=Image.new('RGBA',(int(sqrt(n)),)*2)
inin.putdata(downlink)
inin.save('downlink.png')
inin=Image.new('RGBA',(int(sqrt(n)),)*2)
inin.putdata(uplink)
inin.save('uplink.png')
print('all done')