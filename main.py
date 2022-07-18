from servo import Servo
from machine import Pin
import utime as tm



buz =Pin(25,Pin.OUT)

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
src =Servo(10)
tri =Servo(11)
lift =Servo(9)
door =Servo(8)
door.move(0)
tm.sleep(1)
for i in range(0,120):
    door.move(i)
    tm.sleep(0.001)
for i in range(30,161):
    lift.move(i)
    tm.sleep(0.001)
tm.sleep(1)

def dis():
    timepassed=0
    trigger.low()
    tm.sleep_us(2)
    trigger.high()
    tm.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = tm.ticks_us()
    while echo.value() == 1:
        signalon = tm.ticks_us()
    measured_time = signalon - signaloff
    distance_cm = (measured_time * 0.0343) / 2
    distance_cm = round(distance_cm,2)
    return(distance_cm)
def tre(i):
    tri.move(i)
    tm.sleep(1)
    print("trigger")
while True:
    print("start") 
    for i in range(50,180):
        src.move(i)
        tm.sleep(0.01)
        if(dis()<15):
            tre(i)
    for i in range(180,49,-1):
        src.move(i)
        tm.sleep(0.01)
        if(dis()<15):
            tre(i)