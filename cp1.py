#!/usr/bin/python3

import shutil
import os
from PIL import Image
import cv2
x = os.popen('gsettings get org.gnome.desktop.background picture-uri').read().replace("'","").replace("file://","").strip()


if 'jpeg' or 'jpg' in x:
    print('OK')
    
    image = cv2.imread(x)
    cv2.imwrite("static/img.png", image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    

elif 'png' in x:
    shutil.copy(x,'static/img.png')

else:
    None
    

