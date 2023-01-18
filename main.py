#Code pour se connecter au Bluetooth
from machine import Pin,UART

uart = UART(0,38400)

#while True:
    # print('checking BT')
   # if uart.any():
       # command = uart.readline()
      #  print(command)
        
#Communication Bluetooth

# DAC


# ADC
import machine
import utime
 
analog_value1 = machine.ADC(28)
analog_value2 = machine.ADC(27)
 # Valeur allant de 0-65535 -> 0-3.3V .... Manque le multiplicateur du diviseur de tension***
 
def oscilloscope(pin, num):
    reading = pin.read_u16()
    test = reading* 5.03548*10E-6
    print("Valeur ADC" + num + ": " + str(test))
    print(reading)
 
while True:
    #ADC1
    oscilloscope(analog_value1, "1")
    #ADC 2
    oscilloscope(analog_value2, "2")
    utime.sleep(0.2)
    
    