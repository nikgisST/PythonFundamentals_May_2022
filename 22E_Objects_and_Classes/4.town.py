class Town:
    def __init__(self, name: str , latitude="0°N", longitude="0°E"):    #latitude="0°N", longitude="0°E") това са опционални елементи
        self.name = name
        self.latitude = latitude        #тук се подава стойността по подразбиране, тоест 0 градуса
        self.longitude = longitude

    def set_latitude(self, latitude):
        self.latitude = latitude       #тук се промена стойността на географската дължина като извикаме съответния метод

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
# print(town.latitude)        #("42° 41\' 51.04\' N")
# print(town.longitude)       #("23° 19\' 26.94\' E")
print(town)

