from PIL import Image, ImageDraw, ImageFont

image = Image.open('taco.jpg')
bigger = image.resize((333, 500))
img_draw = ImageDraw.Draw(bigger)
font = ImageFont.truetype('DejaVuSans.ttf', 25)
img_draw.text([20, 0], 'Random Taco Cookbook', fill='purple', font=font)
bigger.save('resizedTaco.jpg')