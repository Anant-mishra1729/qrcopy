#!/bin/bash

# change directory to ~/.local
cd ~/.local

# clone the qrcopy repository from github
git clone https://github.com/Anant-mishra1729/qrcopy.git

# change directory to the cloned qrcopy directory
cd qrcopy

# set the permission for the qrcopy.py script
chmod +x qrcopy.py

# create a virtual environment named qrcopy using python3-venv
python3 -m venv qrcopy

# activate the qrcopy virtual environment
source qrcopy/bin/activate

# install the required packages using pip
pip install qrcode Pillow

# set an alias for qrcopy in the .bashrc file
echo "alias qrcopy='.local/qrcopy/qrcopy.py'" >> ~/.bashrc

# source the .bashrc file to apply the changes
source ~/.bashrc
