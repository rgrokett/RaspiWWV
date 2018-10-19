#!/bin/sh

# Update the RTC HW clock to Network Time (if avail)
#
# If Pi connects to WiFi then try to update to NTP

X=`ping -c 1 -W 5 8.8.8.8 | grep ' 0% packet loss'`

if [ ! -z "$X" ]
then
	sudo hwclock –w --update-drift
fi

