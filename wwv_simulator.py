"""
WWV SIMULATOR - Recreates the WWV Shortwave audio broadcast time signal 
	without requiring a radio or even Internet access.
	This syncronizes the Pi audio to a local Real-Time Clock (RTC)
	playing the correct time like WWV.

	ACCURACY:
	The Pi's clock is set to the RTC so is as accurate as the RTC
	module. (Typically, +-1 second or so per day)
	For more accuracy, use a higher quality RTC module.

	Note that the Pi will automatically recalibrate the RTC
	whenever it is connected to the Internet (ethernet or wifi)

"""
# Version 1.0 2018.10.22 
#
# License: GPLv3, see: www.gnu.org/licenses/gpl-3.0.html
#
 

import os, sys
import subprocess
import time
from datetime import datetime
from datetime import timedelta

DEBUG = 0

full_path = os.path.realpath(__file__)
dir = os.path.dirname(full_path)

# Directory like /home/pi/wwv/sounds
snd = dir + '/sounds/'

wwv_file = snd + 'wwv-style-time-signal.wav'
pre_file = snd + 'wwv_at_the_tone.mp3'
post_file= snd + 'wwv_utc.mp3'
hr_file  = snd + 'hour.mp3'
hrs_file = snd + 'hours.mp3'
mn_file  = snd + 'minute.mp3'
mns_file = snd + 'minutes.mp3'

speak_time = snd + 'starting.mp3'
play_flag = 1

if DEBUG:
    print ("Starting...")

# LOOP FOR EACH MINUTE
while 1 :

    # Get current time 
    utc_now = datetime.utcnow()
    
    # ON THE MINUTE, KICK OFF PLAYING WWV TIME AUDIO
    if (utc_now.second == 0 and play_flag == 0):
        if DEBUG :
            print (utc_now.time())

        # Play WWV SOUND in background
        #subprocess.Popen(["aplay","-q",wwv_file]) 
	os.system("aplay -q " + wwv_file + "&")
        play_flag = 1

        # BUILD AUDIO FILENAME STRING FOR THIS MINUTE AND WRITE TO TMP
        # Add one minute
        utc_next = utc_now + timedelta(minutes=1)
        if DEBUG :
            print (utc_next.time())

        # Parse hours and minutes
        hours = utc_next.hour
        minutes = utc_next.minute

        # Build audio filenames 
        hr_snd = snd + str(hours) + '.mp3'
        if hours > 20 :
            digits = list(str(hours))
            hr_snd = snd + digits[0]+'0' + '.mp3' +' '+ snd + digits[1] + '.mp3'

        mn_snd = snd + str(minutes) + '.mp3'
        if minutes > 20 :
            digits = list(str(minutes))
            if minutes == 0 :
                mn_snd = snd + digits[0]+'0' + '.mp3' +' '+ snd 
            else :
                mn_snd = snd + digits[0]+'0' + '.mp3' +' '+ snd + digits[1] + '.mp3'

	# Say HOUR or HOURS
        hours_s = hrs_file
        if hours == 1 :
            hours_s = hr_file 

        mins_s = mns_file
        if minutes == 1 :
            mins_s = mn_file 

        speak_time = pre_file+' ' + hr_snd+' ' + hours_s+' ' + mn_snd+' ' + mins_s+' ' + post_file	

        if DEBUG :
            print (speak_time)

    # AT 45 SECONDS, PLAY TIME STRING AUDIO
    if utc_now.second == 45 :
        #wait_here = subprocess.Popen(["mpg123","-q",speak_time]) 
	os.system("mpg123 -q " + speak_time)
        play_flag = 0
          
    
    time.sleep(0.1)

# END LOOP 


