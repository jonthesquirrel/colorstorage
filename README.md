# colorstorage
Color map of all minecraft blocks

## Install Dependencies
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow numpy
```

## Extract Minecraft Assets
1. Pick a Minecraft version, such as `1.16.4`. We will refer to this later as `<version>`
2. Run the game with that version at least once
3. Open the `minecraft` folder. [How to find?](https://help.minecraft.net/hc/en-us/articles/360035131551-Where-are-Minecraft-files-stored-)
4. Go to `versions/<version>/<version>.jar`
5. Open the jar with a zip archive utility
6. Copy the `assets` folder from within that jar to the `colorstorage` folder here

## Run Python Script
Open a terminal in the `colorstorage` directory
```
python3 main.py
```