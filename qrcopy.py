import qrcode
import tkinter as tk
from tkinter import messagebox
import argparse
import os
# Import threading
import threading

# Adding arguments to the script
parser = argparse.ArgumentParser(description='QR Code Generator')
parser.add_argument('-i', '--data', help='Input text to generate QR code', type= str)
parser.add_argument('-o', '--output', help='Output file name', type= str)
parser.add_argument('-f', '--file', help='Input file name', type= str)
args = parser.parse_args()

root = tk.Tk()
if args.data:
    data = args.data
elif args.file:
    if os.path.exists(args.file):
        with open(args.file, 'r') as f:
            data = f.read()
    else:
        # If the file doesn't exist, use message box to show error
        root.withdraw()
        messagebox.showerror('Error', 'File not found')
        exit()
else:
    data = tk.Tk().clipboard_get()

print(len(data))

# Generate the QR code
if len(data) > 2953:
    print('Data too long')
    exit()

try:
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size= 10,
        border= 4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
except Exception as e:
    print(e)
    exit()

# Save the image to a file
if args.output:
    img.save(args.output)
    root.withdraw()
    messagebox.showinfo('Success', 'QR code saved to ' + args.output)

img.show()
