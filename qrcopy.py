#!/home/{USER_NAME}/miniconda3/envs/{ENVIRONMENT NAME}/bin/python
# Replace "USER NAME" with your user name and "ENVIRONMENT NAME" with your environment name
# OR 
# Type "which python" to get your python executable path replace it with path in first line

import qrcode
from PIL import Image 
from tkinter import Tk

data = Tk().clipboard_get()
img = qrcode.make(data)
img.show()
