def movement(sensor_values):

    if sensor_values[2] == 1 and sensor_values[3] == 1:
        return "Move Forward"
    
    if sensor_values[0] == 1 or sensor_values[1] == 1:
        return "Turn Left"
    
    if sensor_values[4] == 1 or sensor_values[5] == 1:
        return "Turn Right"

    if sensor_values == [0, 0, 0, 0, 0, 0]:
        return "Stop Robot"

    if sensor_values == [1, 1, 1, 1, 1, 1]:
        return "Junction Detected"

    return "Stop Robot"

