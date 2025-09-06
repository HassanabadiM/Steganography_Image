from PIL import Image

password=''
len_considered_password=8

img=Image.open('encoded_image.png')

for i in range(len_considered_password):
    pix= img.getpixel((i*100,100))
    password+=chr(pix[1]-100)


print(password)
