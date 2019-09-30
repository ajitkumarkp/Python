# class Pokemon(object):
#     attack = 12
#     defense = 10
#     health = 15
#     p_type = "Normal"

#     def __init__(self, name, level = 5):
#         self.name = name
#         self.level = level

#     def train(self):
#         self.update()
#         self.attack_up()
#         self.defense_up()
#         self.health_up()
#         self.level = self.level + 1
#         if self.level%self.evolve == 0:
#             return self.level, "Evolved!"
#         else:
#             return self.level

#     def attack_up(self):
#         self.attack = self.attack + self.attack_boost
#         return self.attack

#     def defense_up(self):
#         self.defense = self.defense + self.defense_boost
#         return self.defense

#     def health_up(self):
#         self.health = self.health + self.health_boost
#         return self.health

#     def update(self):
#         self.health_boost = 5
#         self.attack_boost = 3
#         self.defense_boost = 2
#         self.evolve = 10

#     def __str__(self):
#         self.update()
#         return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

# class Grass_Pokemon(Pokemon):
#     attack = 15
#     defense = 14
#     health = 12

#     def update(self):
#         self.health_boost = 6
#         self.attack_boost = 2
#         self.defense_boost = 3
#         self.evolve = 12

#     def moves(self):
#         self.p_moves = ["razor leaf", "synthesis", "petal dance"]

#     def action(self):
#         return "{} knows a lot of different moves!".format(self.name)

#     def train(self):
#         self.update()
#         self.level = self.level + 1
#         if self.level>=10:
#             self.attack_up()
#         self.defense_up()
#         self.health_up()
#         if self.level%self.evolve == 0:
#             return self.level, "Evolved!"
#         else:
#             return self.level

# p1 = Grass_Pokemon("Belle")
# p2 = Grass_Pokemon("Bulby")

# p3 = Grass_Pokemon("Pika") # name is Pika n self.level=5

# p3.train()
# p3.train()
# p3.train()
# p3.train()
# p3.train()

# print (p3)
# # will call parent train(), and child update() attack_boost=2, self_attack=15+2
# # self.defense = 14+3, self.health= 12+6, self.level=5+1, if self.level%self.evolve i.e 6%12=6
# # self.level=6


class Pokemon():
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name,level = 5):
        self.name = name
        self.level = level
        self.weak = "Normal"
        self.strong = "Normal"

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10


    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"

    def update(self):
        self.health_boost = 3
        self.attack_boost = 4
        self.defense_boost = 3

class Fire_Pokemon(Pokemon):
    p_type = "Fire"

class Flying_Pokemon(Pokemon):
    p_type = "Flying"
















