# qrcopy
Linux application to share clipboard text to mobile phone using qrcode

## Installation
* Clone this repo
``` 
git clone https://github.com/Anant-mishra1729/qrcopy.git 
```

* Create python environment and install requirements
```
mkdir ~/.local/qrcopy/
cd ~/.local/qrcopy
python3 -m venv qrcopy
pip install qrcode
pip install Pillow
```

* Make qrcopy.py executable
```
chmod +x qrcopy.py
```

* Create alias to qrcopy in .bashrc or .bash_aliases
```
alias qrcopy='.local/qrcopy/qrcopy.py'
```
Replace ```.local/share/qrcopy.py``` with path of qrcopy.py (if qrcopy is store elsewhere)

## Test
* Copy some text
* Run ```qrcopy``` in terminal 
* QR code will be generated, scan it and copy it in your mobile phone.

## Todo
* Auto installation script
* Handling large text
* Platform independent software
