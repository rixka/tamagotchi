from tkinter import *
from tama import pet

tamagotchi = pet()

max_age = 20

#-------------------------------------------------------------------


def GameOn():
    isAlive()
    tamagotchi.update()

    if tamagotchi.age == max_age:
        startLabel.config(text="CONGRATULATIONS\n\n You Win!\n")
        return False

    updateDisplay()            
#-------------------------------------------------------------------


def updateDisplay():

    # Update labels
    ageLabel.config(text="Age: {}".format(tamagotchi.age))
    healthLabel.config(text="Health: {}".format(tamagotchi.health))
    tirednessLabel.config(text="Tiredness: {}".format(tamagotchi.sleep))
    hungerLabel.config(text="Hunger: {}".format(tamagotchi.hunger))
    happinessLabel.config(text="Happiness: {}".format(tamagotchi.happy))
    bladderLabel.config(text="Bladder: {}".format(tamagotchi.bladder))
    hygieneLabel.config(text="Hygiene: {}\n". format(tamagotchi.hygiene))
#-------------------------------------------------------------------
  

def isAlive():
 
    # Dead
    if tamagotchi.health <= 0:
        startLabel.config(text="GAME OVER! YOU KILLED IT!")     
        return False
#-------------------------------------------------------------------

# Create a GUI window.
root = Tk()
root.title("Stay Alive!")
root.geometry("500x300")

# Add labels
startLabel = Label(root, text="GAME ON!\n", font=('Helvetica', 12))
startLabel.pack()
ageLabel = Label(root, text="Age: " + str(tamagotchi.age), font=('Helvetica', 12))
ageLabel.pack()
healthLabel = Label(root, text="Health: " + str(tamagotchi.health), font=('Helvetica', 12))
healthLabel.pack()
tirednessLabel = Label(root, text="Tiredness: " + str(tamagotchi.sleep), font=('Helvetica', 12))
tirednessLabel.pack()
hungerLabel = Label(root, text="Hunger: " + str(tamagotchi.hunger), font=('Helvetica', 12))
hungerLabel.pack()
happinessLabel = Label(root, text="Happiness: " + str(tamagotchi.happy), font=('Helvetica', 12))
happinessLabel.pack()
bladderLabel = Label(root, text="Bladder: " + str(tamagotchi.bladder), font=('Helvetica', 12))
bladderLabel.pack()
hygieneLabel = Label(root, text="Hygiene: " + str(tamagotchi.hygiene), font=('Helvetica', 12))
hygieneLabel.pack()

# Add buttons
btnFeed = Button(root, text="Feed", command=lambda:tamagotchi.feed() & GameOn())    # Messy lambda
btnFeed.pack(side=LEFT, padx=30, pady=5)
btnClean = Button(root, text="Clean", command=lambda:tamagotchi.clean() & GameOn())
btnClean.pack(side=LEFT, padx=30, pady=5)
btnPlay = Button(root, text="Play", command=lambda:tamagotchi.play() & GameOn())
btnPlay.pack(side=LEFT, padx=30, pady=5)
btnToilet = Button(root, text="Toilet", command=lambda:tamagotchi.toilet() & GameOn())
btnToilet.pack(side=LEFT, padx=30, pady=5)
if not tamagotchi.wired:
    btnNap = Button(root, text="Nap", command=lambda:tamagotchi.nap() & GameOn())
    btnNap.pack(side=LEFT, padx=30, pady=5)

# Start the GUI
root.mainloop()
