#from lcd1602 import LCD1602_RGB  #LCD1602 RGB grove
from lcd1602 import LCD1602
from machine import I2C,Pin
from time import sleep
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)
#d = LCD1602_RGB.display(i2c, 2, 16)
#d.set_rgb(255, 0, 0)
sleep(1)
 
while True:
    d.home()
    d.print('Hello, World!')
    #d.set_rgb(0, 255, 0)
    sleep(1)
    d.setCursor(0, 1)
    d.print('Hello, Pico!')
    #d.set_rgb(0, 0, 255)
    sleep(1)