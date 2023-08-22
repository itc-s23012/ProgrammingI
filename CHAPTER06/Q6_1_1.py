class Cat:
    cry = "ニャー"
    legs = 4
    is_animal = True

tama = Cat()
print("鳴き声: {}, 足の数: {}, 動物: {}".format(tama.cry, tama.legs, tama.is_animal))

class Car:
    pass
my_car = Car()
print(type(my_car))

class Car:
    num_wheels = 4
my_car = Car()
print(my_car.num_wheels)

class Car:
    weight = 4000
    num_wheels = 4

    def calc_weight_per_wheel(self):
        return 100.0
my_car = Car()
print(my_car.calc_weight_per_wheel())
