#!/bin/bash
# Ask user if virtualenv was .env was sourced?
read -p "Did you sourced .env before installation (must have)? (y/n) " -n 1 -r

# Create env script and install
env > systemctl/gptbible.env
sudo cp -rfv systemctl/gptbible.env /usr/bin/

# Create run script and install
echo "cd $(pwd)" > systemctl/gptbible.sh
echo "source .env" >> systemctl/gptbible.sh
echo "python3 main.py" >> systemctl/gptbible.sh
chmod a+x systemctl/gptbible.sh
sudo cp -rfv systemctl/gptbible.sh /usr/bin/

# Installer of system service to linux.
sudo cp -rfv systemctl/gptbible.timer /etc/systemd/system/
sudo cp -rfv systemctl/gptbible.service /etc/systemd/system/

sudo systemctl enable gptbible.timer
#sudo systemctl start gptbible.timer
