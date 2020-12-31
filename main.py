from numpy import interp
from os import listdir
from PIL import Image, ImageStat

# Directory for block textures extracted from version jar
textures = 'assets/minecraft/textures/block'

# List of blocks to deny loading
with open('deny_blocks.txt') as reader:
    deny_blocks = reader.read().splitlines()

# Find png filenames in textures directory and extract block ids
block_ids = [filename[:-4] for filename in listdir(textures) if filename.endswith('.png')]

# Remove denied blocks from block id list
block_ids = [id for id in block_ids if not id in deny_blocks]

# Convert HSV into hsv(360°, 100%, 100%) color code string
def hsv_string (h, s, v):
    hsv_string = f'hsv({round(h)}, {round(s)}%, {round(v)}%)'
    return (hsv_string)

# Get average HSV color from image
def avg_hsv(block_id):
    # Open Minecraft texture as RGBA image
    im = Image.open(f'{textures}/{block_id}.png')

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

    # Scale from 8-bit channel range (255, 255, 255) to hsv(360°, 100%, 100%) range
    # These are converted to floats
    h = interp(h, [0, 255], [0, 360])[0]
    s = interp(s, [0, 255], [0, 100])[0]
    v = interp(v, [0, 255], [0, 100])[0]
    
    # Collect this block's data in a dictionary
    return {'block_id': block_id, 'hue': h, 'sat': s, 'val': v, 'hsv_string': hsv_string(h, s, v)}

# Make a list of blocks and their average colors
blocks = map(avg_hsv, block_ids)

# Sort blocks by hue, then saturation, then value
blocks = sorted(blocks, key = lambda block: (block['hue'], block['sat'], block['val']))

# Print blocks and their color
for block in blocks:
    print(f"{block['block_id']} : {block['hsv_string']}")