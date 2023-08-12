import uos
import machine
import utime

"""
ESPRESSIF AT Command Set
https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/
"""

print()
print("Machine: \t" + uos.uname()[4])
print("MicroPython: \t" + uos.uname()[3])

#indicate program started visually
led_onboard = machine.Pin(25, machine.Pin.OUT)
led_onboard.value(0)     # onboard LED OFF/ON for 0.5/1.0 sec
utime.sleep(0.5)
led_onboard.value(1)
utime.sleep(1.0)
led_onboard.value(0)

uart0 = machine.UART(0, baudrate=115200)
print(uart0)

def sendCMD_waitResp(cmd, uart=uart0, timeout=2000):
    print("CMD: " + cmd)
    uart.write(cmd)
    waitResp(uart, timeout)
    print()
    
def waitResp(uart=uart0, timeout=2000):
    prvMills = utime.ticks_ms()
    resp = b""
    while (utime.ticks_ms()-prvMills)<timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
    print("resp:")
    try:
        print(resp.decode())
    except UnicodeError:
        print(resp)

'''
sendCMD_waitResp('AT\r\n')          #Test AT startup
sendCMD_waitResp('AT+GMR\r\n')      #Check version information
#sendCMD_waitResp('AT+RESTORE\r\n')  #Restore Factory Default Settings
sendCMD_waitResp('AT+CWMODE?\r\n')  #Query the Wi-Fi mode
sendCMD_waitResp('AT+CWMODE=1\r\n') #Set the Wi-Fi mode = Station mode
sendCMD_waitResp('AT+CWMODE?\r\n')  #Query the Wi-Fi mode again
#sendCMD_waitResp('AT+CWLAP\r\n', timeout=10000) #List available APs
sendCMD_waitResp('AT+CWJAP="FRITZ!Box 5530 DD","79332516618621366233"\r\n', timeout=5000) #Connect to AP
sendCMD_waitResp('AT+CIFSR\r\n')    #Obtain the Local IP Address
'''

sendCMD_waitResp('AT\r\n')
sendCMD_waitResp('AT+RST\r\n')
sendCMD_waitResp('AT+GM\r\n')
sendCMD_waitResp('AT+CWMODE=3\r\n')
sendCMD_waitResp('AT+CWJAP="<ssid>","<pwd>"\r\n', timeout=5000) #Connect to AP
sendCMD_waitResp('AT+CIFSR')
sendCMD_waitResp('AT+CIPSTART="TCP","192.168.178.23","8080"')
sendCMD_waitResp('AT+CIPMODE=1')
sendCMD_waitResp('AT+CIPSEND')

uart0.write('Hello World !!!\r\n')
uart0.write('ESP8266 TCP Client\r\n')
while True:
    s=uart0.read()
    if(s != None):
        s=s.decode()
        print(s)