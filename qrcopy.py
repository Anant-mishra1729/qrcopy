import qrcode
from PIL import ImageTk
import tkinter as tk
import argparse

# Adding arguments to the script
parser = argparse.ArgumentParser(description='QR Code Generator')
parser.add_argument('-i', '--data', help='Input text to generate QR code', type= str)
parser.add_argument('-o', '--output', help='Output file name', type= str)
args = parser.parse_args()

root = tk.Tk()
if args.data:
    data = args.data
else:
    data = root.clipboard_get()

img = qrcode.make(data)

# Save the image to a file
if args.output:
    img.save(args.output)

# Convert the image to a PhotoImage object
img_tk = ImageTk.PhotoImage(img)

# Create a Tkinter window and display the image
label = tk.Label(root, image=img_tk)
label.pack()

# Start the Tkinter event loop
root.mainloop()
