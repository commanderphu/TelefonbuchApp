################################################################
# appName: Telefonbuch
# Author:  Joshua Phu Bein
# Contact:  https:\\phuonline.de\
# Description: This App is for everyone who needs a Phonebook
################################################################

################################################################
#                  User - Function (users.py)                      #
################################################################
Users = [
 [0, "commanderphu", "0123456789"],
 [1, "Crankphoenix", "9876543210"],
]


def getUsername (i,u):
    name = Users[i][u]
    return name
def getID (i,u):
    id = Users[i][u]
    return id
def getNumber (i,u):
    number = Users[i][u]
    return number