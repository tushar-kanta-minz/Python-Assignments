angles = [30,-15,45,200,60,90]

def validAngle(angle):
    valid_angle = list(filter(lambda x:0<x<180, angle))
    return valid_angle

def srvoMotor_cmd(vld_angle):
    commands = list(map(lambda angle: angle*10, vld_angle))
    return commands


filtered_angle = validAngle(angles)
print("Valid Angles: ",filtered_angle)
print("Servo Commands: ",srvoMotor_cmd(filtered_angle))