WWV Simulator
========

![RaspiWWV](/sample.jpg)

Raspberry Pi WWV Simulator

Recreates the WWV Shortwave audio broadcast time signal
without requiring a radio or even Internet access.
This syncronizes the Pi audio to a local Real-Time Clock (RTC)
playing the correct time like WWV.

Hear it in action on [YouTube](https://youtu.be/FzX1HpYpx6E)

Actually, this is a project to help show you how to connect a tiny OLED screen, a Real Time Clock (RTC) and/or an Audio Amplifier all to a single Raspberry Pi Zero!  All with the bonus of being able to listen to WWV time “signals” anytime you wish. 

ACCURACY:
The Pi's clock is set to the RTC so is as accurate as the RTC
module. (Typically, +-1 second or so per day)
For more accuracy, use a higher quality RTC module.

Note that the Pi will automatically recalibrate the RTC
whenever it is connected to the Internet (ethernet or wifi)

Also Note: It can take up to two minutes before audio starts (for syncronization)

INSTRUCTIONS:
[RaspiWWV.pdf](/RaspiWWV.pdf)



Installs the reboot cron and startup file. (This assumes installed to /home/pi on Raspberry.)

Manually run WWV Simulator using:

    $ sh runWWV.sh

