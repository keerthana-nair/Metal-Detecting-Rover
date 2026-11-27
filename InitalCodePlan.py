"""How to code the Raspberry Pi using the gpiozero library"""
"""reference: https://projects.raspberrypi.org/en/projects/physical-computing/14"""
#This library uses Broadcom (BCM) pin numbering for the GPIO pins, as opposed to physical (BOARD) numbering
import gpiozero
import time

"""How to code the LED"""
from gpiozero import LED #This line is redundant, but it is used to import the LED class from the gpiozero library if giozero is not imported
led= LED(17) #pin number 17 for the LED
led.on() #turns the LED on
led.off() #turns the LED off
led.blink() #blinks the LED on and off every second
led.blink(on_time=0.5, off_time=0.5, n=10) #blinks the LED on and off every half second for 10 times

"""How to code the motor"""
from gpiozero import Motor
motor1= Motor(4,14) #pin numbers for the motor, 4 is the forward pin and 14 is the backward pin
motor2= Motor(17,27)
#or you write motor1= Motor(forward=4, backward=14) and motor2= Motor(forward=17, backward=27)

motor1.forward() #moves the motor forward
motor2.backward() #moves the motor backward

motor1.forward(0.5) #moves the motor forward at half speed
motor2.backward(0.5) #moves the motor backward at half speed

#how to reverse the motor direction
motor1.forward()
motor2.backward()
while True:
    time.sleep(5) #waits for 5 seconds
    motor1.reverse()
    motor2.reverse()
#press Ctrl+C to stop the program and exit the loop

#how to stop the motors
motor1.stop()
motor2.stop()

"""or if you want to control the two motors together, you could use the Robot class"""
from gpiozero import Robot
robot= Robot((4,14),(17,27)) #pin numbers for the motors, 4 is the forward pin and 14 is the backward pin, 17 is the forward pin and 27 is the backward pin
#or if you want to see which pin is which, you could use Robot(left=(4, 14), right=(17, 27))

robot.forward() #moves the robot forward
robot.backward() #moves the robot backward
robot.reverse() #reverses the robot direction
robot.forward(0.5) #moves the robot forward at half speed
robot.left() #turns the robot left
robot.right() #turns the robot right
robot.stop() #stops the robot


"""How to use motor in conjunction with a metal detector"""
"""reference: https://gpiozero.readthedocs.io/en/stable/recipes.html"""
from gpiozero import DigitalInputDevice #or just InputDevice

def stop_motor():
    motor1.stop() # Stop the motor when metal is detected
    motor2.stop() # Stop the second motor

def start_motor():
    motor1.forward() # Restart the motor when metal is not detected
    motor2.forward() # Restart the second motor

# Metal detector is connected to GPIO pin 4
metal_detector = DigitalInputDevice(4)

motor1.forward() # Start the motor when the program runs
motor2.forward() # Start the second motor

# When metal is detected (output goes LOW)
metal_detector.when_low = stop_motor()

# Optional: When no metal is detected (output goes HIGH), restart the motor
metal_detector.when_high = start_motor() # (If desired)

# Keep the program running (optional - for continuous monitoring)
while True:
    pass #placeholder for code- we need to add something here. Runs indefinitely until interrupted

#if metal detected- LED on/blinks, motor stops
#need a motion sensor to detect obstacles and stop the robot from moving into them