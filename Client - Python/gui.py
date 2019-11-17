# ******************************************************
#
# The GUI module provides classes for the user interfaces
#
# ******************************************************

#Import libraries
from tkinter import *
import variables

#
# The Window class provides the overall GUI window
#
class Window:
    #Construct the window
    def __init__(self):
        self.window = Tk()
        self.window.title("Music Quiz")

    def CloseGUI(self):
        self.window.destroy()

#
# The Authenticate class provides the GUI for authentication
#
class Authenticate:
    #Construct the GUI
    def __init__(self, loginCallback, registerCallback):
        #Assign local variables
        self.width = 500
        self.height = 500
        self.colour = "floral white"
        self.fontTitle = ("verdana", 20)
        self.font = ("verdana", 13)
        self.label = ("verdana", 8)

        self.loginCallback = loginCallback
        self.registerCallback = registerCallback

        #Create canvas & window
        self.canvas = Canvas(variables.window.window, bg=self.colour, height=self.height, width=self.width)
        self.canvas.grid()

        label = Label(self.canvas, text="Music Quiz Game", font=self.fontTitle, bg=self.colour)
        label.grid(row=1, columnspan=2)
        label = Label(self.canvas, text="Welcome to the music quiz!", font=self.font, bg=self.colour)
        label.grid(row=2, columnspan=2)
        
        self.statusLabel = Label(self.canvas, text="Please authenticate to continue", font=self.label, bg=self.colour, width=40)
        self.statusLabel.grid(row=3, columnspan=2)

        line = Frame(self.canvas, height=1, width=200, bg="grey")
        line.grid(row=4, columnspan=2, pady=10)

        self.loginFrame = Frame(self.canvas, bg=self.colour)
        self.loginFrame.grid(row=5, columnspan=2)

        self.SetUpLogin()
        
    #Called when the login button is pressed on the login screen - attempts login
    def Login_LoginButtonPressed(self):
        self.loginCallback(self.username.get(), self.password.get())

    #Called when the register button is pressed on the register screen - sets up the registration window
    def Login_RegisterButtonPressed(self):
        self.SetUpRegister()

    #Called if the password entered was invalid - notifies the user
    def InvalidPassword(self):
        self.username.set("")
        self.password.set("")

        self.statusLabel.config(text="Invalid credentials - please try again")
        self.statusLabel.config(fg="red")

    #Called if the account was not authorised - notifies the user
    def AccountNotAuthorised(self):
        self.password.set("")

        self.statusLabel.config(text="Your account has not been authorised")
        self.statusLabel.config(fg="red")

    #Sets up the login window
    def SetUpLogin(self):
        self.ClearLoginFrame()

        self.statusLabel.config(text="Please authenticate to continue")
        self.statusLabel.config(fg="black")

        self.username = StringVar()
        self.password = StringVar()

        label = Label(self.loginFrame, text="Username", font=self.label, bg=self.colour)
        self.fieldUsername = Entry(self.loginFrame, textvariable=self.username)

        label.grid(row=1, column=0, sticky=E)
        self.fieldUsername.grid(row=1, column=1, sticky=W)

        label = Label(self.loginFrame, text="Password", font=self.label, bg=self.colour)
        self.fieldPassword = Entry(self.loginFrame, textvariable=self.password, show="*")

        label.grid(row=2, column=0, sticky=E)
        self.fieldPassword.grid(row=2, column=1, sticky=W)

        buttonFrame = Frame(self.loginFrame, bg=self.colour)
        buttonFrame.grid(row=3, columnspan=2, pady=5)

        
        self.loginButton = Button(buttonFrame, text="Login", command=self.Login_LoginButtonPressed)
        self.registerButton = Button(buttonFrame, text="Register", command=self.Login_RegisterButtonPressed)

        self.loginButton.grid(row=0, column=0)
        self.registerButton.grid(row=0, column=1)

    #Called when the login button is pressed in the register window
    def Register_LoginButtonPressed(self):
        self.SetUpLogin()

    #Called when the register button is pressed in the register window
    def Register_RegisterButtonPressed(self):
        self.registerCallback(self.username.get(), self.password.get(), self.password2.get())

    #Sets up the registration window
    def SetUpRegister(self):
        self.ClearLoginFrame()

        self.statusLabel.config(text="Register an account")
        self.statusLabel.config(fg="black")

        self.username = StringVar()
        self.password = StringVar()
        self.password2 = StringVar()

        label = Label(self.loginFrame, text="Username", font=self.label, bg=self.colour)
        self.fieldUsername = Entry(self.loginFrame, textvariable=self.username)

        label.grid(row=1, column=0, sticky=E)
        self.fieldUsername.grid(row=1, column=1, sticky=W)

        label = Label(self.loginFrame, text="Password", font=self.label, bg=self.colour)
        self.fieldPassword = Entry(self.loginFrame, textvariable=self.password, show="*")

        label.grid(row=2, column=0, sticky=E)
        self.fieldPassword.grid(row=2, column=1, sticky=W)

        label = Label(self.loginFrame, text="Confirm Password", font=self.label, bg=self.colour)
        self.fieldPassword2 = Entry(self.loginFrame, textvariable=self.password2, show="*")

        label.grid(row=3, column=0, sticky=E)
        self.fieldPassword2.grid(row=3, column=1, sticky=W)

        buttonFrame = Frame(self.loginFrame, bg=self.colour)
        buttonFrame.grid(row=4, columnspan=2, pady=5)

        
        self.registerButton = Button(buttonFrame, text="Register", command=self.Register_RegisterButtonPressed)
        self.loginButton = Button(buttonFrame, text="Login", command=self.Register_LoginButtonPressed)

        self.registerButton.grid(row=0, column=0)
        self.loginButton.grid(row=0, column=1)

    #Called if there were errors in the registration data - notifies the user
    def InvalidRegistration(self, message):
        self.password.set("")
        self.password2.set("")

        self.statusLabel.config(text=message)
        self.statusLabel.config(fg="red")

    #Sets up the registration confirmation window
    def SetUpRegisterConfirm(self):
        self.ClearLoginFrame()
        
        self.statusLabel.config(text="Registration successful")
        self.statusLabel.config(fg="black")

        label = Label(self.loginFrame, text="Please wait for your account to be validated", font=self.label, bg=self.colour)
        label.grid(row=0, column=0, sticky=E)

        buttonFrame = Frame(self.loginFrame, bg=self.colour)
        buttonFrame.grid(row=4, columnspan=2, pady=5)

        self.loginButton = Button(buttonFrame, text="Login", command=self.Register_LoginButtonPressed)
        self.loginButton.grid(row=1, column=1, columnspan=2)

    #Clears the login frame
    def ClearLoginFrame(self):
        children = self.loginFrame.winfo_children()
        for child in children:
            child.destroy()

    #Closes the authenticator window
    def Close(self):
        self.canvas.destroy()
        del self

        
