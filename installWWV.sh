#!/bin/bash
# Installs WWV Simulator

sudo apt-get update
sudo apt-get install -y mpg123

cp runWWV.sh /home/pi/runWWV.sh

crontab cronfile

