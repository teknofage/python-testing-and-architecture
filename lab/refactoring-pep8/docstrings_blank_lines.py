# by Kami Bigdely
# Docstrings and blank lines
class OnBoardTemperatureSensor:
    """
    Construct a temperature sensor.
    Have it read the voltage.
    Have it get the temperature by converting it from the voltage.
    
    Returns: float(voltage).
    """
    VOLTAGE_TO_TEMP_FACTOR = 5.6
    def __init__(self):
        """initializes OnBoardTemperatureSensor"""
        pass
    
    def read_voltage(self):  
        """returns voltage"""
        return 2.7
    
    def get_temperature(self):
        """returns temperature based on voltage"""
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR # [celcius]

class CarbonMonoxideSensor:
    """
    Construct a carbon monoxide sensor.
    Have it read the carbon monoxide level.
    Have it read the sensor voltage.
    
    Returns: carbon_monoxide level based on temperature and voltage.
    """
    VOLTAGE_TO_CO_FACTOR = 0.048
    def __init__(self, temperature_sensor):
        """initializes CarbonMonoxideSensor"""
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()
            
    def get_carbon_monoxide_level(self):
        """extracts the carbon monoxide level from the sensor's reading"""
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(self, sensor_voltage, self.on_board_temp_sensor.get_temperature())
        return self.carbon_monoxide
    
    def read_sensor_voltage(self):
        """reads the voltage from the sensor"""
        # In real life, it should read from hardware.        
        return 2.3
    
    def convert_voltage_to_carbon_monoxide_level(self, voltage, temperature):
        """converts the voltage to a carbon-monoxide level using an equation"""
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature
    
class DisplayUnit:
    """
    Controls the display on the unit
    """
    def __init__(self):
        """initialiizes the display with an empty string"""
        self.string = ''
        
    def display(self,msg):
        """prints the message on the display"""
        print(msg)
        
class CarbonMonoxideDevice():
    """
    Construct a carbon monoxide device.
    Have it display the cabon monoxide level.
    
    Returns: Display message of carbon monoxide level.
    """
    def __init__(self, co_sensor, display_unit):
        """initializes a CarbonMonoxideDevice"""
        self.carbonMonoxideSensor = co_sensor 
        self.display_unit = display_unit  

    def display(self):
        """displays the readings from the CarbonMOnoxideDevice"""
        msg = 'Carbon Monoxide Level is : ' \
            + str(self.carbonMonoxideSensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)

if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.display()
    