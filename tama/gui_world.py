from tkinter import *
from tama import Pet

tamagotchi = Pet()
max_age = 20
# -------------------------------------------------------------------
def state(state):
	btnFeed.config(state=state)
	btnClean.config(state=state)
	btnPlay.config(state=state)
	btnToilet.config(state=state)
	btnNap.config(state=state)
# -------------------------------------------------------------------


def GameOn():
	tamagotchi.update()
	updateDisplay()
# -------------------------------------------------------------------


def updateDisplay():
	try:
		if tamagotchi.age == max_age:
			startLabel.config(text="CONGRATULATIONS\n\n You Win!")
			state(DISABLED)
			return

		if tamagotchi.holiday:
			btnFeed.config(text='HOLIDAY', command=GameOn)
			btnClean.config(text='HOLIDAY', command=GameOn)
			btnPlay.config(text='HOLIDAY', command=GameOn)
			btnToilet.config(text='HOLIDAY', command=GameOn)
			btnNap.config(text='HOLIDAY', command=GameOn)

		else:
			btnFeed.config(text="Feed", command=combine_funcs(tamagotchi.feed, GameOn))
			btnClean.config(text="Clean", command=combine_funcs(tamagotchi.clean, GameOn))
			btnPlay.config(text="Play", command=combine_funcs(tamagotchi.play, GameOn))
			btnToilet.config(text="Toilet", command=combine_funcs(tamagotchi.toilet, GameOn))
			btnNap.config(text="Nap", command=combine_funcs(tamagotchi.nap, GameOn))

			if tamagotchi.scared:
				btnNap.config(state=DISABLED)
			else:
				btnNap.config(state=NORMAL)
			
		isAlive()

	finally:
		# Update labels
		ageLabel.config(text="Age: {}".format(tamagotchi.age))
		healthLabel.config(text="Health: {}".format(tamagotchi.health))
		tirednessLabel.config(text="Tiredness: {}".format(tamagotchi.sleep))
		hungerLabel.config(text="Hunger: {}".format(tamagotchi.hunger))
		happinessLabel.config(text="Happiness: {}".format(tamagotchi.happy))
		bladderLabel.config(text="Bladder: {}".format(tamagotchi.bladder))
		hygieneLabel.config(text="Hygiene: {}".format(tamagotchi.hygiene))
		pet.config(image=images[tamagotchi.image])

# -------------------------------------------------------------------


def isAlive():

	# Dead
	if tamagotchi.health <= 0:
		startLabel.config(text="\nGAME OVER! YOU KILLED IT!\n")
		state(DISABLED)
	else:
		startLabel.config(text="\nGAME ON!\n")
		state(NORMAL)
	return
# -------------------------------------------------------------------


def combine_funcs(*funcs):
	def combined_func(*args, **kwargs):
		for f in funcs:
			f(*args, **kwargs)
	return combined_func
# -------------------------------------------------------------------


# Create a GUI window.
root = Tk()
root.title("Stay Alive!")
root.geometry("450x305")

images = {
	'bored': PhotoImage(file="images/bored.gif"),
	'vhappy': PhotoImage(file="images/vhappy.gif"),
	'hungry': PhotoImage(file="images/hungry.gif"),
	'poopy': PhotoImage(file="images/poopy.gif"),
	'scared': PhotoImage(file="images/scared.gif"),
	'sleepy': PhotoImage(file="images/sleepy.gif"),
}

# Add labels
startLabel = Label(root, text="\nGAME ON!\n", font=('Helvetica', 12))
startLabel.grid(columnspan=6)
btnReset = Button(root, text="Reset", command=combine_funcs(tamagotchi.__init__, updateDisplay))
btnReset.grid(column=6, row=0)

ageLabel = Label(root, text="Age: {}".format(tamagotchi.age), font=('Helvetica', 12))
ageLabel.grid(sticky=W, padx=20, columnspan=2, row=2)
healthLabel = Label(root, text="Health: {}".format(tamagotchi.health), font=('Helvetica', 12))
healthLabel.grid(sticky=W, padx=20, columnspan=2, row=3)
tirednessLabel = Label(root, text="Tiredness: {}".format(tamagotchi.sleep), font=('Helvetica', 12))
tirednessLabel.grid(sticky=W, padx=20, columnspan=2, row=4)
hungerLabel = Label(root, text="Hunger: {}".format(tamagotchi.hunger), font=('Helvetica', 12))
hungerLabel.grid(sticky=W, padx=20, columnspan=2, row=5)
happinessLabel = Label(root, text="Happiness: {}".format(tamagotchi.happy), font=('Helvetica', 12))
happinessLabel.grid(sticky=W, padx=20, columnspan=2, row=6)
bladderLabel = Label(root, text="Bladder: {}".format(tamagotchi.bladder), font=('Helvetica', 12))
bladderLabel.grid(sticky=W, padx=20, columnspan=2, row=7)
hygieneLabel = Label(root, text="Hygiene: {}".format(tamagotchi.hygiene), font=('Helvetica', 12))
hygieneLabel.grid(sticky=W, padx=20, columnspan=2, row=8)

pet = Label(root, image=images[tamagotchi.image])
pet.grid(sticky=E, column=2, row=2, columnspan=5, rowspan=7, pady=5)

# Add buttons
btnFeed = Button(root, text="Feed", command=combine_funcs(tamagotchi.feed, GameOn))
btnFeed.grid(column=2, row=10)
btnClean = Button(root, text="Clean", command=combine_funcs(tamagotchi.clean, GameOn))
btnClean.grid(column=3, row=10)
btnPlay = Button(root, text="Play", command=combine_funcs(tamagotchi.play, GameOn))
btnPlay.grid(column=4, row=10)
btnToilet = Button(root, text="Toilet", command=combine_funcs(tamagotchi.toilet, GameOn))
btnToilet.grid(column=5, row=10)
btnNap = Button(root, text="Nap", command=combine_funcs(tamagotchi.nap, GameOn))
btnNap.grid(column=6, row=10, rowspan=2)

# Start the GUI
root.mainloop()
