from machine import UART, Pin
import utime,time

WiFi_SSID='<ssid>'  # Wifi_SSID
WiFi_password = '<pwd>'  # WiFi Password
ServerIP = '192.168.178.1' 
Port = '8080'

uart = UART(0, 115200)

def sendCMD(cmd,ack,timeout=2000):
    uart.write(cmd+'\r\n')
    t = utime.ticks_ms()
    while (utime.ticks_ms() - t) < timeout:
        s=uart.read()
        if(s != None):
            s=s.decode()
            print(s)
            if(s.find(ack) >= 0):
                return True
    return False

uart.write('+++')
time.sleep(1)
if(uart.any()>0):uart.read()
sendCMD('AT','OK')
sendCMD("AT+RST","OK")
sendCMD("AT+GMR", "OK")
sendCMD("AT+CWMODE=3","OK")

'''
sendCMD("AT+CWJAP=\""+WiFi_SSID+"\",\""+WiFi_password+"\"","OK",20000)
sendCMD("AT+CIFSR","OK")
sendCMD("AT+CIPSTART=\"TCP\",\""+ServerIP+"\","+Port,"OK",10000)
sendCMD("AT+CIPMODE=1","OK")
sendCMD("AT+CIPSEND",">")

uart.write('Hello World !!!\r\n')
uart.write('ESP8266 TCP Client\r\n')
while True:
    s=uart.read()
    if(s != None):
        s=s.decode()
        print(s)
'''