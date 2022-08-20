from PIL import Image
from gradient import update
from random import randint
img=Image.new('RGB',size=(200,)*2)
w,h=img.size
r,g,b=(255,0,0)
i=0
def pix(x,y):
          global i
          i+=1
          img.putpixel((x,y),(255,)*3)
          ok=[p for p in[(x,(y-1)%h),((x-1)%w,y),(x,(y+1)%h),((x+1)%w,y)]if(not img.getpixel(p)[0])]
          if ok:pix(*ok[randint(0,len(ok)-1)])
                    # else:print('ok')
# for i in range(h):
#           for j in range(w):
#                     img.putpixel((j,i),(255*(j%2 or i%2),)*3)
#                     # img.putpixel((j,i),(r,g,b))
#                     # if not j%(w/10):r,g,b=update(r,g,b)
pix(w//2,h//2)
img.show()