# by Kami Bigdely
# Docstrings and blank lines
class OnBoardTemperatureSensor:
    """
    construct a temperature sensor
    have it read the voltage
    have it get the temperature by converting it from the voltage
    
    returns: float(voltage)
    """
    VOLTAGE_TO_TEMP_FACTOR = 5.6
    def __init__(self):
        pass
    
    def read_voltage(self):        
        return 2.7
    
    def get_temperature(self):
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR # [celcius]

class CarbonMonoxideSensor:
    """
    construct a carbon monoxide sensor
    have it read the carbon monoxide level
    have it read the sensor voltage
    
    returns: carbon_monoxide level based on temperature and voltage
    """
    VOLTAGE_TO_CO_FACTOR = 0.048
    def __init__(self, temperature_sensor):
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()
            
    def get_carbon_monoxide_level(self):
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(sensor_voltage, self.on_board_temp_sensor.get_temperature())
        return self.carbon_monoxide
    
    def read_sensor_voltage(self):
        # In real life, it should read from hardware.        
        return 2.3
    
    def convert_voltage_to_carbon_monoxide_level(voltage, temperature):
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature
    
class DisplayUnit:
    def __init__(self):
        self.string = ''
        
    def display(self,msg):
        print(msg)
        
class CarbonMonoxideDevice():
    """
    construct a carbon monoxide device
    have it display the cabon monoxide level
    
    returns: display message of carbon_monoxide level 
    """
    def __init__(self, co_sensor, display_unit):
        self.carbonMonoxideSensor = co_sensor 
        self.display_unit = display_unit  

    def Display(self):
        msg = 'Carbon Monoxide Level is : ' \
            + str(self.carbonMonoxideSensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)

if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.Display()
    