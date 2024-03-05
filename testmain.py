#!/bin/python3
from sapient import species

human = species()

human.name = "human"
human.blood = "crimson red"
human.id = "45-G"

print(human.id)
print(human.num_badges())
human.set_color_A("#FF00FF")
print(hex(human.color_A_side))

zuru = species()
zuru.name = "zurulian"
zuru.add_stance("quadruped",0.5)
zuru.add_stance("biped",0.9)
print(zuru.stances)