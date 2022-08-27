from PIL import Image,ImageTk
from tkinter import Label,Tk
from tkinter.filedialog import askopenfilename
def read(img):
   l=[]
   for i in range(img.size[1]):
      l.append([])
      for j in range(img.size[0]):l[i].append(img.getpixel((j,i)))
   return l
e=0
def frameupdate():
   global ti,doodoo,tti,lab
   for h in range(len(doodoo)):
      for w in range(len(doodoo[h])):doodoo[h][w]=(*((i+1)%255 for i in doodoo[h][w]),)
   new=[j for i in doodoo for j in i]
   ti.putdata(new)
   tti=ImageTk.PhotoImage(ti)
   lab.config(i=tti)
   lab.after(10,frameupdate)
t=Tk()
img=Image.open(askopenfilename()).convert('RGB')
doodoo=read(img)
ti=Image.new('RGB',img.size)
ti.putdata(img.getdata())
tti=ImageTk.PhotoImage(ti)
lab=Label(t,i=tti)
lab.pack(fill='both',expand=True)
lab.after(50,frameupdate)
t.mainloop()
