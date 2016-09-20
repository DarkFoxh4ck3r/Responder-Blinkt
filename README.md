# Responder-Blinkt

## PreReqs:

* Setup Pi Zero following this guide: http://elevatedprompt.com/2016/09/snagging-credentials-from-locked-machines-with-raspberry-pi-zero/
* I used a more updated Responder Repo: https://github.com/lgandx/Responder

* Power off device, and attach Blinkt!
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
