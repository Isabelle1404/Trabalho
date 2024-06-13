class ConversionLibrary:
    # Comprimento
    def meters_to_kilometers(self, meters):
        return meters / 1000

    def kilometers_to_meters(self, kilometers):
        return kilometers * 1000

    def miles_to_kilometers(self, miles):
        return miles * 1.60934

    def kilometers_to_miles(self, kilometers):
        return kilometers / 1.60934

    def yards_to_meters(self, yards):
        return yards * 0.9144

    def meters_to_yards(self, meters):
        return meters / 0.9144

    def feet_to_meters(self, feet):
        return feet * 0.3048

    def meters_to_feet(self, meters):
        return meters / 0.3048

    def inches_to_centimeters(self, inches):
        return inches * 2.54

    def centimeters_to_inches(self, centimeters):
        return centimeters / 2.54

    # Peso
    def kilograms_to_grams(self, kilograms):
        return kilograms * 1000

    def grams_to_kilograms(self, grams):
        return grams / 1000

    def pounds_to_kilograms(self, pounds):
        return pounds * 0.453592

    def kilograms_to_pounds(self, kilograms):
        return kilograms / 0.453592

    def ounces_to_grams(self, ounces):
        return ounces * 28.3495

    def grams_to_ounces(self, grams):
        return grams / 28.3495

    # Temperatura
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15

    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15

    def fahrenheit_to_kelvin(self, fahrenheit):
        return self.celsius_to_kelvin(self.fahrenheit_to_celsius(fahrenheit))

    def kelvin_to_fahrenheit(self, kelvin):
        return self.celsius_to_fahrenheit(self.kelvin_to_celsius(kelvin))
