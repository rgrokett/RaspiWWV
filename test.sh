#!/bin/bash
#
# Test the RTC, OLED and Audio
#
#


echo "Testing OLED DISPLAY...."
python ./testOLED.py
echo "You should see a test message displayed"
sleep 2

echo
echo "Testing RTC..."
sudo hwclock -r
timedatectl status
echo
echo "You should see current RTC Date/Time in UTC"
sleep 2

echo "Testing Audio..."
sudo amixer sset PCM,0 95%
aplay /usr/share/sounds/alsa/Front_Center.wav
mpg123 sounds/wwv_at_the_tone.mp3
echo
echo "You should have heard audio"
echo
sleep 2

