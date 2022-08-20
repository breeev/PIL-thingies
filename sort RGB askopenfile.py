from tkinter import Tk,Button
from tkinter.filedialog import askopenfilename
from PIL import Image
main=Tk()
img=Image.open(askopenfilename()).convert('RGB')
newimg=Image.new('RGB',img.size)
main.title('Select a sorting key')
r=Button(main,text='R')
g=Button(main,text='G')
b=Button(main,text='B')
a=Button(main,text='A')
any=Button(main,text='Any')
for b in [r,g,b,a,any]:b.pack(side='left')
main.mainloop()
newimg.putdata(sorted(list(img.getdata())))
if img.size[0]<300:newimg=newimg.resize(tuple(i*100 for i in img.size),Image.Resampling.BOX)
newimg.show()