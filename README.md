# qrcopy
Linux application to share clipboard text to mobile phone using qrcode

## Installation

* Clone this repo, create separate python environment and install requirements
```bash
cd ~/.local && git clone https://github.com/Anant-mishra1729/qrcopy.git && cd qrcopy && chmod +x qrcopy.py
python3 -m venv qrcopy && source qrcopy/bin/activate 
```

* Install requirements
```sh
pip install qrcode Pillow
```

* Create alias to qrcopy in .bashrc or .bash_aliases

Replace ```.local/qrcopy/qrcopy.py``` with path of qrcopy.py (if qrcopy.py is store elsewhere)
```
alias qrcopy='.local/qrcopy/qrcopy.py'
```

## Test
* Copy some text
* Run ```qrcopy``` in terminal 
* QR code will be generated, scan it and copy it in your mobile phone.

## Todo
* Auto installation script
* Handling large text
* Platform independent software
