
# i have used Python in-built random
#module which gives the ability to
#generate a random integer with a given range()
import random
def script():
    #if user decides to Roll the Dice ..
    #The yes option will start the program
    start = raw_input("Would you like to Roll the Dice?(y/n)")

    if start == "yes" or start == "y" or start == 'Yes':

        print random.randint(1, 7)

        #after a random number has been printed in the stand out ...
        #if the user wants to Roll the Dice again he/she gets the y/n option here

        restart = raw_input("Would you like to Roll the Dice Again?(y/n)")
        if restart == "yes" or start == "y" or start == 'Yes':

            #on Rolling Again ... A random number is printed...

            print random.randint(1, 6)

            #to avoid quiting the program without users consent I called the dice() function
            #this prevent the program from stopping without users authority

            script()

        if restart == "n" or restart == "no" or restart == 'No':

            print "Thanks For Rolling the Dice:). Goodbye."

    #if the user decides to stop rolling the dice .
    #The n/no/No option quits the terminal input
    if start == "n" or start == "no" or start == 'No':
        print "Thank you :). Goodbye."
script()
# to initialize the funtion
