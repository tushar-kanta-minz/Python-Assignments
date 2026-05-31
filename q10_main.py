from line_follower_robot.sensor import sensor_data
from line_follower_robot.movement import movement

sensor_values, active_sensors = sensor_data()

action = movement(sensor_values)

print("Sensor Values:", sensor_values)
print("Active Sensors:", active_sensors)
print("Robot Action:", action)