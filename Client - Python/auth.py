# ******************************************************
#
# The Auth module provides classes for handling authentication
#
# ******************************************************

#Import libraries
import variables, gui, network

#
# The Authenticator class provides the authentication workflow
#
class Authenticator:
    #Construst the class and create the GUI
    def __init__(self, gameCallback):
        self.gameCallback = gameCallback
        self.ShowLogin()

    #Show the login window
    def ShowLogin(self):
        #Initialise the authentication window
        self.authenticateGui = gui.Authenticate(self.AttemptLogin, self.AttemptRegistration)

    #Check that the password meets the minimum criteria
    def CheckPassword(self, password):
        uppercase = False
        lowercase = False
        number = False

        for letter in password:
            if (letter.isdigit()):
                number = True
            if (letter.islower()):
                lowercase = True
            if (letter.isupper()):
                uppercase = True

        if not uppercase:
            return "Password must contain an uppercase character"
        elif not lowercase:
            return "Password must contain a lowercase character"
        elif not number:
            return "Password must contain a number"
        else:
            return "good"
            
    #Attempt a user login
    def AttemptLogin(self, username, password):
        #First make sure length requirements are met
        if (len(username) > 4 and len(password) > 7):
            username = username.lower()

            variables.user = network.AttemptLogin(username, password)

            if (variables.user != None):
                if (variables.user['authorised']):
                    self.authenticateGui.Close()
                    self.gameCallback()
                else:
                    self.authenticateGui.AccountNotAuthorised()
            else:
                self.authenticateGui.InvalidPassword()
        else:
            self.authenticateGui.InvalidPassword()

    #Attempt a user registration
    def AttemptRegistration(self, username, password, password2):
        if (password != password2):
            self.authenticateGui.InvalidRegistration("Passwords do not match")
        else:
            if (len(password) < 8):
                self.authenticateGui.InvalidRegistration("Password must be at least 8 characters")
            else:
                if (len(password) > 32):
                    self.authenticateGui.InvalidRegistration("Maximum password length is 32 characters")
                else:
                    passwordResult = self.CheckPassword(password)
                    if (passwordResult != "good"):
                        self.authenticateGui.InvalidRegistration(passwordResult)
                    else:
                        if (len(username) < 5):
                            self.authenticateGui.InvalidRegistration("Username must be at least 5 characters")
                        else:
                            if (len(username) > 32):
                                self.authenticateGui.InvalidRegistration("Maximum username length is 32 characters")
                            else:
                                self.Register(username, password)
                                
    #Register a user
    def Register(self, username, password):
        username = username.lower()
            
        result = network.AttemptRegistration(username, password)
        
        if (result == "good"):
            self.authenticateGui.SetUpRegisterConfirm()
        else:
            self.authenticateGui.InvalidRegistration(result)

