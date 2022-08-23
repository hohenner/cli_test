# import testConsole 
def all_coordinates_found(coordinates):
    keys = coordinates.keys()
    'x' in keys and 'y' in keys and 'z' in keys


def retrieve_coordinates():
    coordinates = {}
    while not all_coordinates_found(coordinates):
        reading = readConsole()
        data_type, data_value = reading.split(':')
        if not 'log' in data_type:
            coordinates[data_type] = data_value.strip() 
    coordinates

# test if exception is raised, return true if no exception raised, else false
def test_Accel():
    try:
        writeConsole('accelData')
        coordinates = retrieve_coordinates()
        return true
    except (InvalidCommand, NotConnected) as e:
        return false
