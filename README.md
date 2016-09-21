# Responder-Blinkt

## Summary:

* Based on "Snagging creds from locked machines" by Mubix: https://room362.com/post/2016/snagging-creds-from-locked-machines/
* Uses a Raspberry Pi Zero and a Blinkt! LED indicator from Pimoroni.

## PreReqs:

* Setup Pi Zero following this guide: http://elevatedprompt.com/2016/09/snagging-credentials-from-locked-machines-with-raspberry-pi-zero/
* I used a more updated Responder Repo: https://github.com/lgandx/Responder

* Power off device, and attach Blinkt
* Setup Blinkt following this guide: https://github.com/pimoroni/blinkt
* Test to confirm Blinkt is working using the included examples.

* Install pyinotify:
```
pip install pyinotify
```

## Install:

* Copy monitor.py to /root/monitor.py
* Copy the empty Responder.db.bck to /root/Responder/Responder.db
* Edit /etc/rc.local and add before ```Exit 0``` :
```
# Start Monitor
/usr/bin/screen -dmS monitor bash -c 'python /root/monitor.py'
```

## Usage:

* Attach Pi Zero to target device via USB.
* This will automatically shutdown the Pi Zero once the Responder.db has been modified.

## Todo:

* Add shutdown indication using Blinkt
* Add Network Traffic indication using Blinkt? (i.e. like the CPU usage demo)
