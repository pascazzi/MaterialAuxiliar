#sonido para repl.it
#for x in range(1,1000):
#   print ('\a')

import time


def beep(interval=0.01, frequency=10):
    for i in range(frequency):
        print("\a\a", end="\r")
        time.sleep(interval)
