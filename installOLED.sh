#!/bin/sh
# ADAFRUIT OLED INSTALL
#
# Note: it is OK to run this script multiple times.
#
# https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage
#

# Install Deps
sudo apt-get update
sudo apt-get install -y build-essential python-dev python-pip
sudo pip install -y RPi.GPIO
sudo apt-get install -y python-imaging python-smbus

# Install Libs
sudo apt-get install git
cd
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306
sudo python setup.py install

# Test
cd 
cd RaspiWWV
python testOLED.py

echo
echo "Finished"
echo

