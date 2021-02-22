from controller import Motor


class WheelInfo:
    def __init__(self, left_wheel_indexes: list[int], right_wheel_indexes: list[int]):
        self.LeftWheels = left_wheel_indexes
        self.RightWheels = right_wheel_indexes


def turn_left(m: list[Motor], wi: WheelInfo, right_wheel_velocity: int):
    for i in wi.RightWheels:
        m[i].setVelocity(right_wheel_velocity + 4)


def turn_right(m: list[Motor], wi: WheelInfo, left_wheel_velocity: int):
    for i in wi.RightWheels:
        m[i].setVelocity(left_wheel_velocity + 4)


def turn_in_place(m: list[Motor], wi: WheelInfo, direction: str, turn_speed: int):
    if direction == "left":
        for i in wi.RightWheels:
            m[i].setVelocity(turn_speed)
        for i in wi.LeftWheels:
            m[i].setVelocity(turn_speed * -1)
    elif direction == "right":
        for i in wi.RightWheels:
            m[i].setVelocity(turn_speed * -1)
        for i in wi.LeftWheels:
            m[i].setVelocity(turn_speed)
    else:
        raise Exception("direction is neither left nor right but was " + direction)
