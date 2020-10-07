# documentation
# https://pillow.readthedocs.io/en/stable/index.html

from PIL import Image, ImageFilter, ImageDraw

# Open image
try:
    img = Image.open("pic.jpg")
except:
    print("Unable to load image")

# print image details
print(img.format, img.size, img.mode)
img.show()

# Blur the image
blurred_img = img.filter(ImageFilter.BLUR)
blurred_img.show()

# Contour image
countour_img = img.filter(ImageFilter.CONTOUR)
countour_img.show()

# Enhance edge
enhance_img = img.filter(ImageFilter.EDGE_ENHANCE)
enhance_img.show()

# Find Edge
edge_img = img.filter(ImageFilter.FIND_EDGES)
edge_img.show()

# smooth image
smooth_img = img.filter(ImageFilter.SMOOTH)
smooth_img.show()

# crop image
cropped_img = img.crop((0, 0 , 150 , 250))
cropped_img.show()

# grayscale image
grayscale_img = img.convert("L")
grayscale_img.show()

# resize image
resized_img = img.resize((500, 500))
resized_img.show()

# rotate image
rotated_img = img.rotate(90)
rotated_img.show()

# Flip image
filpped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
filpped_img.show()


# copy logo to my original image
logo = Image.open("img01.jpg")
img_copy = img.copy()
position = ((img_copy.width - logo.width), (img_copy.height - logo.height))
img_copy.paste(logo, position)
img_copy.show()

# create thumbnail
thum_size = (128, 128)
thum_img = img.thumbnail(thum_size)
img.show() # note: cannot show thum_img, we should show img

# saved blurred image
blurred_img.save("blurred.png")

# save grayscale image 
grayscale_img.save("grayscale.png")

# save thumbnail
img.save("thumbnail.png")



# Draw rectangle
blank_img = Image.new('RGBA', (400, 300), 'white')
img_draw = ImageDraw.Draw(blank_img)
img_draw.rectangle((70, 50, 270 ,200), outline='red', fill='blue')
img_draw.text((70, 250), "Hello world", fill='green' )
blank_img.save("draw_img.bmp")
blank_img.show()