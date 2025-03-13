class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):  # Computed property
        return (self._celsius * 9/5) + 32  # Converts to Fahrenheit

temp = Temperature(0)
print(temp.fahrenheit)  # ✅ Output: 32.0 (0°C = 32°F)