#
# The Game class provides the GUI for the main game
#
class Game():
    #Construct the GUI
    def __init__(self, submitCallback):
        self.width = 500
        self.height = 500
        self.colour = "floral white"
        self.fontTitle = ("verdana", 18)
        self.font = ("verdana", 13)
        self.label = ("verdana", 8)

        self.letterInputsStringVar = []
        self.letterInputsEntry = []

        self.submitCallback = submitCallback

        self.canvas = Canvas(variables.window.window, bg=self.colour, height=self.height, width=self.width)
        self.canvas.grid()

        self.songLabel = Label(self.canvas, text="Song 1", font=self.fontTitle, bg=self.colour)
        self.songLabel.grid(sticky="W", rowspan=2, pady=10, padx=10)

        self.usernameLabel = Label(self.canvas, text=variables.user['username'], font=self.label, bg=self.colour, width=20)
        self.usernameLabel.grid(row=0, column=1, sticky="E", padx=5)

        self.scoreLabel = Label(self.canvas, text="Score: 0", font=self.label, bg=self.colour, width=20)
        self.scoreLabel.grid(row=1, column=1, sticky="E", padx=5)

        self.statusLabel = Label(self.canvas, text="", font=self.label, bg=self.colour, width=40)
        self.statusLabel.grid(columnspan=2)

        line = Frame(self.canvas, height=1, width=200, bg="grey")
        line.grid(columnspan=2, pady=10)

        self.songArtistLabel = Label(self.canvas, bg=self.colour, font=self.font, text="")
        self.songArtistLabel.grid(columnspan=2)

        self.songTitleFrame = Frame(self.canvas, bg=self.colour, width=300)
        self.songTitleFrame.grid(columnspan=2)

        bottomButtons = Frame(self.canvas, height=1, width=300, bg=self.colour)
        bottomButtons.grid(columnspan=2)

        self.resetButton = Button(bottomButtons, text="Reset", command=self.ResetLetterInputs)
        self.resetButton.grid(pady=7, column=0, row=0, padx=5, sticky="E")
        self.submitButton = Button(bottomButtons, text="Submit", command=self.SubmitAnswer)
        self.submitButton.grid(pady=7, column=1, row=0, padx=5, sticky="W")

        
    #Called to show a new song  
    def SetSong(self, artist, title):
        #Sets up a song in the game
        def ValidateSongLetter(letterid, unneeded, unneeded2):
            #Called after a letter is entered

            #Get the letter id
            letterid = int(letterid[6:len(letterid)])

            #Get the letter value
            lettervalue = self.letterInputsStringVar[letterid].get()

            #If the length of the letter is more than one, set it to just the last letter
            if (len(lettervalue) > 1):
                self.letterInputsStringVar[letterid].set(lettervalue[len(lettervalue)-1])

            #If the length of the letter is more than 0, move focus to the next box
            if (len(lettervalue) > 0):
                if (len(self.letterInputsEntry) > letterid + 1):
                    self.letterInputsEntry[letterid + 1].focus()

        #Sets the artist label
        self.songArtistLabel['text'] = artist

        #Remove old song title
        for item in self.songTitleFrame.winfo_children():
            item.destroy()

        #Remove old entry boxes
        for item in self.letterInputsStringVar:
            for trace in item.trace_vinfo():
                item.trace_vdelete(trace[0], trace[1])
            del item
        for item in self.letterInputsEntry:
            item.destroy()
            
        #Creates entry boxes
        column = 0
        letterid = 0
        self.letterInputsStringVar = []
        self.letterInputsEntry = []
        #For each character in the title
        for letter in title:
            #If the character is a space, leave a space label
            if (letter == " "):
                label = Label(self.songTitleFrame, text=" ", height=1, width=1, bg=self.colour)
                label.grid(row=0, column=column)

            #If the character is NOT unknown, leave the character label
            elif (letter != "_"):
                label = Label(self.songTitleFrame, text=letter, height=1, width=1, bg=self.colour)
                label.grid(row=0, column=column)

            #If the character is unknown, leave an entry box
            else:
                stringVar = StringVar(name="letter" + str(letterid))
                #Call ValidateSongLetter whenever a letter is added
                stringVar.trace_variable("w", ValidateSongLetter)
                
                entry = Entry(self.songTitleFrame, textvariable=stringVar, width=2, bg=self.colour, justify="center")
                entry.grid(row=0, column=column)

                self.letterInputsStringVar.append(stringVar)
                self.letterInputsEntry.append(entry)

                letterid += 1
            
            column += 1

        #Reset inputs
        self.ResetLetterInputs()

    #Called to submit an answer
    def SubmitAnswer(self):
        answer = []
        for stringVar in self.letterInputsStringVar:
            answer.append(stringVar.get())
            
        self.submitCallback(answer)
        
    #Called to reset the user's input
    def ResetLetterInputs(self):
        for stringVar in self.letterInputsStringVar:
            stringVar.set("")
        self.letterInputsEntry[0].focus()

    #Called to set the status in the middle of the window (e.g. try again)
    def SetStatus(self, string, colourid = 0):
        if (colourid == 0):
            colour = "black"
        elif (colourid == 1):
            colour = "red"
        elif (colourid == 2):
            colour = "green"

        self.statusLabel['text'] = string
        self.statusLabel['fg'] = colour

    #Called to update the data in the top right of the window (e.g. score, etc.)
    def UpdateData(self):
        self.scoreLabel['text'] = "Score: " + str(variables.score)
        self.songLabel['text'] = "Song " + str(variables.songNumber)

    #Called to close
    def Close(self):
        self.canvas.destroy()
        del self

