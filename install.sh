#!/bin/bash

# set the qrcopy directory path
QR_COPY_DIR=~/.local/qrcopy

# create the qrcopy directory if it does not exist
if [ ! -d "$QR_COPY_DIR" ]; then
  mkdir -p "$QR_COPY_DIR"
fi

# download the qrcopy.py file from GitHub using curl
echo -e "\e[1m\e[32mDownloading qrcopy.py...\e[0m"
curl -o "$QR_COPY_DIR/qrcopy.py" https://raw.githubusercontent.com/Anant-mishra1729/qrcopy/main/qrcopy.py

# change directory to the qrcopy directory
cd "$QR_COPY_DIR"

# set the permission for the qrcopy.py script
echo -e "\e[1m\e[32mSetting permissions for qrcopy.py...\e[0m"
chmod +x qrcopy.py

# create a virtual environment named qrcopy using python3-venv
echo -e "\e[1m\e[32mCreating virtual environment for qrcopy...\e[0m"
python3 -m venv qrcopy

# activate the qrcopy virtual environment
echo -e "\e[1m\e[32mActivating virtual environment...\e[0m"
source qrcopy/bin/activate

# install the required packages using pip
echo -e "\e[1m\e[32mInstalling required packages using pip...\e[0m"
pip install qrcode Pillow

# set an alias for qrcopy in the .bashrc or .bash_aliases file
if [ -f ~/.bash_aliases ]; then
  echo -e "\e[1m\e[32mAdding alias to .bash_aliases...\e[0m"
  echo "alias qrcopy='~/.local/qrcopy/qrcopy.py'" >> ~/.bash_aliases
  source ~/.bash_aliases
else
  echo -e "\e[1m\e[32mAdding alias to .bashrc...\e[0m"
  echo "alias qrcopy='~/.local/qrcopy/qrcopy.py'" >> ~/.bashrc
  source ~/.bashrc
fi

echo -e "\e[1m\e[32mDone!\e[0m"
