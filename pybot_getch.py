## PyBot v.01
import RPi.GPIO as GPIO
import time

##Setup keypress listener
class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()




##setup GPIO - this has to be done somewhere in the code
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.IN)
GPIO.setwarnings(False)

## check killswitch and print
killswitchstatus = GPIO.input(10)
print(killswitchstatus)

## functions - these functions actually make the hardware respond on a GPIO level

def forward():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    return

def reverse():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    return
    
def left():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    return
	
	
def right():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    return
    
def stop():
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    return
	
##main loop

print "Use the WSAD keys to move, z to stop and q to quit"
while  1:
    key = _Getch()
    ## If you press w, set the motors to forward
    if key == 'w':
        forward();
        print "Forward"
        ## and backward	
        
    if key == 's':
        reverse();
        	
        ## left
    if key == 'a':
        left();
        	
    ## right	
    if key == 'd':
        right();
	
    ## Z stops all motors
    if key == 'z':
    	stop();
        	
    ## q quits the program and the loop
    if key == 'q':
        ## This cleanup routine should be run somewhere to set the pins back
        GPIO.cleanup()
        break
        
