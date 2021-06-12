#https://github.com/krishnasantosh11/WindowsSpotlightImages

import os
from pathlib import Path
import shutil

#default user path and drive letter
userPath = os.path.expanduser('~')
driveletter = userPath[:2]

#this is the source path of windows spotlight images 
dir = f'{userPath}/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/'

#creating a new folder, or if the folder already exists using the folder's path as destination 
despath = f'{driveletter}/Windows_Spotlight_Images'
if os.path.exists(despath):
    des = despath
    print(f"Folder exists at ({des})")
else:
    os.mkdir(despath)
    des = despath
    print(f'Folder Created at ({des})')

#creating a new list to store the files in our windows spotlight folder 
list = os.listdir(dir)   
        
#creating an empty list to append our desired images
assets = []

#appending images that are above the size of 140kb
for files in list:
    location = os.path.join(dir, files)
    size = os.path.getsize(location)
    if size > 143360:
        assets.append(files)

#copying the files from assets to our destination folder
for f in assets:
    if os.path.exists(des+'/'+f+'.jpg') == False:
        shutil.copy(src=dir+f, dst=des)

#this function renames the files in the destination, i.e converting file type to .jpg
def rename(img):
    p = Path(des+'/'+img)
    p.rename(p.with_suffix('.jpg'))

#using a for loop and calling the funciton for each individual file
for i in range(0,len(assets)):
    if os.path.exists(des+'/'+assets[i]+'.jpg') == False:
        rename(assets[i])
        print(assets[i])

#displaying the folder
os.system(f'start {os.path.realpath(des)}')

print('Done!')
