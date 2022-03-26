import threading
import time

class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting" + self.name)
        threadLock.aquire()
        print_time(self.name, self.delay, 3)
        threadLock.release()

def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (thread_name.threadID, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []
