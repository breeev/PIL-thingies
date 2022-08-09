def update(r,g,b):
          if sum([not i for i in [r,g,b]])==2:
                    # 2 vars empty means one is full
                    if r:r,g=254,1
                    elif g:g,b=254,1
                    elif b:b,r=254,1
          else:
                    if not r:
                              if b==255:g-=1
                              else:b+=1
                    elif not g:
                              if r==255:b-=1
                              else:r+=1
                    elif not b:
                              if g==255:r-=1
                              else:g+=1
          return r,g,b
def main():
          from PIL import Image
          img=Image.new('RGB',size=(200,)*2)
          w,h=img.size
          r,g,b=(255,0,0)
          for i in range(h):
                    for j in range(w):
                              img.putpixel((j,i),(r,g,b))
                              if not j%(w/10):r,g,b=update(r,g,b)
          img.show()