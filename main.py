from gpiozero import Servo
from pyPS4Controller.controller import Controller


# We use the GPIOZero Servo class since it does everything we need to control an ESC
# Speed is always a float from 0-1
# 0 is the midpoint, -1 is backwards and 1 is forwards
class RobotMotor(Servo):
    def forward(self, speed):
        self.value = speed

    def backwards(self, speed):
        self.value = -speed


class RobotMotorController:
    def __init__(self, left, right):
        self.leftMotor = RobotMotor(left)
        self.rightMotor = RobotMotor(right)

    def forward(self, speed):
        self.leftMotor.forward(speed)
        self.rightMotor.forward(speed)

    def backwards(self, speed):
        self.leftMotor.backwards(speed)
        self.rightMotor.backwards(speed)

    def left(self, speed):
        self.leftMotor.backwards(speed)
        self.rightMotor.forward(speed)

    def right(self, speed):
        self.leftMotor.forward(speed)
        self.rightMotor.backwards(speed)

    def raw(self, leftSpeed, rightSpeed):
        if leftSpeed > 0:
            self.leftMotor.forward(leftSpeed)
        else:
            self.leftMotor.backwards(leftSpeed)

        if rightSpeed > 0:
            self.rightMotor.forward(rightSpeed)
        else:
            self.rightMotor.backwards(rightSpeed)


class Ps4Controller(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        print("Hello, world!")

    def on_L3_up(self, value):
        print("L3 Moved! {value}")


controller = Ps4Controller(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen(timeout=60, on_connect=print("Controller Connected Successfully"))
