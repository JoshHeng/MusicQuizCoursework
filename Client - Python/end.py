# ******************************************************
#
# The End module provides the code for the end of the game
#
# ******************************************************

#Import libraries
import variables, gui, network

#
# The End class handles the end of the game
#
class End:
    #Create the GUI
    def __init__(self, restartCallback, logOutCallback, quitCallback, won):
        self.gui = gui.GameOver(restartCallback, logOutCallback, quitCallback, won)

        self.SyncScores()

    #Sync the scores to get the leaderboard
    def SyncScores(self):
        scoresData = network.SyncScores(variables.user['token'], variables.score)
        
        self.gui.ShowHighscores(scoresData[0])
        self.gui.SetPlayerData(scoresData[1])

    #Close the class
    def Close(self):
        self.gui.Close()
        

