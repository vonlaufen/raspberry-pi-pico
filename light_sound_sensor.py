#from lcd1602 import LCD1602_RGB  #LCD1602 RGB grove
from lcd1602 import LCD1602
from machine import I2C,Pin,ADC
from utime import sleep
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)
#d = LCD1602_RGB.display(i2c, 2, 16)
#d.set_rgb(255, 0, 0)
LIGHT_SENSOR = ADC(0)
SOUND_SENSOR = ADC(1)
button = Pin(18, Pin.IN, Pin.PULL_UP)# button connect to D18
button.irq(lambda pin: InterruptsButton(),Pin.IRQ_FALLING)#Set key interrupt
led = Pin(16, Pin.OUT)#led connect to D16

def InterruptsButton(): #button input
    led.value(0)

led.value(0)
while True:
    average = 0
    lightVal = LIGHT_SENSOR.read_u16()/256
    print(lightVal)
    for i in range (1000):
        sound = SOUND_SENSOR.read_u16()/256
        average += sound
    soundVal = average/1000
    print(soundVal)

    f = open("light_sound_sensor.txt", "a")
    f.write("lightVal="+str(lightVal)+" / soundVal="+str(soundVal)+"\n")
    f.close()

    if soundVal > 20:
        led.value(1)

    d.home()
    d.print('lightVal=')
    d.print(str(lightVal))
    #d.set_rgb(0, 255, 0)
    sleep(1)
    d.setCursor(0, 1)
    d.print('soundVal=')
    d.print(str(soundVal))
    #d.set_rgb(0, 0, 255)
    sleep(1)

