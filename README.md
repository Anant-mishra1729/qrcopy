# qrcopy
Linux application to share clipboard text to mobile phone using qrcode

## Installation

```bash
curl https://raw.githubusercontent.com/Anant-mishra1729/qrcopy/main/install.sh | bash
```

## Usage
#### Only clipboard text

```bash
qrcopy
```

#### For some input text
```bash
qrcopy -i "Hello World"
```

#### Save qrcode to file
```shell
qrcopy -o qrcode.png # Save qrcode of clipboard text to qrcode.png
qrcopy -i "Hello World" -o qrcode.png # Save qrcode of "Hello World" to qrcode.png
```

## Update
```bash
curl https://raw.githubusercontent.com/Anant-mishra1729/qrcopy/main/update.sh | bash

```

## Todo
* Handling large text
* Platform independent (Windows, Mac) (Currently only Linux)
### Contributions are welcome :)
