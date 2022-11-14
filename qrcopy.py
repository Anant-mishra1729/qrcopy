#!/home/rk/miniconda3/envs/temp/bin/python
# Replace "temp" with your environment name 
# OR 
# Type "which python" to get your python executable path replace it with path in first line

import qrcode
from PIL import Image 
from tkinter import Tk

data = Tk().clipboard_get()
img = qrcode.make(data)
img.show()
