from math import cos
from PIL import Image
from random import randint
img=Image.new('RGB',size=(2000,)*2)
new=[]
j=None
def r():global j;return randint(0,j)
for i in range(len(img.getdata())):
          j=int((cos(i/20000)+1)*127)
          new.append((r(),r(),r()))
img.putdata(new)
img.show()