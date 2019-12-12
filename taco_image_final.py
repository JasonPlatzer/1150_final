'''This program will take a jpeg and resize it and then write random taco cookbook on it'''
from PIL import Image, ImageDraw, ImageFont   #importing what I need to be able to do what I want with picture

image = Image.open('taco.jpg')   #making it so that i can change the picture of taco.jpg
bigger = image.resize((233, 350))   #creating a resized version of taco.jpg
img_draw = ImageDraw.Draw(bigger)   #creating a version of bigger that I can draw on
font = ImageFont.truetype('DejaVuSans.ttf', 15)   #creating a variable for the font I want to write with
img_draw.text([20, 0], 'Random Taco Cookbook', fill='purple', font=font)    #writing random taco cookbool in purple with the font I put in the variable
bigger.save('resizedTaco.jpg')   #saving the version of taco.jpg I altered