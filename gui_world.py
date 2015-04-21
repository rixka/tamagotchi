from tkinter import *
from tama import Pet

tamagotchi = Pet()
max_age = 20
# -------------------------------------------------------------------


def GameOn():
    tamagotchi.update()
    updateDisplay()
# -------------------------------------------------------------------


def updateDisplay():

    if tamagotchi.age == max_age:
        startLabel.config(text="CONGRATULATIONS\n\n You Win!\n")
        return False

    # Update labels
    ageLabel.config(text="Age: {}".format(tamagotchi.age))
    healthLabel.config(text="Health: {}".format(tamagotchi.health))
    tirednessLabel.config(text="Tiredness: {}".format(tamagotchi.sleep))
    hungerLabel.config(text="Hunger: {}".format(tamagotchi.hunger))
    happinessLabel.config(text="Happiness: {}".format(tamagotchi.happy))
    bladderLabel.config(text="Bladder: {}".format(tamagotchi.bladder))
    hygieneLabel.config(text="Hygiene: {}\n". format(tamagotchi.hygiene))

    isAlive()
# -------------------------------------------------------------------


def isAlive():

    # Dead
    if tamagotchi.health <= 0:
        startLabel.config(text="GAME OVER! YOU KILLED IT!")
        return False
    else:
        startLabel.config(text="GAME ON!")
        return True
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
root.geometry("400x300")

logo = PhotoImage(file="images/happy.gif")


# Add labels
startLabel = Label(root, text="GAME ON!", font=('Helvetica', 12))
startLabel.grid(sticky=E, columnspan=4)
btnReset = Button(root, text="Reset", command=combine_funcs(tamagotchi.__init__, updateDisplay))
btnReset.grid(column=6, row=0)

ageLabel = Label(root, text="Age: " + str(tamagotchi.age), font=('Helvetica', 12))
ageLabel.grid(sticky=W, columnspan=2, row=2)
healthLabel = Label(root, text="Health: " + str(tamagotchi.health), font=('Helvetica', 12))
healthLabel.grid(sticky=W, columnspan=2, row=3)
tirednessLabel = Label(root, text="Tiredness: " + str(tamagotchi.sleep), font=('Helvetica', 12))
tirednessLabel.grid(sticky=W, columnspan=2, row=4)
hungerLabel = Label(root, text="Hunger: " + str(tamagotchi.hunger), font=('Helvetica', 12))
hungerLabel.grid(sticky=W, columnspan=2, row=5)
happinessLabel = Label(root, text="Happiness: " + str(tamagotchi.happy), font=('Helvetica', 12))
happinessLabel.grid(sticky=W, columnspan=2, row=6)
bladderLabel = Label(root, text="Bladder: " + str(tamagotchi.bladder), font=('Helvetica', 12))
bladderLabel.grid(sticky=W, columnspan=2, row=7)
hygieneLabel = Label(root, text="Hygiene: " + str(tamagotchi.hygiene), font=('Helvetica', 12))
hygieneLabel.grid(sticky=W, columnspan=2, row=8)

pet = Label(root, image=logo).grid(column=2, row=2, columnspan=5, rowspan=7, padx=5, pady=5)

# Add buttons
btnFeed = Button(root, text="Feed", command=combine_funcs(tamagotchi.feed, GameOn))
btnFeed.grid(column=2, row=10)
btnClean = Button(root, text="Clean", command=combine_funcs(tamagotchi.clean, GameOn))
btnClean.grid(column=3, row=10)
btnPlay = Button(root, text="Play", command=combine_funcs(tamagotchi.play, GameOn))
btnPlay.grid(column=4, row=10)
btnToilet = Button(root, text="Toilet", command=combine_funcs(tamagotchi.toilet, GameOn))
btnToilet.grid(column=5, row=10)
if not tamagotchi.wired:
    btnNap = Button(root, text="Nap", command=combine_funcs(tamagotchi.nap, GameOn))
    btnNap.grid(column=6, row=10, rowspan=2)

# Start the GUI
root.mainloop()