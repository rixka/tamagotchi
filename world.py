from tama import pet

# Create class world to specify user interface
class world (object):

	tamagotchi = pet()

	max_age = 20
	
	# Link user response to action
	def handle_response(tamagotchi, response):

		if response == 'f':
			tamagotchi.feed()
		elif response == 'c':
			tamagotchi.clean()
		elif response == 'p':
			tamagotchi.play()
		elif response == 'n':
			if tamagotchi.wired:
				print ("Tama wired and cannot sleep\n")
			else: 
				tamagotchi.nap()
		elif response == 't':
			tamagotchi.toilet()

		# Damage Control
		else:
			print ("Please try again:\n\n'f' for feed\n'c' for clean\n'p' for play\n'n' for nap\n't' for toilet\n")

	# Begin game and run while day is less than or equal to life span
	while tamagotchi.age <= max_age:

		# Check condidtion of pet and run update to print existing stats
		tamagotchi.update()

		# It Died
		if tamagotchi.health <= 0:
			print ("I'M DEAD!")
			break
		
		tamagotchi.print_status()

		if not tamagotchi.holiday:
			# Prompt for user response and call handling
			response = input("What do you want to do?")
			handle_response(tamagotchi, response)

		# If tamagotchi is on holiday print message and *do not allow actions*
		else:
			print ("### TAMAGOTCHI ON HOLIDAY ###")

		# Increment day
		day += 1

	if day == total_days:
		print ("You Win!\n")
