# qrcopy
Linux application to share clipboard text to mobile phone using qrcode

## Installation
Clone this repo

``` 
git clone https://github.com/Anant-mishra1729/qrcopy.git 
```

If desired, move qrcopy.py to separate location e.g. ```~/.local/share/qrcopy.py```

Make qrcopy.py executable
```
chmod +x qrcopy.py
```

Create alias to qrcopy in .bashrc or .bash_aliases
```
alias qrcopy='.local/share/qrcopy.py'
```
Replace ```.local/share/qrcopy.py``` with path of qrcopy.py

## Test
* Restart terminal and copy some text
* Run ```qrcopy``` in terminal 
* QR code will be generated, scan it and copy it in your mobile phone.
