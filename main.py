from numpy import interp
from PIL import Image, ImageStat

# Open Minecraft texture as RGBA image
im = Image.open('assets/minecraft/textures/block/acacia_log.png')

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
print (hsv_string)