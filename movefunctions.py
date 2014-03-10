##setup GPIO - this has to be done somewhere in the code
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.IN)
GPIO.setwarnings(False)



## Stop code


def stop():
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    return


## check killswitch and print
def killSwitch():
    killswitchstatus = GPIO.input(10)
    if killswitchstatus == 1:
        print("Kill Switch Activated")
    return


## functions - these functions actually make the hardware respond on a GPIO level




def forward(time):
    killSwitch()
    if killswitchstatus != 1:
      GPIO.output(11, GPIO.HIGH)
      GPIO.output(12, GPIO.HIGH)
      GPIO.output(13, GPIO.LOW)
      GPIO.output(16, GPIO.HIGH)
      GPIO.output(18, GPIO.LOW)
      time.sleep(time)
      return
    else:
      break


def reverse(time):
    killSwitch()
    if killswitchstatus != 1:
      GPIO.output(11, GPIO.HIGH)
      GPIO.output(12, GPIO.LOW)
      GPIO.output(13, GPIO.HIGH)
      GPIO.output(16, GPIO.LOW)
      GPIO.output(18, GPIO.HIGH)
      time.sleep(time)
      return
    else:
      break
    
def left(time):
    killSwitch()
    if killswitchstatus !=1:
      GPIO.output(11, GPIO.HIGH)
      GPIO.output(12, GPIO.LOW)
      GPIO.output(13, GPIO.HIGH)
      GPIO.output(16, GPIO.HIGH)
      GPIO.output(18, GPIO.LOW)
      time.sleep(time)
      return
    else:  
      break



def right(time):
    killSwitch()
    if killswitchstatus !=1:
      GPIO.output(11, GPIO.HIGH)
      GPIO.output(12, GPIO.HIGH)
      GPIO.output(13, GPIO.LOW)
      GPIO.output(16, GPIO.LOW)
      GPIO.output(18, GPIO.HIGH)
      time.sleep(time)
      return
    else:
      break
