def testing (a, b):
    if (a==b):
        return True
    else:
        return False


class car():
    def __init__(self):
        print ("You have a new car!")
    def __str__(self):
        return "Your car is a {} {} {}".format(self.year, self.maker, self.model)

    def set(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year  = year



