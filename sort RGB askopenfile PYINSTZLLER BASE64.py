from base64 import encodebytes,decodebytes
exec(decodebytes(encodebytes(b"""from math import sqrt,ceil
from operator import mul
from pathlib import Path
from tkinter import BooleanVar, Checkbutton, IntVar, Label, Spinbox, Tk,Button
from tkinter.filedialog import askopenfilename,askdirectory
from PIL import Image
from random import choice
from string import ascii_lowercase
V=None
ok=False
main=Tk()
def buttonHandle(v):
   global V,ok
   main.destroy()
   V=v
   ok=True
img=Image.open(askopenfilename(parent=main,filetypes=(
      ('Portable Network Graphics','*.png'),
      ('Joint Photographic Experts Group',['*.jpg','*.jpeg']),
      ('Other files','*.*')
   ),title='Select an image')).convert('RGBA')
newimg=Image.new('RGB',(ceil(sqrt(mul(*img.size))),)*2)
main.title('Select a sorting key')
r=Button(main,text='R',bg='red',fg='white',command=lambda:buttonHandle(0))
g=Button(main,text='G',bg='green',fg='white',command=lambda:buttonHandle(1))
b=Button(main,text='B',bg='blue',fg='white',command=lambda:buttonHandle(2))
a=Button(main,text='A',bg='black',fg='white',command=lambda:buttonHandle(3))
any=Button(main,text='Any',command=lambda:buttonHandle(None))
sv=IntVar(main)
s=Spinbox(main,textvariable=sv,values=[i for i in range(-51,52,2)],width=3)
sv.set(21)
zv=BooleanVar(main,value=True)
z=Checkbutton(main,variable=zv,text='Save')
q=Label(main,text=str(newimg.size))
for b in [r,g,b,a,any,s,z,q]:b.pack(side='left',padx=4,pady=4)
main.mainloop()
if ok:
   main=Tk()
   Label(main,text='Working hard...').pack()
   newimg.putdata(sorted(list(img.getdata()),key=None if not V else lambda x:x[V]))
   svv=sv.get()
   newimg=newimg.resize((int(newimg.size[0]*(svv if svv>0 else 1/(-1*svv))),)*2,Image.Resampling.BOX)
   if zv.get():
      p=askdirectory(parent=main,title='Select a destination (random file name)')
      if p:newimg.save(Path(p).joinpath(''.join([choice(ascii_lowercase) for i in range(8)])+'.png').absolute())
   else:newimg.show()""")))