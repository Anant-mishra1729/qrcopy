# qrcopy
Linux application to share clipboard text to mobile phone using qrcode

## Installation

```bash
curl https://raw.githubusercontent.com/Anant-mishra1729/qrcopy/main/install.sh | bash
```
> Restart terminal incase command is not working

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
> **Note**
```bash
# When both file and input text are used .i.e
qrcopy -i "Hello World" -f hello.txt
# Input text will be shared with QR-Code
```
### Share to pastebin
```bash
# Default format : text; Expiry : 1D
qrcopy -p <FORMAT> <EXPIRY DATE>

qrcopy -p # Clipboard text
qrcopy -i "Hello World" -p # Input text
qrcopy -f <FILE NAME> -p # Input file
```



## Update
```bash
curl https://raw.githubusercontent.com/Anant-mishra1729/qrcopy/main/update.sh | bash

```

## Todo
* Handling large text
* Platform independent (Windows, Mac) (Currently only Linux)
### Contributions are welcome :)
