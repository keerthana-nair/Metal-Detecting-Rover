#uses micropython code for microcontrollers
import machine
import utime #uTime library specifically designed for microcontrollers

#Setting variables for the motor pins
leftmotorforwards= machine.Pin(11, machine.Pin.OUT)
leftmotorbackwards= machine.Pin(10, machine.Pin.OUT)
rightmotorforwards= machine.Pin(9, machine.Pin.OUT)
rightmotorbackwards= machine.Pin(8, machine.Pin.OUT)

lfpwm= machine.PWM(11, freq= 100, duty_u16= 32768)
rfpwm= machine.PWM(9, freq= 100, duty_u16= 32768)
lbpwm= machine.PWM(10, freq= 100, duty_u16= 32768)
rbpwm= machine.PWM(11, freq= 100, duty_u16= 32768)

#Turn all motors off
def stop():
    lfpwm.duty_u16(0)
    lfpwm.duty_u16(0)
    lfpwm.duty_u16(0)
    lfpwm.duty_u16(0)

    """
    leftmotorforwards.value(0)
    leftmotorbackwards.value(0)
    rightmotorforwards.value(0)
    rightmotorbackwards.value(0)
    
    """

#Turn both motors forwards
def forwards():
    lfpwm.duty_u16(25596)
    rfpwm.duty_u16(25596)

    """
    leftmotorforwards.value(1)
    leftmotorbackwards.value(0)
    rightmotorforwards.value(1)
    rightmotorbackwards.value(0)

    """

#Turn both motors backwards
def backwards():
    lbpwm. duty_u16(25596)
    rbpwm. duty_u16(25596)

    """
    leftmotorforwards.value(0)
    leftmotorbackwards.value(1)
    rightmotorforwards.value(0)
    rightmotorbackwards.value(1)

    """

#Turn left
def left():
    lbpwm. duty_u16(25596)
    rfpwm.duty_u16(25596)

    """
    leftmotorforwards.value(0)
    leftmotorbackwards.value(1)
    rightmotorforwards.value(1)
    rightmotorbackwards.value(0)

    """

#Turn right
def right():
    lfpwm. duty_u16(25596)
    rbpwm.duty_u16(25596)

    """
    leftmotorforwards.value(1)
    leftmotorbackwards.value(0)
    rightmotorforwards.value(0)
    rightmotorbackwards.value(1)

    """

metaldetector= machine.Pin(15, machine.Pin.IN)

#main
while True:
    forwards()
    if metaldetector.value()>0: #high means metal is detected
        print("Detected")
        stop()
        utime.sleep(5)
        break

