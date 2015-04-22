import random

# Create pet class and characteristics and cause/effect of user interactions


class Pet(object):
    # Initial stats for day 1
    def __init__(self):
        self.holiday = False
        self.scared = False
        self.sick = False
        self.age = 0
        self.health = 99
        self.hunger = 0
        self.happy = 99
        self.bladder = 0
        self.sleep = 0
        self.hygiene = 99
        self.image = 'vhappy'

    # Check stats 
    def update(self):

        # Daily adjustments
        self.age += 1
        self.hunger += random.randint(1, 15)
        self.bladder += random.randint(1, 15)
        self.sleep += random.randint(1, 10)
        self.hygiene -= random.randint(1, 10)

        # When hungry health, happy, sleep deteriorates
        if self.hunger > 50:
            print("I'M HUNGRY!")
            self.image = "hungry"
            self.health -= random.randint(5, 15)
            self.happy -= random.randint(1, 10)
            self.sleep -= random.randint(1, 15)

        # When needing the toilet health and happy deteriorates
        if self.bladder > 50:
            print("I'M POOPY!")
            self.image =  "poopy"
            self.health -= random.randint(5, 25)
            self.happy -= random.randint(1, 10)

        # When bladder is full health and hygeine significantly deteriorate
        elif self.bladder >= 99:
            print("MY BLADDER EXPLODED")
            self.image = "scared"
            self.scared = True
            self.health -= 50
            self.hygiene -= 90

        # When sleepy health and happy deteriorates
        if self.sleep > 50:
            print("I'M SLEEPY!")
            self.image = "images/sleepy.gif"
            self.health -= random.randint(1, 10)
            self.happy -= random.randint(5, 25)

        if self.happy < 60:
            print("I'M BORED!")
            self.image = "bored"
        
        # Come back from holiday when happiness is satisfactory
        if self.happy >= 40:
            self.holiday = False

        # When unhappy pet goes on holiday and becomes pissed off that it had to
        elif self.happy < 40 and not self.holiday:
            self.happy = 20
            self.holiday = True

        # Create random possibility for an Earthquake and scare pet    
        if self.bladder == random.randint(50, 75):
            self.scared = True
            print("EARTHQUAKE! I'M SCARED")

        # Create random possibility to get sick and very hungry
        if self.hunger == random.randint(50, 75):
            self.sick = True
            self.hunger += 90

        # While scared decrease happy and increase bladder
        if self.scared:
            self.happy -= 45
            self.bladder += 90

        # While sick increase hunger and bladder nad decrease hygiene
        if self.sick:
            self.hunger += random.randint(1, 10)
            self.hygiene -= random.randint(1, 10)
            self.bladder += random.randint(1, 10)

        # While on holiday improve stats slightly
        if self.holiday:
            self.happy += 5
            self.health += random.randint(1, 5)
            self.hunger -= random.randint(1, 5)
            self.happy += random.randint(1, 5)
            self.bladder -= random.randint(1, 5)
            self.sleep -= random.randint(1, 5)
            self.hygiene += random.randint(1, 5)

    # Print all stats
    def print_status(self):
        print("\nAge: {}".format(self.age))
        print("Health: {}".format(self.health))
        print("Tiredness: {}".format(self.sleep))
        print("Hunger: {}".format(self.hunger))
        print("Happiness: {}".format(self.happy))
        print("Bladder: {}".format(self.bladder))
        print("Hygiene: {}\n". format(self.hygiene))

    def feed(self):
        self.hunger -= 30
        self.bladder += random.randint(1, 10)
        if self.hunger < 0:
            self.hunger = 0

    def toilet(self):
        self.bladder -= 30
        if self.bladder < 0:
            self.bladder = 0

    def clean(self):
        self.hygiene += 30
    
    def play(self):
        self.happy += 30

    def nap(self):
        self.sleep -= 30
