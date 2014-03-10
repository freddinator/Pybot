## PyBot v.01
import RPi.GPIO as GPIO
import time
import movefunctions


debug = true
	
##main loop

while 1:
    #Go Forward for 1 sec
    forward(1)
		
    #Turn Right 90 degrees
    left(1)
		
    #add more movement here
    break
        
GPIO.cleanup()
