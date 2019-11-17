# ******************************************************
#
# The Music Quiz by Joshua Heng
# This is the main file that must be run to start the game
# Note that all other python files in this directory must be accessible
#
# You can register your own account and use the 'AuthoriseAccount.py' file
# to authorise it on the server
#
# ******************************************************

#Import libraries
import gui, network, variables, game, auth, end
import time

#Called to start the game
def Start():
    #Init variables
    variables.init()

    #Create the window
    variables.window = gui.Window()

    #Get songs
    variables.songs = network.GetSongs()

    #Authenticate
    auth.Authenticator(StartGame)

#Called to start the actual game after authentication
def StartGame():
    #Reset the game variables
    variables.ResetGame()
    variables.songs = network.GetSongs()

    #Start the game instance
    global gameInstance
    gameInstance = game.Game(GameFinished)

#Called when the game is finished
def GameFinished(won = False):
    #Delete the game instance
    global gameInstance
    gameInstance.Close()
    del gameInstance

    #Start the end instance
    global endInstance
    endInstance = end.End(Restart, LogOut, Quit, won)

#Delete the end instance
def CloseEndInstance():
    global endInstance
    endInstance.Close()
    del endInstance
    
#Restarts the game
def Restart():
    CloseEndInstance()
    variables.window.CloseGUI()
    variables.window = gui.Window()
    StartGame()

#Logs out of the game
def LogOut():
    CloseEndInstance()
    variables.window.CloseGUI()
    Start()

#Quits the game
def Quit():
    CloseEndInstance()
    variables.window.CloseGUI()

#Start the game
Start()

#Start the GUI infinite loop
variables.window.window.mainloop()
