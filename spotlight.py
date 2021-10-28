#https://github.com/krishnasantosh11/WindowsSpotlightImages

"""spotlight.py: This script helps you to get the windows spotlight wallpapers"""

import os
import shutil
from pathlib import Path
try:
    from PIL import Image
except:
    os.system("pip install Pillow")
    from PIL import Image

user_path = os.path.expanduser('~')
drive_letter = user_path[:2]

#this is the source path of windows spotlight images 
dir = f'{user_path}/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/'
despath = f'{drive_letter}/Windows_Spotlight_Images'
portrait = f'{despath}/Portrait'
landscape = f'{despath}/Landscape'
Horizontal = (1920, 1080)
Vertical = (1080, 1920)

if os.path.exists(despath) == False:
    os.mkdir(despath)

if os.path.exists(portrait) == False:
    os.mkdir(portrait)

if os.path.exists(landscape) == False:
    os.mkdir(landscape)

list = os.listdir(dir)   
        
assets = []

for files in list:
    location = os.path.join(dir, files)
    size = os.path.getsize(location)
    if size > 143360:
        assets.append(files)

for f in assets:
    if os.path.exists(despath+'/'+f+'.jpg') == False and os.path.exists(portrait+'/'+f+'.jpg') == False and os.path.exists(landscape+'/'+f+'.jpg') == False:
        shutil.copy(src=dir+f, dst=despath)

def rename(img):
    p = Path(despath+'/'+img)
    p.rename(p.with_suffix('.jpg'))

for f in assets:
    if os.path.exists(despath+'/'+f+'.jpg') == False  and os.path.exists(portrait+'/'+f+'.jpg') == False and os.path.exists(landscape+'/'+f+'.jpg') == False:
        rename(f)
        print(f)

def orientation(pic):
    image = Image.open(pic)
    if image.size == Horizontal:
        return 'landscape'
    elif image.size == Vertical:
        return 'portrait'

list_2 = os.listdir(despath)

for file in list_2:
    if '.jpg' in file:
        if os.path.exists(portrait+'/'+file) == False and os.path.exists(landscape+'/'+file) == False:
            if orientation(despath+'/'+file) == 'landscape':
                shutil.move(despath+'/'+file, landscape)
            elif orientation(despath+'/'+file) == 'portrait':
                shutil.move(despath+'/'+file, portrait)

os.system(f'start {os.path.realpath(despath)}')

print('Done!')
