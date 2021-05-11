from PIL import Image, ImageFilter
from PIL import ImageFont
from PIL import ImageDraw 

im1 = Image.open('birthday_template.jpg')

im2 = Image.open('Dini_profile.jpg')
size = (400, 400)
im2 = im2.resize(size)

mask_im = Image.new("L", im2.size, 0)
draw = ImageDraw.Draw(mask_im)
draw.ellipse((15, 15, 396, 383), fill=255)

mask_im_blur = mask_im.filter(ImageFilter.GaussianBlur(10))

back_im = im1.copy()
back_im.paste(im2, (260, -25), mask_im_blur)

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
