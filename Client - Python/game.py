# ******************************************************
#
# The Game module provides the game workflow
#
# ******************************************************

#Import libraries
import variables, gui

#
# The Game class provides the game workflow
#
class Game:
    def __init__(self, gameFinishedCallback):
        #Initialise window
        self.gui = gui.Game(self.CheckAnswer)

        self.gameFinishedCallback = gameFinishedCallback

        self.GameRound()

    #Check a user answer
    def CheckAnswer(self, answer):
        letterid = 0
        correct = True

        #See if each letter matches
        for letter in answer:
            if (letter != self.answers[letterid]):
                correct = False
            letterid += 1

        #If answer is correct, move to next round and add points
        if correct:
            if (self.firstAttempt): points = 3
            else: points = 1

            pointsAbbreviation = "pts"
            if (points > 1): pointsAbbreviation = "pt"
                
            self.gui.SetStatus("Correct! " + str(points) + pointsAbbreviation, 2)

            variables.score += points

            if (variables.songNumber < len(variables.songs)):
                self.GameRound()
                self.gui.ResetLetterInputs()
            else:
                self.gameFinishedCallback(False)
        #If answer is incorrect, offer a second chance then finish the game
        else:
            if (self.firstAttempt):
                self.gui.SetStatus("Incorrect - second chance", 1)
                self.firstAttempt = False
                self.gui.ResetLetterInputs()
            else:
                self.gameFinishedCallback(False)
            
    #Called to start a game round
    def GameRound(self):
        variables.songNumber += 1
        self.firstAttempt = True

        self.gui.UpdateData()
        
        self.song = variables.songs[variables.songNumber-1]
        encodedName = self.EncodeSongName(self.song[1])

        self.gui.SetSong(self.song[0], encodedName)

    #Encodes a song name into the GUI format
    def EncodeSongName(self, songName):
        answers = []
        
        name = ""
        firstLetter = True
        for letter in songName:
            #Shows the first letter of each word as a capital
            if (firstLetter):
                name += letter.upper()
                firstLetter = False
            #If whitespace, keep it and start a new word
            elif (letter == " "):
                firstLetter = True
                name += " "
            #Otherwise hides the character with an underscore
            else:
                name += "_"
                answers.append(letter)
 
        self.answers = answers      
        return name

    #Close the game window
    def Close(self):
        self.gui.Close()
        del self
    
