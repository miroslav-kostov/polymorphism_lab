from project.animals.animal import Mammal, Bird
from project.food import Vegetable, Seed, Meat, Food, Fruit


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.eaten_food = ["Meat"]
        self.weight_increase = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.eaten_food = ["Meat", "Vegetable", "Seed", "Fruit"]
        self.weight_increase = 0.35

    def make_sound(self):
        return "Cluck"
