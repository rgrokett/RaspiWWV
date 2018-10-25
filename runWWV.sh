#!/bin/bash

cd /home/pi/RaspiWWV;
sudo sh updateRTCtoNTP.sh

python clockOLED.py &
python wwv_simulator.py 
#sudo shutdown --no-wall now

