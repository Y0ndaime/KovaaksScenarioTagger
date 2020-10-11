# Scenario Tagger made by Yondaime#1370 on Discord
from tkinter import *
import random
from ScenarioReader import *

sent = 0  # Initialize sent for checks later, 0 = not submitted, 1 = submitted, 2 = not submitted but warning displayed
# Use the Scenario Reader Class to open the cache and get a list of all scenario names
sr = Scenreader
sr.opencache(sr, sr.getpath(sr))
scenarios = sr.createscenlist(sr, sr.opencache(sr, sr.getpath(sr)))

# Check if file with output exists, if not create it
pather = os.path
if pather.exists('output.txt'):  # Check if the file exists
    outputfile = open("output.txt", "a")
else:
    outputfile = open("output.txt", "w")

# Create window and title it
window = Tk()
window.geometry("369x560")
window.title("Kovaaks Scenario Randomizer")
frameabove = Frame(window)
frameabove.grid(row=0, column=0, columnspan=4)
framebelow = Frame(window)
framebelow.grid(row=11, column=0, columnspan=4, rowspan=2)
framebottom = Frame(window)
framebottom.grid(row=13, column=0, columnspan=4, rowspan=2)
frameresponse = Frame(window)
frameresponse.grid(row=15, column=0, columnspan=4, rowspan=5, sticky="w")

# Create label for errors
errorlabel = Label(framebottom, text="")
errorlabel.pack(side=BOTTOM)

# Create label for responses
responselabel = Label(frameresponse, text="", anchor=W, justify=LEFT)
responselabel.pack(fill="x")

# Create label with the current scenario and a pretext
precurrent = Label(frameabove, text="Current Scenario: ")
precurrent.pack(side="left")
scenarioname = StringVar(window)
assert len(scenarios) > 0, "You already created tags for all scenarios in your scenario.txt"
scenarioname.set(random.choice(scenarios))
window.clipboard_append(scenarioname.get())
currentscen = Label(frameabove, textvariable=scenarioname)
currentscen.pack(side="right")

# Create Dropdown with aimstyles and the variable aimtype which gets updated on selection and a label infront
typelabel = Label(window, text="Type:")
typelabel.grid(row=1, column=0)

optionsaimtype = [
    "Tracking",
    "Clicking",
    "Switching"
]
aimtype = StringVar(window)
aimtype.set(optionsaimtype[0])

optaimtype = OptionMenu(window, aimtype, *optionsaimtype)
optaimtype.config(width=10)
optaimtype.grid(row=1, column=1)

# Create Dropdown for Recommendation and variable recommended that gets updated on selection and a label infront
recommendedlabel = Label(window, text="Recommended:")
recommendedlabel.grid(row=1, column=2)

optionsrecommended = [
    "Yes",
    "No"
]
recommended = StringVar(window)
recommended.set(optionsrecommended[0])

optrecommended = OptionMenu(window, recommended, *optionsrecommended)
optrecommended.config(width="5")
optrecommended.grid(row=1, column=3)

# Create Dropdown for targetsize and variable targetsize that gets updated on selection and a label infront
targetsizelabel = Label(window, text="Targetsize:")
targetsizelabel.grid(row=2, column=0)

optionstargetsize = [
    "es",
    "s",
    "m",
    "l",
    "xl",
    "varying"
]
targetsize = StringVar(window)
targetsize.set(optionstargetsize[0])

opttargetsize = OptionMenu(window, targetsize, *optionstargetsize)
opttargetsize.config(width="10")
opttargetsize.grid(row=2, column=1)

# Create Dropdown for Dodge and variable dodge that gets updated on selection and a label infront
dodgelabel = Label(window, text="Dodge:")
dodgelabel.grid(row=2, column=2)

optionsdodge = [
    "Yes",
    "No"
]
dodge = StringVar(window)
dodge.set(optionsdodge[0])

optdodge = OptionMenu(window, dodge, *optionsdodge)
optdodge.config(width="5")
optdodge.grid(row=2, column=3)

