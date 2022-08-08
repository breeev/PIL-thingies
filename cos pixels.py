from math import cos,sin,tan
from PIL import Image
size=1920
img=Image.new('RGB',size=(size,)*2)
new=[]
j=None
length=len(img.getdata())
for i in range(length):new.append((int((cos(i/length)+1)*127),int((sin(i/length)+1)*127),int((tan(i/length)+1)*127)))
img.putdata(new)
img.show()