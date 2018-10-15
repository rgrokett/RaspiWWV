WWV Simulator
========

![RaspiWWV](/sample.jpg)

Raspberry Pi WWV Simulator

Recreates the WWV Shortwave audio broadcast time signal
without requiring a radio or even Internet access.
This syncronizes the Pi audio to a local Real-Time Clock (RTC)
playing the correct time like WWV.

ACCURACY:
The Pi's clock is set to the RTC so is as accurate as the RTC
module. (Typically, +-1 second or so per day)
For more accuracy, use a higher quality RTC module.

Note that the Pi will automatically recalibrate the RTC
whenever it is connected to the Internet (ethernet or wifi)

Original from:
https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi/overview


Install:
    $ cd /home/pi
    $ git clone https://github.com/rgrokett/RaspiWWV.git
    $ cd RaspiWWV
    $ bash installWWV.sh

Installs the reboot cron and startup file. (This assumes installed to /home/pi on Raspberry.)

Manually run WWV Simulator using:

    $ python wwv_simulator.py

