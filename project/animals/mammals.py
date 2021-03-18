from project.animals.animal import Mammal, Bird
from project.food import Vegetable, Seed, Meat, Food, Fruit


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.eaten_food = ["Vegetable", "Fruit"]
        self.weight_increase = 0.1

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.eaten_food = ["Meat"]
        self.weight_increase = 0.4

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.eaten_food = ["Meat", "Vegetable"]
        self.weight_increase = 0.3

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.eaten_food = ["Meat"]
        self.weight_increase = 1.0

    def make_sound(self):
        return "ROAR!!!"


