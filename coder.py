from PIL import Image

pass='@testtest'
img=Image.open('img.jpg')

for i , chr in enumerate(pass):
    r,g,b=img.getpixel((i*100,100))
    img.putpixel((i*100,100),(r,(ord(chr)+100),b))


img.save('img2.png')
