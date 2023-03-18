#!/bin/bash

# set the qrcopy directory path
QR_COPY_DIR=~/.local/qrcopy

# create the qrcopy directory if it does not exist
if [ ! -d "$QR_COPY_DIR" ]; then
  mkdir -p "$QR_COPY_DIR"
fi

# download the qrcopy.py file from GitHub using curl
curl -o "$QR_COPY_DIR/qrcopy.py" https://raw.githubusercontent.com/Anant-mishra1729/qrcopy/main/qrcopy.py

# create the qrcopy.sh script
cat > "$QR_COPY_DIR/qrcopy.sh" <<EOF
#!/bin/bash
source $QR_COPY_DIR/bin/activate
python3 $QR_COPY_DIR/qrcopy.py
EOF

# set the permission for the qrcopy.sh script
chmod +x "$QR_COPY_DIR/qrcopy.sh"

# create a virtual environment named qrcopy using python3-venv
python3 -m venv "$QR_COPY_DIR"

# activate the qrcopy virtual environment
source "$QR_COPY_DIR/bin/activate"

# install the required packages using pip
pip install qrcode Pillow

# check if ~/.bash_aliases exists, if it does, add the alias to it, else add it to ~/.bashrc
if [ -f ~/.bash_aliases ]; then
  echo "alias qrcopy='~/.local/qrcopy/qrcopy.sh'" >> ~/.bash_aliases
else
  echo "alias qrcopy='~/.local/qrcopy/qrcopy.sh'" >> ~/.bashrc
fi

# source the .bashrc file to apply the changes
source ~/.bashrc
