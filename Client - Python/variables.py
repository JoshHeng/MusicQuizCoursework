# ******************************************************
#
# The Variables module provides global variables and functions
#
# ******************************************************

#Initialise the variables
def init():
    global score
    global songNumber
    global user
    global songs
    global window

    score = 0
    songNumber = 0

    user = {}
    songs = []

    window = None

#Capitalises a song name
def CapitaliseName(uncapitalisedName):
    name = ""
    firstLetter = True
    for letter in uncapitalisedName:
        if (firstLetter):
            name += letter.upper()
            firstLetter = False
        elif (letter == " "):
            firstLetter = True
            name += " "
        else:
            name += letter.lower()
    return name

#Resets the game variables
def ResetGame():
    global score
    global songNumber
    global songs
    
    score = 0
    songNumber = 0
    songs = []
