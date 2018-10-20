#!/bin/bash
# Install shutdown button to Raspiberry Pi
# 
# Can be safely run multiple times
#
# version 20171203
#
 


# VERIFY BUTTONS ARE INSTALLED
# Move the on/off button to top row
X=`grep rpi_power_switch /etc/modules`

if [ -z "$X" ];
then
        sudo bash -c "cp -p /etc/modules /etc/modules.BAK"
        sudo bash -c "echo 'rpi_power_switch' >> /etc/modules"
	echo "Added power button to /etc/modules"
else
	echo "Found power button OK"
fi
	
X=`grep "rpi_power_switch" /etc/modprobe.d/adafruit.conf`
Y=`grep "17" /etc/modprobe.d/adafruit.conf`
if [ -z "$X" ]; then
        sudo bash -c "cp -p /etc/modprobe.d/adafruit.conf /etc/modprobe.d/adafruit.conf.BAK"
        sudo bash -c "echo 'options rpi_power_switch gpio_pin=17 mode=0' > /etc/modprobe.d/adafruit.conf"
	echo "Added rpi_power_switch to /etc/modprobe.d/adafruit.conf"
elif [ -z "$Y" ]; then
        sudo bash -c "echo 'options rpi_power_switch gpio_pin=17 mode=0' > /etc/modprobe.d/adafruit.conf"
	echo "Added rpi_power_switch to /etc/modprobe.d/adafruit.conf"
else
	echo "Found power button is assigned OK"
fi 

echo
echo "Finished"
echo
