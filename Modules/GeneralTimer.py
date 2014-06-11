import threading
import time
class MyTimer(threading.Thread):
    timeOpenPortal = 1 * 60
    timeLivePortal = 25
    stop = False

    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        while(not self.stop):
            if self.timeOpenPortal == 0 and self.timeLivePortal == 0:
                self.stop = True
            else:
                time.sleep(1)
                if self.timeOpenPortal == 0:
                    self.timeLivePortal -= 1
                else:
                    self.timeOpenPortal -= 1

    def getTimeOpenPortal(self):
        return self.timeOpenPortal

    def getTimeLivePortal(self):
        return self.timeLivePortal

    def getStrTimeOpenPortal(self):
        if len(str(self.timeOpenPortal % 60)) == 2:
            return "0" + str(self.timeOpenPortal / 60) + ":" + str(self.timeOpenPortal % 60)
        else:
            return "0" + str(self.timeOpenPortal / 60) + ":0" + str(self.timeOpenPortal % 60)

    def getStrTimeLivePortal(self):
        if len(str(self.timeLivePortal % 60)) == 2:
            return "0" + str(self.timeLivePortal / 60) + ":" + str(self.timeLivePortal % 60)
        else:
            return "0" + str(self.timeLivePortal / 60) + ":0" + str(self.timeLivePortal % 60)