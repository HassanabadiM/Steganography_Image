from PIL import Image

password='testtest'
img=Image.open('image.jpg')

for i , chr in enumerate(password):
    r,g,b=img.getpixel((i*100,100))
    img.putpixel((i*100,100),(r,(ord(chr)+100),b))


img.save('encoded_image.png')
