#!/bin/bash

# set the qrcopy directory path
QR_COPY_DIR=~/.local/qrcopy
CONFIG_DIR=~/.config/qrcopy

# create the qrcopy directory if it does not exist
if [ ! -d "$QR_COPY_DIR" ]; then
  mkdir -p "$QR_COPY_DIR"
fi

# create a virtual environment named qrcopy using python3-venv
echo -e "\e[1m\e[32mCreating virtual environment for qrcopy...\n\e[0m"
python3 -m venv "$QR_COPY_DIR/qrcopy"

# Check if the virtual environment is created successfully
if [ ! -d "$QR_COPY_DIR/qrcopy" ]; then
  echo -e "\e[1m\e[31mError: Failed to create virtual environment for qrcopy.\e[0m\n Check if python3-venv is installed."
  exit 1
fi

# activate the qrcopy virtual environment
echo -e "\e[1m\e[32mActivating virtual environment...\n\e[0m"
source "$QR_COPY_DIR/qrcopy/bin/activate"


# download the qrcopy.py file from GitHub using curl
echo -e "\e[1m\e[32mDownloading qrcopy.py...\n\e[0m"
curl -o "$QR_COPY_DIR/qrcopy.py" https://raw.githubusercontent.com/Anant-mishra1729/qrcopy/main/qrcopy.py

# create the qrcopy.sh file
echo -e "\e[1m\e[32mCreating qrcopy.sh file...\n\e[0m"

cat << EOF > "$QR_COPY_DIR/qrcopy.sh"
#!/bin/bash
source $QR_COPY_DIR/qrcopy/bin/activate
python $QR_COPY_DIR/qrcopy.py "\$@"
EOF

# set the permission for the qrcopy.py and qrcopy.sh script
echo -e "\e[1m\e[32mSetting permissions for scripts...\n\e[0m"
chmod +x "$QR_COPY_DIR/qrcopy.py"
chmod +x "$QR_COPY_DIR/qrcopy.sh"


# install the required packages using pip
echo -e "\e[1m\e[32mInstalling required packages using pip...\n\e[0m"
pip install qrcode Pillow pyperclip requests

echo -e "\e[1m\e[36mEnter your Pastebin API key in ~/.config/qrcopy/qrcopy.conf (You can get it from pastebin.com) \e[0m"

# set an alias for qrcopy in the .bashrc or .bash_aliases file
if [ -f ~/.bash_aliases ]; then
  echo -e "\e[1m\e[32mAdding alias to .bash_aliases...\n\e[0m"
  echo "alias qrcopy='$QR_COPY_DIR/qrcopy.sh'" >> ~/.bash_aliases
else
  echo -e "\e[1m\e[32mAdding alias to .bashrc...\n\e[0m"
  echo "alias qrcopy='$QR_COPY_DIR/qrcopy.sh'" >> ~/.bashrc
fi

# create the CONFIG_DIR directory if it does not exist
if [ ! -d "$CONFIG_DIR" ]; then
  mkdir -p "$CONFIG_DIR"
fi

# Config file to store installation details
echo -e "\e[1m\e[32mCreating config file...\n\e[0m"
cat > "$CONFIG_DIR/qrcopy.json" << EOF
{
  "QRCOPY_DIR": "$QR_COPY_DIR",
  "VENV_DIR": "$QR_COPY_DIR/qrcopy",
  "PASTEBIN_API_KEY": "",
  "PASTEBIN_USER_API_KEY": ""
}
EOF


echo -e "\e[1m\e[32mDone!\e[0m"
