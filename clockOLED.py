#!/usr/bin/env python
#
# Uses piOLED 128x32 I2C Display
# https://www.adafruit.com/product/3527
#
# Requires piOLED Library
# https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage
#
# Modified from Adafruit examples
#
# Version 1.0 2018.10.15 - r.grokett Initial
# 2018-10-25 added larger font
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

try:
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
  font2 = ImageFont.truetype('fonts/VCR_font.ttf', 16)

  # Display Starting
  LINE1 = "RaspiWWV Simulator"
  LINE2 = " "
  LINE3 = "Starting..."
  draw.text((x, top),       LINE1,  font=font, fill=255)
  draw.text((x, top+8),     LINE2, font=font, fill=255)
  draw.text((x, top+16),     LINE3, font=font2, fill=255)
  disp.image(image)
  disp.display()
  while datetime.datetime.utcnow().second != 0 :
    time.sleep(0.1)	

  while 1 :
    cur_date = datetime.datetime.utcnow().strftime('%Y-%m-%d')
    cur_time = datetime.datetime.utcnow().strftime('%H:%M:%S')

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Display Date/Time
    LINE1 = str(cur_date)
    LINE3 = str(cur_time)+' UTC'
    draw.text((x, top),       LINE1,  font=font, fill=255)
    draw.text((x, top+16),     LINE3, font=font2, fill=255)
    disp.image(image)
    disp.display()

    time.sleep(0.1)

except Exception as e: 
    print(e)
    exit()

