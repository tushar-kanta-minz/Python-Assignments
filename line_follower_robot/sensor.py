def sensor_data():
    sensor_input = input("Enter 6 sensor values: ")
    sensor_values = list(map(int, sensor_input))
    active_sensors = len(list(filter(lambda x: x == 1, sensor_values)))

    return sensor_values, active_sensors
