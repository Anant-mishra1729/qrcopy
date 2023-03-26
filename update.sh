#!/bin/bash

# set the qrcopy directory path
QR_COPY_DIR=~/.local/qrcopy

# download the latest qrcopy.py file from GitHub using curl
echo -e "\e[1m\e[32mDownloading the latest qrcopy.py...\e[0m"
curl -o "$QR_COPY_DIR/qrcopy_new.py" https://raw.githubusercontent.com/Anant-mishra1729/qrcopy/main/qrcopy.py

# compare the checksum of the new file with the current file
if [[ $(sha256sum "$QR_COPY_DIR/qrcopy_new.py" | cut -d " " -f 1) == $(sha256sum "$QR_COPY_DIR/qrcopy.py" | cut -d " " -f 1) ]]; then
  echo -e "\e[1m\e[32mqrcopy.py is already up to date\e[0m"
  rm "$QR_COPY_DIR/qrcopy_new.py"
  exit 0
fi

# backup the current qrcopy.py file
echo -e "\e[1m\e[32mBacking up the current qrcopy.py...\e[0m"
mv "$QR_COPY_DIR/qrcopy.py" "$QR_COPY_DIR/qrcopy_old.py"

# rename the new file to qrcopy.py
echo -e "\e[1m\e[32mRenaming the new qrcopy.py...\e[0m"
mv "$QR_COPY_DIR/qrcopy_new.py" "$QR_COPY_DIR/qrcopy.py"

# set the permission for the qrcopy.py script
echo -e "\e[1m\e[32mSetting permissions for qrcopy.py...\e[0m"
chmod +x "$QR_COPY_DIR/qrcopy.py"

echo -e "\e[1m\e[32mDone!\e[0m"
