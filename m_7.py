class Car:
    pass
my_car = Car()
type(my_car)
#__init__()

class Car:
   def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color

#mustang = Car(make="Ford", model_name="Mustang", color="Red", top_speed=250)
#print(mustang.make)

mustang = Car(make="Ford", model_name="Mustang", color="Yellow", top_speed=250)
print(mustang)

def __str__(self):
    return f'{self.color} {self.make} {self.model_name}'
print(mustang)