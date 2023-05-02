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
Restart terminal incase ```qrcopy``` command is not working after installation

## Update
```bash
curl https://raw.githubusercontent.com/Anant-mishra1729/qrcopy/main/scripts/update.sh | bash
```

### Usage : Checkout [wiki](https://github.com/Anant-mishra1729/qrcopy/wiki)


## Uninstall
* Find line starting with `alias qrcopy=` and remove that alias from `.bashrc` or `.bash_aliases`.
* Remove directories `~/.config/qrcopy` and `~/.local/qrcopy`

## Todo
* Platform independent (Windows, Mac) (Currently only Linux)
### Contributions are welcome :)
