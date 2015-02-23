
#! /usr/bin/env python

# Import the modules we need, for creating a GUI
from tkinter import *

# Import attributes from tama file
from tama import pet

# Tamagotchi is equal to class pet
tamagotchi = pet()

# Life span is set to 20 and starts on day 1
max_age = 20

#-------------------------------------------------------------------

def GameOn(event):

    # Check condidtion of pet and run update to update stats
    isAlive()
    tamagotchi.update()

    if tamagotchi.age == max_age:
        startLabel.config(text="CONGRATULATIONS\n\n You Win!\n")
        return False

    updateDisplay()        
    
#-------------------------------------------------------------------
 
def updateDisplay():

    # Update the age label.
    ageLabel.config(text="Age: {}".format(tamagotchi.age))

    # Update the health label.
    healthLabel.config(text="Health: {}".format(tamagotchi.health))

    # Update the tiredness label.
    tirednessLabel.config(text="Tiredness: {}".format(tamagotchi.sleep))

    # Update the hunger label.
    hungerLabel.config(text="Hunger: {}".format(tamagotchi.hunger))

    # Update the happiness label.
    happinessLabel.config(text="Happiness: {}".format(tamagotchi.happy))

    # Update the bladder label.
    bladderLabel.config(text="Bladder: {}".format(tamagotchi.bladder))

    # Update the hygeine label.
    hygieneLabel.config(text="Hygiene: {}\n". format(tamagotchi.hygiene))

#-------------------------------------------------------------------
  
def isAlive():
 
    # If health reaches 0, pet is dead print message and quit
    if tamagotchi.health <= 0:

        # Update the start info label.
        startLabel.config(text="GAME OVER! YOU KILLED IT!")     
        return False

#-------------------------------------------------------------------

# Create a GUI window.
root = Tk()
# Set the title.
root.title("Stay Alive!")
# Set the size.
root.geometry("500x300")

# Add a start label.
startLabel = Label(root, text="GAME ON!\n", font=('Helvetica', 12))
startLabel.pack()

# Add a 'day' label.
ageLabel = Label(root, text="Age: " + str(tamagotchi.age), font=('Helvetica', 12))
ageLabel.pack()

# Add a hunger label.
healthLabel = Label(root, text="Health: " + str(tamagotchi.health), font=('Helvetica', 12))
healthLabel.pack()

# Add a tiredness label.
tirednessLabel = Label(root, text="Tiredness: " + str(tamagotchi.sleep), font=('Helvetica', 12))
tirednessLabel.pack()

# Add a hunger label.
hungerLabel = Label(root, text="Hunger: " + str(tamagotchi.hunger), font=('Helvetica', 12))
hungerLabel.pack()

# Add a happiness label.
happinessLabel = Label(root, text="Happiness: " + str(tamagotchi.happy), font=('Helvetica', 12))
happinessLabel.pack()

# Add a bladder label.
bladderLabel = Label(root, text="Bladder: " + str(tamagotchi.bladder), font=('Helvetica', 12))
bladderLabel.pack()

# Add a hygeine label.
hygieneLabel = Label(root, text="Hygiene: " + str(tamagotchi.hygiene), font=('Helvetica', 12))
hygieneLabel.pack()

btnFeed = Button(root, text="Feed", command=tamagotchi.feed)
btnFeed.pack(side=LEFT, padx=30, pady=5)

btnClean = Button(root, text="Clean", command=tamagotchi.clean)
btnClean.pack(side=LEFT, padx=30, pady=5)

btnPlay = Button(root, text="Play", command=tamagotchi.play)
btnPlay.pack(side=LEFT, padx=30, pady=5)

btnToilet = Button(root, text="Toilet", command= tamagotchi.toilet)
btnToilet.pack(side=LEFT, padx=30, pady=5)

if not tamagotchi.wired:
    btnNap = Button(root, text="Nap", command=tamagotchi.nap)
    btnNap.pack(side=LEFT, padx=30, pady=5)

"""
This thingy below it wrong but it makes it function so until I write a function to call two functions it will do.
"""

# Run the 'GameOn' function when the left mouse button is released.
root.bind('<ButtonRelease-1>', GameOn)

# Start the GUI
root.mainloop()
