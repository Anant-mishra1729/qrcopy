# qrcopy
Linux application to generate QR code for
* Clipboard text
* Any input text
* Input file

and **Directly share any text to Pastebin with a single command**


## Install

```bash
curl https://raw.githubusercontent.com/Anant-mishra1729/qrcopy/main/scripts/install.sh | bash
```
> Restart terminal incase ```qrcopy``` command is not working after installation

## Update
```bash
curl https://raw.githubusercontent.com/Anant-mishra1729/qrcopy/main/scripts/update.sh | bash
```

## Usage

### Clipboard text (Default)
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

### Save QR-code as image
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
```bash
# Default format : text; Expiry : 1D
qrcopy -p <FORMAT> <EXPIRY DATE>

qrcopy -p # Clipboard text
qrcopy -i "Hello World" -p # Input text
qrcopy -f <FILE NAME> -p # Input file
```
### Using standard input (piping commands) -> ```command | qrcode -s```
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
