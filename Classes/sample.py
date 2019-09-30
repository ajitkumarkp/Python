class Cereal:
    def __init__(self, name, brand, number):
        self.name=name
        self.brand=brand
        self.number=number
    
    def __str__(self):
        return "{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name,self.brand,self.number)

c1 = Cereal("Corn Flakes","Kellogg's", 2)
c2 = Cereal("Honey Nut Cheerios","General Mills", 3)

print (c1)
print (c2)
