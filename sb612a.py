# sb612a　焦電センサの使用テスト
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


SENSOR_GPIO = 18 # GPIO 18 : human detect sensor, pin:12
LED_G_GPIO = 4 # GPIO 4: LED - green, pin:7
LED_R_GPIO = 17 # GPIO 17: LED - red, pin: 11

GPIO.setup(SENSOR_GPIO, GPIO.IN) 
GPIO.setup(LED_G_GPIO, GPIO.OUT) 
GPIO.setup(LED_R_GPIO, GPIO.OUT) 

# initialize
if GPIO.input(SENSOR_GPIO):
  print("sssd")
  GPIO.output(LED_G_GPIO, 1)
else:
  print("hello")
  GPIO.output(LED_R_GPIO, 1)

time.sleep(2)

try:

  while True:
    if GPIO.input(SENSOR_GPIO):
      print("1")
      GPIO.output(LED_G_GPIO, 1)
      GPIO.output(LED_R_GPIO, 0)
    else:
      print("0")
      GPIO.output(LED_G_GPIO, 0)
      GPIO.output(LED_R_GPIO, 1)

    time.sleep(0.1)
  
except KeyboardInterrupt:
  GPIO.cleanup()
