from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
buttonPinsos=7
buttonPinheadup =11
vibPin = 13

GPIO.setup( buttonPinsos,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup( buttonPinheadup,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup( vibPin,GPIO.IN)


while True:
    if GPIO.input(buttonPinsos) == False :
        print ("Sos activated")
        sleep(5)
    else:
        print ("No SOS active")
    if GPIO.input(buttonPinheadup) == False :
        print ("Helmet Weared")
        sleep(5)
    else:
        print ("Helmet not weared")
    if GPIO.input(vibPin) == True :
        print ("Vibration Detected")
        sleep(5)
    else:
        print ("No Vibration")

sleep(5)

