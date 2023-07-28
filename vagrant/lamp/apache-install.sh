#! /bin/bash

sudo apt-get update -y

if [ $(dpkg-query -W -f='${Status}' apache2 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  sudo apt-get install -y apache2;
  sudo systemctl enable apache2;
  sudo systemctl start apache2;
  sudo systemctl status -l apache2 >> apache2_install.txt;
fi

if [ $(dpkg-query -W -f='${Status}' php 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  sudo apt-get install php libapache2-mod-php php-mysql -y;
fi