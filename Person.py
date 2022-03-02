class Person:
    #Lisätään tänne tekstiä
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

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

    
testi = Person("Timo", 35)

print(testi.name)
print(testi.age)
    
