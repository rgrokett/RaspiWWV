#!/bin/bash

cd /home/pi/RaspiWWV;
sudo updateRTCtoNTP.sh

python clockOLED.py &
python wwv_simulator.py 
#sudo shutdown --no-wall now

