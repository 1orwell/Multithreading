#from youtube tutorial

#from youtube tutorial
import threading
import time

#creating thread class
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def __del__(self):
        print("Destructor called, thread deleted.")

    # this run method is called by the .start() 
    def run(self):
        print("Starting " + self.name + "\n")
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name + "\n")


# delayig the thread so the other can come in
# printing where each thread is
def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s %s" % (threadName, time.ctime(time.time()), counter) + "\n")
        counter -= 1

# instantiating threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 1.5)

thread1.start()
thread2.start()

#making sure both threads finish before moving onto next line of code.
thread1.join()
thread2.join()

print("Exiting main thread.")
"""
Visual representation of why thread 1 is run twice, between 3 and 4 seconds.

thread 2           5        4        3        2        1
thread 1        5     4     3     2     1
time      0-----1-----2-----3-----4-----5-----6-----7-----8-----9

"""
