from numpy import interp
from PIL import Image, ImageColor, ImageStat

# print average HSV of image

im = Image.open('assets/minecraft/textures/block/acacia_planks.png')

stat = ImageStat.Stat(im)

im = im.convert('HSV')
hue_channel = im.getchannel('H')
sat_channel = im.getchannel('S')
val_channel = im.getchannel('V')
h = ImageStat.Stat(hue_channel).mean
s = ImageStat.Stat(sat_channel).mean
v = ImageStat.Stat(val_channel).mean
h = interp(h, [0, 255], [0, 360])[0]
s = interp(s, [0, 255], [0, 100])[0]
v = interp(v, [0, 255], [0, 100])[0]

hsv_string = f'hsv({round(h)}, {round(s)}%, {round(v)}%)'

print (hsv_string)