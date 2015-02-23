import random

# Create pet class and characteristics and cause/effect of user interactions
class pet(object):

	# Initial stats for day 1
	def __init__(self):
		self.holiday = False
		self.scared = False
		self.sick = False
		self.wired = False
		self.age = 0
		self.health = 99
		self.hunger = 0
		self.happy = 99
		self.bladder = 0
		self.sleep = 0
		self.hygiene = 99

	# Check stats 
	def update (self):

		# Daily adjustments
		self.age += 1
		self.hunger += random.randint(1, 15)
		self.bladder += random.randint(1, 15)
		self.sleep += random.randint(1, 10)
		self.hygiene -= random.randint(1, 10)

		# If hunger is greater than 50 adjust health, happy, sleep
		if self.hunger > 50:
			print ("I'M HUNGRY!")
			self.health -= random.randint(5, 15)
			self.happy -= random.randint(1, 10)
			self.sleep -= random.randint(1, 15)

		# If bladder is greater than 50 print warning message and adjust health and happy
		if self.bladder > 50:
			print ("I'M POOPY!")
			self.health -= random.randint(5, 25)
			self.happy -= random.randint(1, 10)

		# Else-if bladder is 99+ print messaged and decrement health and hygiene
		elif self.bladder >= 99:
			print ("MY BLADDER EXPLOADED")
			self.health -= 50
			self.hygiene -= 90

		# If sleep is greated than 50 print warning message and adjust health and happy
		if self.sleep > 50:
			print ("I'M SLEEPY!")
			self.health -= random.randint(1, 10)
			self.happy -= random.randint(5, 25)

		# If happy is less than 60 print warning message
		if self.happy < 60:
			print ("I'M BORED!")
		
		# If happy is greater or equal to 40 then holiday is false
		if self.happy >= 40:
			self.holiday = False

		# Else-if happy is less than 40 and holiday is false decrement happy and set holiday true
		elif self.happy < 40 and not self.holiday:
			self.happy = 20
			self.holiday = True

		# If bladder equals a random integer between 50-75 initialise earthquake and scared = true	
		if self.bladder == random.randint(50, 75):
			self.scared = True
			print("EARTHQUAKE! I'M SCARED")

		# If hunger equals a random integer between 50-75 sick is true and hunger increases
		if self.hunger == random.randint(50, 75):
			self.sick = True
			self.hunger += 90

		# While scared decrease happy and increase bladder
		if self.scared:
			self.happy -= 45
			self.bladder += 90
			self.wired = True

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
	def print_status (self):
		print ("\nAge: {}".format(self.age))
		print ("Health: {}".format(self.health))
		print ("Tiredness: {}".format(self.sleep))
		print ("Hunger: {}".format(self.hunger))
		print ("Happiness: {}".format(self.happy))
		print ("Bladder: {}".format(self.bladder))
		print ("Hygiene: {}\n". format(self.hygiene))

	# Action feed
	def feed(self):
		self.hunger -= 30
		self.bladder += random.randint(1, 10)
		if self.hunger < 0:
			self.hunger = 0

	# Action to use toilet
	def toilet(self):
		self.bladder -= 30
		if self.bladder < 0:
			self.bladder = 0

	# Action clean
	def clean(self):
		self.hygiene += 30
	
	# Action play	
	def play(self):
		self.happy += 30

	# Action to nap
	def nap(self):
		self.sleep -= 30
