#!/bin/bash

cd /home/pi/RaspiWWV;
python wwv_simulator.py >/dev/null 2>&1
#sudo shutdown --no-wall now

