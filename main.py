from numpy import interp
from os import listdir
from PIL import Image, ImageStat

# Block textures directory extracted from version jar
textures = 'assets/minecraft/textures/block'

# Find png files in textures directory
files = [file for file in listdir(textures) if file.endswith('.png')]

for file in files:
    # Open Minecraft texture as RGBA image
    im = Image.open(f'{textures}/{file}')

    # Convert RGBA image into HSV (Hue, Saturation, Value) image
    im = im.convert('HSV')

    # Split HSV into separate channels
    hue_channel = im.getchannel('H')
    sat_channel = im.getchannel('S')
    val_channel = im.getchannel('V')

    # Get average of each channel
    h = ImageStat.Stat(hue_channel).mean
    s = ImageStat.Stat(sat_channel).mean
    v = ImageStat.Stat(val_channel).mean

    # Scale from 8-bit channel (255, 255, 255) to hsv(360°, 100%, 100%) range
    h = interp(h, [0, 255], [0, 360])[0]
    s = interp(s, [0, 255], [0, 100])[0]
    v = interp(v, [0, 255], [0, 100])[0]

    # Print average HSV of image as hsv() color code
    hsv_string = f'hsv({round(h)}, {round(s)}%, {round(v)}%)'
    print (f'{file} : {hsv_string}')
