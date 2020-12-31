from numpy import interp
from os import listdir
from PIL import Image, ImageStat

# Directory for block textures extracted from version jar
textures = 'assets/minecraft/textures/block'

# Find png filenames in textures directory
filenames = [filename for filename in listdir(textures) if filename.endswith('.png')]

# Convert HSV into hsv(360°, 100%, 100%) color code string
def hsv_string (h, s, v):
    hsv_string = f'hsv({round(h)}, {round(s)}%, {round(v)}%)'
    return (hsv_string)

# Get average HSV color from image
def avg_hsv(filename):
    # Open Minecraft texture as RGBA image
    im = Image.open(f'{textures}/{filename}')

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
    
    # Attach filename name
    return {'filename': filename, 'h': h, 's': s, 'v': v, 'hsv_string': hsv_string(h, s, v)}

colors = map(avg_hsv, filenames)

for color in colors:
    print(f"{color['filename']} : {color['hsv_string']}")