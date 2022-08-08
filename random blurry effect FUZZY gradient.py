from random import randint
from numpy import arange
from numpy.random import choice
from PIL import Image
img=Image.open('brutalist_cube_houses.jpg')
Range=40
w,h=img.size
modeChoices=['normal','diagonal','inverted diagonal']
mode=1
p=[round(i/Range/10/1.025/2,9) for i in range(1,Range+1)]
p.reverse()
if not mode:
          def r(i):
                    a=randint(0,2)
                    return i if not a else choice(arange(i,i+Range),p=p) if a==1 else choice(arange(i,i+Range),p=p)
          for i in range(w):
                    for j in range(h):
                              try:img.putpixel((i,j),img.getpixel((r(i),r(j))))
                              except:pass
if mode==1:
          def r():
                    a=randint(0,2)
                    return a if not a else choice(arange(Range),p=p) if a==1 else -choice(arange(Range),p=p)
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
                    return a if not a else choice(arange(Range),p=p) if a==1 else -choice(arange(Range),p=p)
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