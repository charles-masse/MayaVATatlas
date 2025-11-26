
from PIL import Image
import random

def generateTexture(width=512, height=512):

    img = Image.new('RGB', (width, height))

    pixels = []
    for p in range(width * height):
        pixels.append(tuple(map(lambda x: int(x * 256), (random.random(), random.random(), random.random()))))

    img.putdata(pixels)

    return img

generateTexture().save('D:/Desktop/Scripts/portfolio/public/textures/animations.png')