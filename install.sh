#!/bin/bash

# Create env script and install
env > systemctl/gptbible.env
sudo cp -rfv systemctl/gptbible.env /usr/bin/

# Create run script and install
echo "cd $(pwd)" > systemctl/gptbible.sh
echo "source .env" >> systemctl/gptbible.sh
echo "python main.py" >> systemctl/gptbible.sh
chmod a+x systemctl/gptbible.sh
sudo cp -rfv systemctl/gptbible.sh /usr/bin/

# Installer of system service to linux.
sudo cp -rfv systemctl/gptbible.timer /etc/systemd/system/
sudo cp -rfv systemctl/gptbible.service /etc/systemd/system/

sudo systemctl enable gptbible.timer
#sudo systemctl start gptbible.timer
