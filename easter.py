#-------------------------------------------------------------------------------
# Name:   easter.py     
# Purpose: Entertainment 
#
# Author:      BH0
#
# Created:     15/04/2017
# Copyright:   (c) User 2017
# Licence:     <so far, none>
#-------------------------------------------------------------------------------

# Open File (which stores the shape)
file = open("easter0.txt", "w")

def closeFile():
    file.close()

# Global Variables
num_of_shapes = 2

# Draw Shape/s
def drawEgg():
    file.write(" ..... ")
    file.write("........ ")
    file.write("..........")
    file.write("........")
    file.write(" ......")
    file.write("  ...")
    file.write("Happy Easter, egg goes here")

def drawBunny():
    file.write("Happy Easter, bunny goes here")

def drawChick():
    file.write("Happy Easter, chick goes here")

# Choose Random Shape
import random
def chooseRandomShape():
    randomShape = random.randint(0, num_of_shapes)

    egg = 0
    bunny = 1
    chick = 2

    if randomShape == egg:
        drawEgg()
    elif randomShape == bunny:
        drawBunny()
    elif randomShape == chick:
        drawChick()
    else:
        file.write("Sorry shape unknown, this is likely an error.")


# Call Main
def main():
    chooseRandomShape()
    closeFile()

if __name__ == '__main__':
    main()

