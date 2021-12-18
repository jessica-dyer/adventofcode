import random
from enum import Enum
import math

def draw_card():
    dict = {'Type A': .2,
            'Type B': .2,
            'Type C': .6}
    num = random.random()

    card = random.choices(('Type A', 'Type B', 'Type C'), weights = (20, 20, 60), k=1)

    return card


for _ in range(40):
    print(draw_card())

def draw_card_v2():
    dict = {'Type A': .2,
            'Type B': .2,
            'Type C': .6}
    num = random.random()

    keys = list(dict.keys())
    for key in keys:
        num -= dict[key]
        if num < 0:
            return key

draw_card_v2()

class CardType(Enum):
    A = "A"
    B = "B"
    C = "C"

    def probability(self):
        if self == CardType.A:
            return .2
        elif self == CardType.B:
            return 0.2
        elif self == CardType.C:
            return 0.6
        return None

    def unique_count(self):
        if self == CardType.A:
            return 5
        elif self == CardType.B:
            return 10
        elif self == CardType.C:
            return 200
        return None

foo = CardType.C
print(foo.probability())

class Card():
    def __init__(self, card_type):
        self.card_type = card_type
        self.id = math.ceil(random.random() * self.card_type.unique_count())

    def string_id(self):
        return self.card_type.value + str(self.id)

def draw_card_v3():
    all_card_types = [CardType.A, CardType.B, CardType.C]

    num = random.random()

    for t in all_card_types:
        num -= t.probability()
        if num < 0:
            return Card(t)

for _ in range(10):
    print(draw_card_v3().string_id())