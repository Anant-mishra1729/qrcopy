import qrcode
import tkinter as tk
import argparse
import os
import json
from utils.pastebin import Pastebin

def upload_to_pastebin(text):
    # Read config file for pastebin api key
    print("Uploading to pastebin...")
    config_file = os.path.expanduser('~/.config/qrcopy/qrcopy.json')
    with open(config_file, 'r') as f:
        config = json.load(f)
    api_key = config['PASTEBIN_API_KEY']
    if api_key == "":
        print('Pastebin API key not found\nPlease add it to the ~/.config/qrcopy/qrcopy.json file')
        exit()
    pastebin = Pastebin(api_key, api_paste_private= '0', api_paste_expire_date= args.expiry, api_paste_format= args.format)
    print('Uploading to pastebin, the url will expire in 1 day')
    url = pastebin.get_url(text, 'QR Code')
    if url.startswith('http'):
        return url
    else:
        print('Error uploading to pastebin')
        print(url)
        exit()

def get_data(args):
    data = ''
    if args.data:
        data = args.data
    elif args.file:
        if os.path.exists(args.file):
            with open(args.file, 'r') as f:
                data = f.read()
        else:
            print('File not found')
            exit()
    else:
        data = tk.Tk().clipboard_get()
        if not data:
            print('No data found in clipboard')
            exit()
    return data

def generate_qr(data):
    print('Generating QR code...')
    try:
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size= 10,
            border= 4
        )
        qr.add_data(data)
        qr.make(fit=True)
        if args.version:
            print('QR Code version: ' + str(qr.version))
        img = qr.make_image(fill_color="black", back_color="white")
    except Exception as e:
        print(e)
        exit()

    # Save the image to a file
    if args.output:
        img.save(args.output)
        root.withdraw()
        print('QR code saved to ' + args.output)

    img.show()


# Adding arguments to the script
parser = argparse.ArgumentParser(description='QR Code Generator')
parser.add_argument('-i', '--data', help='Input text to generate QR code', type= str)
parser.add_argument('-o', '--output', help='Output file name', type= str)
parser.add_argument('-f', '--file', help='Input file name', type= str)
parser.add_argument('-p', '--pastebin', help='Upload to pastebin', action='store_true')
parser.add_argument('-v', '--version', help='Show version', action='store_true')
parser.add_argument('-t', '--format', help='Paste format', type= str, default= 'text')
parser.add_argument('-e', '--expiry', help='Paste expiry date', type= str, default= '1D')
args = parser.parse_args()

root = tk.Tk()
root.withdraw()

data = get_data(args)

if args.pastebin:
    data = upload_to_pastebin(data)
    print("URL: " + data)
    generate_qr(data)
    exit()

# Check if data is too long to be encoded in a QR code
# If it is, upload to pastebin
if len(data) > 2952:
    print('Data too long')
    print("Do you want to upload to pastebin? (y/n)")
    choice = input().lower()
    if choice == 'y':
        data = upload_to_pastebin(data)
        # If data starts with http, it is a url
        if data.startswith('http'):
            print("URL: " + data)
            generate_qr(data)
    else:
        exit()

else:
    generate_qr(data)
