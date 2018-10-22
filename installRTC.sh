#!/bin/bash
# Installs RTC


echo "Installing Real Time Clock (RTC)..."

echo "Select which module you have:"
echo "1 - pcf8523"
echo "2 - ds1307"
echo "3 - ds3231"
read -p '[1]: ' ANS
case "$ANS" in
        1)
            RTC='pcf8523'
            ;;
         
        2)
            RTC='ds1307'
            ;;

        3)
            RTC='ds3231'
            ;;

	*)
            RTC='pcf8523'
	    ;;
esac

# IF RTC ALREADY INSTALLED, REPLACE SOFTWARE CLOCK WITH RTC
Y=`grep $RTC /boot/config.txt`
if [ ! -z "$Y" ];
then
	echo "Disabling old software clock..."
    sudo apt-get update
	sudo apt-get -y remove fake-hwclock
	sudo update-rc.d -f fake-hwclock remove
	sudo systemctl disable fake-hwclock
	sudo mv /run/systemd/system /run/systemd/system.BAK
	sleep 1

	echo "Setting time in RTC..."
	sudo hwclock -w --update-drift   
	sleep 1

	echo "Displaying system & RTC times:"
	timedatectl status
	sleep 1
	echo
	exit
fi

# ADD RTC module
STR="dtoverlay=i2c-rtc,$RTC"
X=`grep i2c-rtc /boot/config.txt`
if [ -z "$X" ];
then
	# insert module
	echo "Adding $RTC to /boot/config.txt"
	echo
        sudo bash -c "echo $STR >> /boot/config.txt"
else
	# update module
	echo "Updating /boot/config.txt for $RTC"
	echo
	sudo bash -c "sed -i '/dtoverlay=i2c-rtc/ c\'$STR /boot/config.txt"
fi

# Install Deps if needed
sudo apt-get update
sudo apt-get install -y build-essential python-dev python-pip
sudo pip install RPi.GPIO
sudo apt-get install -y python-imaging python-smbus


echo
echo "Now reboot your Pi"
echo

