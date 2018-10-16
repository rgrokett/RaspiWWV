#!/usr/bin/env python
#
# Uses piOLED 128x32 I2C Display
# https://www.adafruit.com/product/3527
#
# Requires piOLED Library
# https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage
#
# Version 1.0 2018.10.15 - r.grokett Initial
#
# License: GPLv3, see: www.gnu.org/licenses/gpl-3.0.html
#

import time
import datetime
import subprocess

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Screen layout constants
pad = -2
top = pad
bottom = height-pad
x = 0
y = 0

# Load default font.
font = ImageFont.load_default()

cur_date = datetime.datetime.now().strftime('%Y-%m-%d')
cur_time = datetime.datetime.now().strftime('%H:%M:%S')

# Display start message
LINE1 = "RaspiWWV"
LINE2 = "OLED Display Test"
LINE3 = "line 3"
LINE4 = "line 4" 
draw.text((x, top),       LINE1,  font=font, fill=255)
draw.text((x, top+8),     LINE2, font=font, fill=255)
draw.text((x, top+16),     LINE3, font=font, fill=255)
draw.text((x, top+25),     LINE4, font=font, fill=255)
disp.image(image)
disp.display()

