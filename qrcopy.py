import qrcode
import pyperclip
import argparse
import os
import json
import requests
import sys

class Pastebin:
    def __init__(self, api_key, api_option='paste', api_paste_private='0', api_paste_expire_date='N', api_paste_format='text'):
        self.api_key = api_key
        self.url = 'https://pastebin.com/api/api_post.php'
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.data = {
            'api_dev_key': self.api_key, # api key
            'api_option': api_option, # Available options: paste, list, login, userdetails, delete, expire etc.
            'api_paste_private': api_paste_private, # 0 = public, 1 = unlisted, 2 = private
            'api_paste_expire_date': api_paste_expire_date, # N = Never, 10M = 10 Minutes, 1H = 1 Hour, 1D = 1 Day, 1W = 1 Week, 2W = 2 Weeks, 1M = 1 Month, 6M = 6 Months, 1Y = 1 Year
            'api_paste_format': api_paste_format # Available formats: text, c, cpp, csharp, css, diff, html4strict, java, javascript, lua, mysql, objectivec, perl, php, python, ruby, vb, xml
        }
    def upload(self, text, title):
        self.data['api_paste_code'] = text
        self.data['api_paste_name'] = title
        r = requests.post(self.url, headers=self.headers, data=self.data)
        return r.text
    
    def get_url(self, text, title):
        return self.upload(text, title)

def upload_to_pastebin(text):
    # Read config file for pastebin api key
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
        data = pyperclip.paste()
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
        print('QR code saved to ' + args.output)

    img.show()

def main():
    data = get_data(args)

    # If stdin is true, read from stdin
    if args.stdin:
        data = sys.stdin.read()

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

if __name__ == '__main__':
    # Adding arguments to the script
    parser = argparse.ArgumentParser(description='QR Code Generator')
    parser.add_argument('-i', '--data', help='Input text to generate QR code', type= str)
    parser.add_argument('-o', '--output', help='Output file name', type= str)
    parser.add_argument('-f', '--file', help='Input file name', type= str)
    parser.add_argument('-p', '--pastebin', help='Upload to pastebin', action='store_true')
    parser.add_argument('-v', '--version', help='Show version', action='store_true')
    parser.add_argument('-t', '--format', help='Paste format', type= str, default= 'text')
    parser.add_argument('-e', '--expiry', help='Paste expiry date', type= str, default= '1D')
    # Adding argument for stdin
    parser.add_argument('-s', '--stdin', help='Read from stdin', action='store_true')
    args = parser.parse_args()
    main()