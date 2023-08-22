class Nigiri:
    def __init__(self):
        self.rice = "おしし"
        self.sauce = "醤油"
    
    def show_attributes(self):
        print("rice: {}".format(self.rice))
        print("sauce: {}".format(self.sauce))

class Katsuo(Nigiri):
    top = "かつお"
    topping = "生姜とねげ"
    price = 100
    
    def show_attributes(self):
        super().show_attributes()
        print("topping: {}".format(self.topping))

k1 = Katsuo()
k1.show_attributes()

