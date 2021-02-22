"""first_controller controller."""
from controller import Robot, Motor
import utils

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# wheels
motorName = ["wheel1", "wheel2", "wheel3", "wheel4"]
wheels = []
for i in motorName:
    device = robot.getDevice(i)
    device.setPosition(float('inf'))
    device.setVelocity(0.0)
    wheels.append(device)
wheelInfo = utils.WheelInfo([0, 2], [3, 1])

# distance sensors
dsSensorNames = ["ds_left", "ds_right"]
dsSensors = []
for i in dsSensorNames:
    device = robot.getDevice(i)
    device.enable(timestep)
    dsSensors.append(device)

# -- logic -- #
leftSpeed = 4
rightSpeed = 4
count = 0
while robot.step(timestep) != -1:
    if count > 0:
        utils.turn_in_place(wheels, wheelInfo, "right", 4)
        count -= 1
        if count == 0:
            print("object avoided")
        continue
    elif dsSensors[0].getValue() < 1000 or dsSensors[1].getValue() < 1000:
        print("object detected avoiding")
        count = 60

    wheels[0].setVelocity(leftSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
    wheels[1].setVelocity(rightSpeed)

    pass
