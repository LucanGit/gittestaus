class Person:

    #Lisätään tänne tekstiä
    def __init__(self, name: str, age: int, city, address, phone_number):
        self.name = name
        self.age = age
        self._city = city
        self._address = address
        self._phone_number = phone_number

    def return_name(self):
        return self.name

    def set_name(self, x: str):
        self.name = x

    def return_age(self):
        return self.age

    def set_age(self, y: int):
        self.age = y
    
    def __str__(self):
        return f"Hi, I'm {self.name} and I am ({self.age}) years old"
 

    @property
    def city(self, _default = None):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def phone_number(self, _default=None):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    def __str__(self):
        return f'Address: {self._address}\nCity: {self._city}\nPhone: {self._phone_number}'