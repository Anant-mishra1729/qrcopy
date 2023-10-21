# qrcopy
Qrcopy is a Linux application that generates QR codes for clipboard text, any input text, and input files and share text on pastebin.com.
It also supports standard input or piping of commands, allowing you to generate QR codes for the output of any command that can be piped to it.


## 🛑 Prerequisites 🛑

* Install `python3-venv` (`python3.10-venv` if python3-venv is not working).
* For clipboard functionality install anyone of these `xsel` or `xclip` (checkout [here](https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error:~:text=after%205%20seconds.-,Not%20Implemented%20Error,-You%20may%20get)), otherwise you may get this error *Pyperclip could not find a copy/paste mechanism for your system.*

## Install

```bash
curl https://raw.githubusercontent.com/Anant-mishra1729/qrcopy/main/scripts/install.sh | bash
```
Restart terminal after installation


## Update
```bash
curl https://raw.githubusercontent.com/Anant-mishra1729/qrcopy/main/scripts/update.sh | bash
```

## How to use it?
### Normal usage
* **Clipboard (copied text)**
```bash
qrcopy
```
* **For any input text**
```bash 
qrcopy -i "Hello World"
```
* **For any input file**
```bash
qrcopy -f <FILE NAME>
```

* **Save generated QR as an image file**
```bash
qrcopy -o "qrcode.png"
```

> **Note**
```bash
# When both file and input text are used .i.e
qrcopy -i "Hello World" -f hello.txt
# Input text will be shared with QR-Code
```

### Upload to pastebin

To use Pastebin insert you **Pastebin API Key** in ```~/.config/qrcopy/qrcopy.json``` -> ```PASTEBIN_API_KEY```

**For EXPIRY DATE valid values are**

* N = Never
* 10M = 10 Minutes
* 1H = 1 Hour
* 1D = 1 Day
* 1W = 1 Week
* 2W = 2 Weeks
* 1M = 1 Month
* 6M = 6 Months
* 1Y = 1 Year

**Visit [here](https://pastebin.com/doc_api#:~:text=down%20the%20page.-,Creating%20A%20New%20Paste%2C%20The%20%27api_paste_format%27%20Parameter%20In%20Detail,-We%20have%20over) for the available 200 formats**

```bash
# Default format : text; Expiry : 1D
qrcopy -p <FORMAT> <EXPIRY DATE>

qrcopy -p # Uploading copied text to Pastebin
qrcopy -i "Hello World" -p # Uploading input text to Pastebin
qrcopy -f hello.txt -p # Uploading file to Pastebin

## Uploading with parameters
qrcopy -f hello.html -pf html5 -p # Upload hello.html with HTML5 syntax highlighting
qrcopy -f hello.html -pf html5 -pe 1W -p # Upload hello.html with HTML5 syntax highlighting, expired in 1 week
```


### With other commands
Format : **`command | qrcopy -s`**
```bash
# Generating qrcode for output of cat command
cat file | qrcopy -s 

# Generating qrcode for url of file uploaded at 0x0.st file sharing service
command | curl -F 'file=@-' 0x0.st | qrcopy -s 

# Upload log of strace command to 0x0.st and generate qrcode for the url
strace command | curl -F 'file=@-' 0x0.st | qrcopy -s 

# Upload image to 0x0.st and generate qrcode of the url
curl -F'file=@yourfile.png' 0x0.st | qrcopy -s
```


## Uninstall
* Find line starting with `alias qrcopy=` and remove that alias from `.bashrc` or `.bash_aliases`.
* Remove directories `~/.config/qrcopy` and `~/.local/qrcopy`

## Todo
* Platform independent (Windows, Mac) (Currently only Linux)
### Contributions are welcome :)
