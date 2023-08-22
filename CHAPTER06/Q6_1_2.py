class Person:
    def __init__(self,
                 name = '',
                 nationality = '',
                 birth = '',
                 address = ''):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address

    def show_attributes(self):
        print("名前:", self.name)
        print("国籍:", self.nationality)
        print("生まれた年:", self.birth)
        print("住んでいる所:", self.address)

heroine = Person('かぐや姫', '日本', '685', '静岡県富士市')
print(heroine.show_attributes())

hero = Person('金太郎',  '日本', '956', '静岡県駿東郡小山町')
print(hero.show_attributes())

class Car:
    weight = 400
    num_wheels = 4

    def calc_weight_per_wheel(self):
        return self.weight / self.num_wheels
my_car = Car()
print(my_car.calc_weight_per_wheel())
