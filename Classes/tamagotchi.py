import random

THRESH = 100

class Pet:
    s_list_str = ["aah", "hmmm"]

    hunger_decrement = random.randrange(0, THRESH) 

    def __init__(self):
        self.hunger = random.randrange(0, THRESH)
        self.boredom = random.randrange(0, THRESH)
        self.sounds = s_list_str.copy()
    
    def clock_tick(self):
        self.hunger += 1
        self.boredom += 1
    
    def __str__(self):
        if self.hunger >=THRESH or self.boredom >=THRESH:
            return ("I am bored or Hungry")
        else:
            return ("I am Happy")
    
    def reduce_boredom(self):
        self.hunger= self.hunger-hunger_decrement

    def teach(self):
        self.sounds.append("ohhh")
        reduce_boredom(self)
    
    def hi(self):
        reduce_boredom(self)
        i = random.randrange(0,len(self.sounds))
        print(self.sounds[i])
    