import qrcode
import pyperclip
import argparse
import os
import json
import requests
import sys


class Pastebin:
    """
    Pastebin API wrapper
    api_key: Pastebin API key
    api_option: Available options: paste, list, login, userdetails, delete, expire etc.
    api_paste_private: 0 = public, 1 = unlisted, 2 = private
    api_paste_expire_date: N = Never, 10M = 10 Minutes, 1H = 1 Hour, 1D = 1 Day, 1W = 1 Week, 2W = 2 Weeks, 1M = 1 Month, 6M = 6 Months, 1Y = 1 Year
    api_paste_format: Available formats: text, c, cpp, csharp, css, diff, html4strict, java, javascript, lua, mysql, objectivec, perl, php, python, ruby, vb, xml etc.
    """

    def __init__(
        self,
        api_key,
        api_option="paste",
        api_paste_private="0",
        api_paste_expire_date="N",
        api_paste_format="text",
    ):
        self.api_key = api_key
        self.url = "https://pastebin.com/api/api_post.php"
        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}
        self.data = {
            "api_dev_key": self.api_key,
            "api_option": api_option,
            "api_paste_private": api_paste_private,
            "api_paste_expire_date": api_paste_expire_date,
            "api_paste_format": api_paste_format,
        }

    def upload(self, text, title):
        """
        Upload text to pastebin
        text: text to upload
        title: title of the paste
        """
        self.data["api_paste_code"] = text
        self.data["api_paste_name"] = title
        r = requests.post(self.url, headers=self.headers, data=self.data)
        return r.text


def upload_to_pastebin(text):
    """
    Upload text to pastebin
    text: text to upload
    """
    # Read config file for pastebin api key
    config_file = os.path.expanduser("~/.config/qrcopy/qrcopy.json")
    with open(config_file, "r") as f:
        config = json.load(f)
    if args.paste_mode == "2":
        api_key = config["PASTEBIN_USER_API_KEY"]
    else:
        api_key = config["PASTEBIN_API_KEY"]
    if api_key == "":
        print(
            "Pastebin API key not found\nPlease add it to the ~/.config/qrcopy/qrcopy.json file"
        )
        exit()

    # Initialize pastebin object
    pastebin = Pastebin(
        api_key,
        api_paste_private=args.paste_mode,
        api_paste_expire_date=args.expiry,
        api_paste_format=args.format,
    )

    # Upload to pastebin
    print("Uploading to pastebin, the url will expire in " + args.expiry + "...")
    url = pastebin.upload(text, "QR Code")

    if url.startswith("http"):
        return url
    else:
        print("Error uploading to pastebin")
        print(url)
        exit()


# Get data from clipboard, file or stdin
def get_data(args):
    """
    Get data from clipboard, file or stdin
    args: command line arguments
    """
    data = ""

    # Get data from stdin
    if args.stdin:
        data = sys.stdin.read()

    # Get data from input text
    elif args.input_data:
        data = args.input_data

    # Get data from file
    elif args.file:
        if os.path.exists(args.file):
            with open(args.file, "r") as f:
                data = f.read()
        else:
            print("File not found")
            exit()

    # Clipboard
    else:
        data = pyperclip.paste()
        if not data:
            print("No data found in clipboard")
            exit()
    return data


# Generate QR code
def generate_qr(data):
    """
    Generate QR code
    data: data to encode in QR code
    """
    print("Generating QR code for\n" + data[:30] + "...")
    try:
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4
        )
        qr.add_data(data)
        qr.make(fit=True)
        if args.version:
            print("QR Code version: " + str(qr.version))
        img = qr.make_image(fill_color="black", back_color="white")
    except Exception as e:
        print(e)
        exit()

    # Save the image to a file
    if args.output:
        img.save(args.output)
        print("QR code saved to " + args.output)

    img.show()


# Main function
def main():
    data = get_data(args)

    # Upload to pastebin
    if args.pastebin:
        url_ = upload_to_pastebin(data)
        print("URL: " + url_)
        generate_qr(url_)
        exit()

    # Check if data is too long to be encoded in a QR code (2953 characters) and ask user to upload to pastebin
    if len(data) > 2952:
        if not args.stdin:
            print("Data is too long\nDo you want to upload to pastebin? (y/n)")
            choice = input().lower()
            if choice == "y":
                url = upload_to_pastebin(data)
                generate_qr(url)
            else:
                exit()
        else:
            print(
                "Data is too long to be encoded in a QR code\n Use -p or --pastebin to upload to pastebin"
            )
    else:
        # Data is not too long, generate QR code
        generate_qr(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="QR Code Generator")
    parser.add_argument(
        "-v", "--version", help="Show generated QR code version", action="store_true"
    )

    parser.add_argument(
        "-i", "--input_data", help="Input text to generate QR code", type=str
    )

    parser.add_argument("-f", "--file", help="Input file path", type=str)

    parser.add_argument("-o", "--output", help="Output file path", type=str)

    parser.add_argument(
        "-p",
        "--pastebin",
        help="Upload to pastebin (API key required in ~/.config/qrcopy/qrcopy.json)",
        action="store_true",
    )

    parser.add_argument(
        "-pf",
        "--format",
        help="Paste format (text, c, cpp etc.)",
        type=str,
        default="text",
    )

    parser.add_argument(
        "-pe", "--expiry", help="Paste expiry date", type=str, default="1D"
    )

    parser.add_argument(
        "-pm",
        "--paste_mode",
        help="Paste mode (public = 0, unlisted = 1, private = 2)",
        type=str,
        default="0",
    )

    # Get data from stdin, thanks to @vmath3us for the suggestion
    parser.add_argument("-s", "--stdin", help="Read from stdin", action="store_true")
    args = parser.parse_args()
    main()
