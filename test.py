import threading
import time
import sys

# This variable will determine when the loading screen should stop
done = False 

def loading_screen():
    global done
    # This is the animation
    while not done:
        for char in ['|', '/', '-', '\\']:
            sys.stdout.write('\rloading ' + char)
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

# Start the loading screen
t = threading.Thread(target=loading_screen)
t.start()

# Here you can put the long process for which you want to display the loading screen
time.sleep(10)  # This is just an example

# Stop the loading screen
done = True
