#!/bin/bash

# set the qrcopy directory path
QR_COPY_DIR=~/.local/qrcopy

# create the qrcopy directory if it does not exist
if [ ! -d "$QR_COPY_DIR" ]; then
  mkdir -p "$QR_COPY_DIR"
fi

# download the qrcopy.py file from GitHub using curl
curl -o "$QR_COPY_DIR/qrcopy.py" https://raw.githubusercontent.com/Anant-mishra1729/qrcopy/main/qrcopy.py

# change directory to the qrcopy directory
cd "$QR_COPY_DIR"

# set the permission for the qrcopy.py script
chmod +x qrcopy.py

# create a virtual environment named qrcopy using python3-venv
python3 -m venv qrcopy

# activate the qrcopy virtual environment
source qrcopy/bin/activate

# install the required packages using pip
pip install qrcode Pillow

# set an alias for qrcopy in the .bashrc file
echo "alias qrcopy='~/.local/qrcopy/qrcopy.sh'" >> ~/.bashrc

# create a script file to activate the virtual environment and run qrcopy.py
echo "#!/bin/bash" > qrcopy.sh
echo "source $QR_COPY_DIR/qrcopy/bin/activate" >> qrcopy.sh
echo "python $QR_COPY_DIR/qrcopy.py" >> qrcopy.sh

# make the script file executable
chmod +x qrcopy.sh

# source the .bashrc file to apply the changes
source ~/.bashrc
