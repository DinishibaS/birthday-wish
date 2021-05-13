from PIL import Image, ImageFilter
from PIL import ImageFont
from PIL import ImageDraw 

im1 = Image.open('birthday_template.jpg')

im2 = Image.open('Fabian Ferno.jpg')
width  = im2.size[0]
height = im2.size[1]
ar = round((width / height),2)
print (ar)
if ar == 1.77:
    size = (400, 400)
    im2 = im2.resize(size)    

elif ar >= 0.67 and ar < 1.77:
    size = (500, 500)
    im2 = im2.resize(size)

else:
    size = (400, 400)
    im2 = im2.resize(size)    

mask_im = Image.new("L", im2.size, 0)
draw = ImageDraw.Draw(mask_im)
draw.ellipse((15, 15, 396, 383), fill=255)

mask_im_blur = mask_im.filter(ImageFilter.GaussianBlur(13))

back_im = im1.copy()
back_im.paste(im2, (259, -23), mask_im_blur)

draw = ImageDraw.Draw(back_im)

# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("Fonts/Montserrat-Black.ttf", 65)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((45,520),"Sample guy",(255,255,255),font=font)

# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("Fonts/Montserrat-Black.ttf", 16)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((10, 0),"Feb 31",(255,255,255),font=font)

back_im.save('sample-out.jpg', quality=100)





