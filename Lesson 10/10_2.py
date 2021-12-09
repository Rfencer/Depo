from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def material_needed(self):
        pass


class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def material_needed(self):
        return 2 * self.height + 0.3


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def material_needed(self):
        return self.size / 6.5 + 0.5


suit = Suit(10)
coat = Coat(13)

print(suit.material_needed)
print(coat.material_needed)