#
# The GameOver class provides the GUI for the end of the game
#
class GameOver():
    #Construct the GUI
    def __init__(self, restartCallback, logOutCallback, quitCallback, won = False):
        self.width = 500
        self.height = 500
        self.colour = "floral white"
        self.fontTitle = ("verdana", 18)
        self.font = ("verdana", 13)
        self.label = ("verdana", 10)
        self.fontBold = "verdana 9 bold"
        self.fontSmall = ("verdana", 8)

        self.restartCallback = restartCallback
        self.logOutCallback = logOutCallback
        self.quitCallback = quitCallback
        
        self.canvas = Canvas(variables.window.window, bg=self.colour, height=self.height, width=self.width)
        self.canvas.grid()

        label = Label(self.canvas, text="Music Quiz Game", font=self.fontTitle, bg=self.colour)
        label.grid(row=1, columnspan=3)
        label = Label(self.canvas, text="Thanks for playing the music quiz!", font=self.font, bg=self.colour)
        label.grid(row=2, columnspan=3)

        if (won):
            message = "Game Win"
        else:
            message = "Game Over"

        label = Label(self.canvas, text=message, font=self.label, bg=self.colour, width=40)
        label.grid(row=3, columnspan=3)

        label = Label(self.canvas, text="Name: " + variables.user['username'], bg=self.colour, font=self.fontSmall)
        label.grid(column=0, row=4, columnspan=3)

        label = Label(self.canvas, text="Score: " + str(variables.score), bg=self.colour, font=self.fontSmall)
        label.grid(column=0, row=5, padx=5)

        self.highscoreLabel = Label(self.canvas, text="Highscore: Error", bg=self.colour, font=self.fontSmall)
        self.highscoreLabel.grid(column=1, row=5, padx=5)

        self.rankLabel = Label(self.canvas, text="Rank: Error", bg=self.colour, font=self.fontSmall)
        self.rankLabel.grid(column=2, row=5, padx=5)

        if (won):
            label = Label(self.canvas, text="Songs: " + str(variables.songNumber), bg=self.colour, font=self.fontSmall)
            label.grid(column=0, row=6, columnspan=3)
        else:
            label = Label(self.canvas, text="Song: " + str(variables.songNumber), bg=self.colour, font=self.fontSmall)
            label.grid(column=0, row=6)

            text = variables.songs[variables.songNumber-1][0]+ " - " + variables.CapitaliseName(variables.songs[variables.songNumber-1][1])
            label = Label(self.canvas, text=text, bg=self.colour, font=self.fontSmall)
            label.grid(column=1, row=6, columnspan=2)

        line = Frame(self.canvas, height=1, width=200, bg="grey")
        line.grid(row=7, columnspan=3, pady=10)

        self.leaderboardFrame = Frame(self.canvas, bg=self.colour)
        self.leaderboardFrame.grid(row=8, columnspan=3)

        self.resetButton = Button(self.canvas, text="Restart", command=self.Restart)
        self.resetButton.grid(pady=7, column=0, row=9, sticky="E")
        self.resetButton = Button(self.canvas, text="Log Out", command=self.LogOut)
        self.resetButton.grid(pady=7, column=1, row=9)
        self.submitButton = Button(self.canvas, text="Quit", command=self.Quit)
        self.submitButton.grid(pady=7, column=2, row=9, sticky="W")

    #Called to update the highscores list
    def ShowHighscores(self, highscores):
        label = Label(self.leaderboardFrame, text="Rank", bg=self.colour, font=self.fontBold)
        label.grid(column=0, row=0)
        label = Label(self.leaderboardFrame, text="Username", bg=self.colour, font=self.fontBold)
        label.grid(column=1, row=0)
        label = Label(self.leaderboardFrame, text="Score", bg=self.colour, font=self.fontBold)
        label.grid(column=2, row=0)
            
        row = 1
        for highscore in highscores:
            label = Label(self.leaderboardFrame, text=str(highscore[0]), bg=self.colour, font=self.fontSmall)
            label.grid(column=0, row=row)
            label = Label(self.leaderboardFrame, text=highscore[1], bg=self.colour, font=self.fontSmall)
            label.grid(column=1, row=row)
            label = Label(self.leaderboardFrame, text=str(highscore[2]), bg=self.colour, font=self.fontSmall)
            label.grid(column=2, row=row)

            row += 1

    #Called to set the player info (e.g. rank, highscore)
    def SetPlayerData(self, playerData):
        self.rankLabel['text'] = "Rank: " + str(playerData[0])
        self.highscoreLabel['text'] = "Highscore: " + str(playerData[2])

    #Restarts the game
    def Restart(self):
        self.restartCallback()

    #Logs out of the game
    def LogOut(self):
        self.logOutCallback()

    #Quits the game
    def Quit(self):
        self.quitCallback()

    #Closes the canvas
    def Close(self):
        self.canvas.destroy()
        del self
