from PIL import Image
from gradient import update
img=Image.new('RGB',size=(200,)*2)
w,h=img.size
r,g,b=(255,0,0)
for i in range(h):
          for j in range(w):
                    pass
                    ## img.putpixel((j,i),(255*(j%2 or i%2),)*3)
                    # img.putpixel((j,i),(r,g,b))
                    # if not j%(w/10):r,g,b=update(r,g,b)
img.show()