#!/bin/bash
#
# Test the Real Time Clock
#
#


echo
echo "Testing RTC..."
echo "RTC:"
sudo hwclock -r
echo "System:"
date
echo
timedatectl status
echo
echo "You should see current RTC Date/Time in UTC"


