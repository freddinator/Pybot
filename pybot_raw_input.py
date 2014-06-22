## PyBot v.01
import RPi.GPIO as GPIO
import time


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
    killswitchstatus = GPIO.input(10)
    if killswitchstatus == 1:
        print("Kill Switch Activated")
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(10, GPIO.LOW)
    key = raw_input()
    ## If you press w, set the motors to forward
    if key == 'w':
        forward()
        print "Moving forward"
        ## and backward	
    elif key == 's':
        reverse()
        print "Reversing"
        ## left
    elif key == 'a':
        left()
        print "Turning left"
    ## right	
    elif key == 'd':
        right()
        print "Turning right"
    ## Z stops all motors
    elif key == 'z':
    	stop()
    	print "Stopping movements"
    ## q quits the program and the loop
    elif key == 'q':
        break
    else:
    	print "That keypress was not recognised!"
GPIO.cleanup()
print "The script was ended."
        
