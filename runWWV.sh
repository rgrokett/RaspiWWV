#!/bin/bash

cd /home/pi/RaspiWWV;
python clockOLED.py &
python wwv_simulator.py 
#sudo shutdown --no-wall now

