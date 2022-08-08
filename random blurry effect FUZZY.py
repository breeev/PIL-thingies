from random import randint
from numpy import arange
from numpy.random import choice
from PIL import Image
img=Image.open('brutalist_cube_houses.jpg')
Range=40
w,h=img.size
modeChoices=['normal','diagonal','inverted diagonal']
mode=1
if not mode:
          def r(i):
                    a=randint(0,2)
                    return i if not a else i+Range if a==1 else i-Range
          for i in range(w):
                    for j in range(h):
                              try:img.putpixel((i,j),img.getpixel((r(i),r(j))))
                              except:pass
if mode==1:
          def r():
                    a=randint(0,2)
                    return a if not a else Range if a==1 else -Range
          for i in range(w):
                    for j in range(h):
                              l=r()
                              li=[i,i+l]
                              li.sort()
                              lj=[j,j+l]
                              lj.sort()
                              try:img.putpixel((i,j),img.getpixel((randint(*li),randint(*lj))))
                              except:pass
if mode==2:
          def r():
                    a=randint(0,2)
                    return a if not a else Range if a==1 else -Range
          for i in range(w):
                    for j in range(h):
                              l=r()
                              li=[i,i+l]
                              li.sort()
                              lj=[j,j-l]
                              lj.sort()
                              try:img.putpixel((i,j),img.getpixel((randint(*li),randint(*lj))))
                              except:pass
img.show()