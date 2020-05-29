from PIL import Image

#return val of img object data type
img = Image.open('bulldog.jpg')
width, height = img.size

print("Width: ", width, "Height: ", height)

#if .jpg change to .png
if img.format == 'JPEG':
    img.save('bulldog2.png')