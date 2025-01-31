################################################################
# appName: Telefonbuch
# Author:  Joshua Phu Bein
# Contact:  https:\\phuonline.de\
# Description: This App is for everyone who needs a Phonebook
################################################################

################################################################
#                  Main - Script (app.py)                      #
################################################################
import users
import types
## Initializing Script
placeholderWelcome = "##########"
placeholderWelcomeName = "Willkommen zur meiner TelefonbuchApp"
## Ausagabe Intial Script
welcomeString = placeholderWelcome + " " + placeholderWelcomeName + " " + placeholderWelcome
endString = "© Joshua Phu Bein, 2019"

if __name__ == "__main__":
    print(welcomeString)
#    print(endString)
    # Eingabe UserID
    userID = int(input("Geben sie ihre id ein:  "))
#    print(endString)
    # Auslesen der Daten von users.py
    respName = users.getUsername(userID,1)
    respNumber = users.getNumber(userID,2)
    print(respName + " --> " + respNumber)
    print(endString)
    continueApp = input("Wollen Sie weitermachen? [y/n]:")
    if continueApp == "y":
        while continueApp == "y":
            userID = int(input("Geben sie ihre id ein:  "))
            if userID == users.getLength:
                respName = users.getUsername(userID, 1)
                respNumber = users.getNumber(userID, 2)
                print(respName + " --> " + respNum1ber)
                continueApp = input("Wollen Sie weitermachen? [y/n]:")
            else: print(endString)
        else:
            print(endString)
    else:
        print(endString)
