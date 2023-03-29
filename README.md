# qrcopy
Qrcopy is a Linux application that generates QR codes for clipboard text, any input text, and input files and share text on pastebin.com.
It also supports standard input or piping of commands, allowing you to generate QR codes for the output of any command that can be piped to it.

<ol>
  <li><a href="#install">Install</a></li>
  <li><a href="#updating">Updating</a></li>
  <li><a href="#usage">Usage</a></li>
  <ul>
    <li><a href="#clipboard-text">Clipboard (Default) 📋</a></li>
    <li><a href="#input-text">Input text</a></li>
    <li><a href="#save-qr-as-image">Save QR code as image</a></li>
    <li><a href="#upload-to-pastebin">Upload to pastebin</a></li>
    <li><a href="#with-other-commands">With other commands</a></li>
  </ul>
  <li><a href="#todo">Todo</a></li>
</ol>




## Install

```bash
curl https://raw.githubusercontent.com/Anant-mishra1729/qrcopy/main/scripts/install.sh | bash
```
> Restart terminal incase ```qrcopy``` command is not working after installation

## Updating
```bash
curl https://raw.githubusercontent.com/Anant-mishra1729/qrcopy/main/scripts/update.sh | bash
```

## Usage

### Clipboard text
```bash
qrcopy
```
### Input text
```bash 
qrcopy -i "Hello World"
```
### Input file
```bash
qrcopy -f <FILE NAME>
```

### Save QR as image
```bash
qrcopy -o "qrcode.png"
```
> **Warning**
```bash
# When both file and input text are used .i.e
qrcopy -i "Hello World" -f hello.txt
# Input text will be shared with QR-Code
```

> **Note**

To use Pastebin insert you **Pastebin API Key** in ```~/.config/qrcopy/qrcopy.json``` -> ```PASTEBIN_API_KEY```

### Upload to pastebin
#### For EXPIRY DATE vaild values are
* N = Never
* 10M = 10 Minutes
* 1H = 1 Hour
* 1D = 1 Day
* 1W = 1 Week
* 2W = 2 Weeks
* 1M = 1 Month
* 6M = 6 Months
* 1Y = 1 Year
#### Visit [here](https://pastebin.com/doc_api#:~:text=down%20the%20page.-,Creating%20A%20New%20Paste%2C%20The%20%27api_paste_format%27%20Parameter%20In%20Detail,-We%20have%20over) for the available 200 formats
```bash
# Default format : text; Expiry : 1D
qrcopy -p <FORMAT> <EXPIRY DATE>

qrcopy -p # Clipboard text
qrcopy -i "Hello World" -p # Input text
qrcopy -f <FILE NAME> -p # Input file
```


### With other commands
#### Format : ```command | qrcopy -s```
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


## Todo
* Platform independent (Windows, Mac) (Currently only Linux)
### Contributions are welcome :)
