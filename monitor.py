import pyinotify
import os
from blinkt import set_clear_on_exit, set_all, set_brightness, set_pixel, show

set_all(255,100,0)
show()

class ModHandler(pyinotify.ProcessEvent):
	def process_IN_MODIFY(self, evt):
		set_all(0,128,0)
		show()
		os.system("shutdown now -h")

handler = ModHandler()
wm = pyinotify.WatchManager()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('/root/responder/Responder.db', pyinotify.IN_MODIFY)
notifier.loop()

