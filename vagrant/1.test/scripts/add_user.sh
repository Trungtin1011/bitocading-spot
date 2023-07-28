#!/bin.sh

USER=$1

useradd -m -s /bin/bash -U $USER -u 666 --group wheel
cp -pr /home/vagrant/.ssh /home/${USER}/.ssh

chown -R ${USER}:${USER} /home/${USER}
echo "%${USER} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/${USER}