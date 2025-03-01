import time
from sbot import motors, BRAKE

motors.set_power(0, 1)
motors.set_power(1, 1)

time.sleep(5)  

motors.set_power(0, BRAKE)
motors.set_power(1, BRAKE)

