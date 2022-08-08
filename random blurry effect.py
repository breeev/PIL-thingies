from random import randint
from PIL import Image
img=Image.open('brutalist_cube_houses.jpg')
Range=10
w,h=img.size
modeChoices=['normal','diagonal','inverted diagonal']
mode=2
def r():return Range if randint(0,1) else -Range
if not mode:
          for i in range(w):
                    for j in range(h):
                              try:img.putpixel((i,j),img.getpixel((i+r(),j+r())))
                              except:pass
if mode==1:
          for i in range(w):
                    for j in range(h):
                              l=r()
                              try:img.putpixel((i,j),img.getpixel((i+l,j+l)))
                              except:pass
if mode==2:
          for i in range(w):
                    for j in range(h):
                              l=r()
                              try:img.putpixel((i,j),img.getpixel((i+l,j-l)))
                              except:pass
img.show()