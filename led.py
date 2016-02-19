from time import sleep
import subprocess
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)

try:
    while 1:
            GPIO.output(8,GPIO.HIGH)
            print "LED GOES ON"
            sleep(0.1)
            GPIO.output(8,GPIO.LOW)
            print "LED GOES OFF"
            sleep(0.5)

except KeyboardInterrupt:

    GPIO.cleanup()