import time
import RPi.GPIO as GPIO

CONTROL_PIN = 17
PWM_FREQ = 50
STEP=15

GPIO.setmode(GPIO.BCM)
GPIO.setup(CONTROL_PIN, GPIO.OUT)

pwm = GPIO.PWM(CONTROL_PIN, PWM_FREQ)
pwm.start(0)

def angle_to_duty_cycle(angle=0):
    duty_cycle = ( 5 * (180 - angle) + 10 * (angle) ) / 180
    return duty_cycle

def switch2deg(deg):
    dc = angle_to_duty_cycle(deg)
    pwm.ChangeDutyCycle(dc)

print("start servo.")
switch2deg(0)
time.sleep(1)

degrees = [45, 90, 135, 180, 135, 90, 45, 0]

for i in range(5):
    for deg in degrees:
        switch2deg(deg)
        time.sleep(0.5)

pwm.stop()
GPIO.cleanup()
