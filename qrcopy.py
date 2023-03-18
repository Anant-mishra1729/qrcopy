import qrcode
from PIL import Image 
from tkinter import Tk

data = Tk().clipboard_get()
img = qrcode.make(data)
img.show()