# Create Dropdown for Targetspeed and variable targetspeed that gets updated on selection and a label infront
targetspeedlabel = Label(window, text="Targetspeed:")
targetspeedlabel.grid(row=3, column=0)

optionstargetspeed = [
    "static",
    "slow",
    "medium",
    "fast",
    "reflex",
    "varying"
]

targetspeed = StringVar(window)
targetspeed.set(optionstargetspeed[0])

opttargetspeed = OptionMenu(window, targetspeed, *optionstargetspeed)
opttargetspeed.config(width="10")
opttargetspeed.grid(row=3, column=1)

# Create Dropdown for HPRegen and variable regen that gets updated on selection and a label infront
regenlabel = Label(window, text="HP-Regeneration:")
regenlabel.grid(row=3, column=2)

optionsregen = [
    "Yes",
    "No"
]
regen = StringVar(window)
regen.set(optionsregen[0])

optregen = OptionMenu(window, regen, *optionsregen)
optregen.config(width="5")
optregen.grid(row=3, column=3)

# Create Dropdown for Botmovement and variable botmovement that gets updated on selection and a label infront
botmovementlabel = Label(window, text="Botmovement:")
botmovementlabel.grid(row=4, column=0)

optionsbotmovement = [
    "vertical",
    "horizontal",
    "arc",
    "mixed",
    "static"
]

botmovement = StringVar(window)
botmovement.set(optionsbotmovement[0])

optbotmovement = OptionMenu(window, botmovement, *optionsbotmovement)
optbotmovement.config(width="10")
optbotmovement.grid(row=4, column=1)

# Create Dropdown for Scenarioangle and variable angle that gets updated on selection and a label infront
anglelabel = Label(window, text="Angle:")
anglelabel.grid(row=4, column=2)

optionsangle = [
    "<=90°",
    "<=180°",
    ">180°"
]
angle = StringVar(window)
angle.set(optionsangle[0])

optangle = OptionMenu(window, angle, *optionsangle)
optangle.config(width="5")
optangle.grid(row=4, column=3)

# Create Dropdown for Weapontype and variable weapontype that gets updated on selection and a label infront
weapontypelabel = Label(window, text="Weapontype:")
weapontypelabel.grid(row=5, column=0, columnspan=1)

optionsweapontype = [
    "Hitscan",
    "Projectile"
]
weapontype = StringVar(window)
weapontype.set(optionsweapontype[0])

optweapontype = OptionMenu(window, weapontype, *optionsweapontype)
optweapontype.config(width="10")
optweapontype.grid(row=5, column=1, columnspan=1)

# Create Dropdown for Gauntlet and variable gauntlet that gets updated on selection and a label infront
gauntletlabel = Label(window, text="Gauntlet:")
gauntletlabel.grid(row=5, column=2, columnspan=1)

optionsgauntlet = [
    "Yes",
    "No"
]
gauntlet = StringVar(window)
gauntlet.set(optionsgauntlet[0])

optgauntlet = OptionMenu(window, gauntlet, *optionsgauntlet)
optgauntlet.config(width="5")
optgauntlet.grid(row=5, column=3, columnspan=1)

# Create Dropdown for Smoothness/Reactivity and variable resm that gets updated on selection and a label infront
resmlabel = Label(window, text="Reactivity/Smoothness:")
resmlabel.grid(row=6, column=0, columnspan=2)

optionsresm = [
    "none",
    "pure smoothness",
    "dominant smoothness",
    "mixed",
    "dominant reactivity",
    "pure reactivity"
]
resm = StringVar(window)
resm.set(optionsresm[0])

optresm = OptionMenu(window, resm, *optionsresm)
optresm.config(width="19")
optresm.grid(row=6, column=2, columnspan=2)

# Create Dropdown for speed and variable speed that gets updated on selection and a label infront
speedlabel = Label(window, text="Switchspeed:")
speedlabel.grid(row=8, column=0, columnspan=2)

optionsspeed = [
    "no switching",
    "no speed",
    "normal speed",
    "pure speed"
]
speed = StringVar(window)
speed.set(optionsspeed[0])

