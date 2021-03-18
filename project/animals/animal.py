from abc import ABC, abstractmethod
from project.food import Vegetable, Seed, Meat, Food, Fruit


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.eaten_food = []
        self.food_eaten = 0
        self.weight_increase = 0

    def make_sound(self):
        pass

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type not in self.eaten_food:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.weight += food.quantity * self.weight_increase
        self.food_eaten += food.quantity


class Mammal(Animal):
    @abstractmethod
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Bird(Animal):
    @abstractmethod
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
