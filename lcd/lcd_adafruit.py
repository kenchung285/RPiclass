import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
from time import sleep

GPIO.setwarnings(False)

lcd = CharLCD(pin_rs=26, pin_rw=19, pin_e=13, pins_data=[6, 5, 11, 9], numbering_mode=GPIO.BCM, cols=16, rows=2, dotsize=8)
lcd.clear()
lcd.write_string("Adafruit CharLCD\r\n  Raspberry Pi")
sleep(1)

for i in range(16):
    lcd.shift_display(1)
    sleep(0.3)
sleep(1)

for i in range(16):
    lcd.shift_display(-1)
    sleep(0.3)
sleep(1)

for i in range(16):
    lcd.shift_display(-1)
    sleep(0.3)
sleep(1)

for i in range(16):
    lcd.shift_display(1)
    sleep(0.3)
sleep(1)
lcd.close(clear=True)
GPIO.cleanup()