optspeed = OptionMenu(window, speed, *optionsspeed)
optspeed.config(width="19")
optspeed.grid(row=8, column=2, columnspan=2)

# Create Dropdown for perspective and variable perspective that gets updated on selection and a label infront
perspectivelabel = Label(window, text="Perspective:")
perspectivelabel.grid(row=9, column=0, columnspan=2)

optionsperspective = [
    "First Person",
    "Third Person"
]
perspective = StringVar(window)
perspective.set(optionsperspective[0])

optperspective = OptionMenu(window, perspective, *optionsperspective)
optperspective.config(width="19")
optperspective.grid(row=9, column=2, columnspan=2)

# Create Input for time and variable time and a label infront
timelabel = Label(window, text="Length:")
timelabel.grid(row=10, column=0, columnspan=2)

time = StringVar()

timeentry = Entry(window, textvariable=time)
time.set(60)
timeentry.grid(row=10, column=2, columnspan=2)


# Method to update the Scenario
def newscen():
    global sent  # Use the global sent to check if this scen was rated already
    if sent == 1 or sent == 2:  # If already submitted, or the warning was displayed, update the label with a random
        sent = 0  # choice from the scenario list
        errorlabel.config(text="")
        responselabel.config(text="")
        if len(scenarios) > 0:
            temp = random.choice(scenarios)  # Temporary Scenario name
            scenarioname.set(temp)
            window.clipboard_clear()
            window.clipboard_append(temp)  # Add to clipboard
        else:
            errorlabel.config(text="You already created tags for all Scenarios in the Scenario.txt")
    elif sent == 0:  # If not already submitted warn user
        errorlabel.config(text="You have not send your evaluation in,\nif you want to continue press the button again")
        sent = 2


# Create button for new scenario
newscenario = Button(framebelow, text="New Scenario", command=newscen)


# Method to create new row in table, for now it checks entries and prints them
def sendentry():
    global sent
    if sent == 1:  # Check that the evaluation was not sent in already
        errorlabel.config(text="You already sent in this evaluation.\nGet a new scenario first")
    elif sent == 0 or sent == 2:  # If not already sent
        if time.get().isdigit():  # Check if input for time is an integer
            output = "{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}\n"
            values = """The selected values are:\n
            Aimtype: {} | Recommendation: {} | Targetsize: {}\n
            Dodge: {} | Targetspeed: {} |Hp-Regeneration: {}\n
            Botmovement: {} | Angle: {}\n
            Weapontype: {} | Gauntlet: {}\n
            Smoothness/Reactivity: {} | Switchspeed: {}\n
            Perspective: {} | Length: {}"""
            if scenarioname.get() in scenarios:
                scenarios.remove(scenarioname.get())
            output = output.format(str(scenarioname.get()), aimtype.get(), recommended.get(), targetsize.get(),
                                   dodge.get(), targetspeed.get(), regen.get(), botmovement.get(), angle.get(),
                                   weapontype.get(), gauntlet.get(), resm.get(), speed.get(), perspective.get(),
                                   time.get())
            outputfile.write(output)
            sent = 1
            errorlabel.config(text="Your evaluation has been submitted")
            responselabel.config(
                text=values.format(aimtype.get(), recommended.get(), targetsize.get(),
                                   dodge.get(), targetspeed.get(), regen.get(), botmovement.get(), angle.get(),
                                   weapontype.get(), gauntlet.get(), resm.get(), speed.get(), perspective.get(),
                                   time.get()))
        else:
            errorlabel.config(text="Please input an whole positive number as length")


newscenario.pack(side=LEFT, fill="x")
# Create send button
sendbutton = Button(framebelow, text="Send", command=sendentry)
sendbutton.pack(side=LEFT, fill="x")

# Create exit button
exitbutton = Button(framebelow, text="Exit Program", command=window.quit)
exitbutton.pack(side=RIGHT, fill="x")

# Run gui
window.mainloop()

# Update Scenariolist
with open('scenarios.txt', 'w') as f:
    for item in scenarios:
        f.write("%s\n" % item)
f.close()

# Close connection file
outputfile.close()
