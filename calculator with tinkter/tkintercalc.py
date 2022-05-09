from tkinter import *


# function to update expression
# in the text entry box
from urllib import error

import equation as equation
import top


def press(num):
    # globally declare expression variable
    expression = ""

    # concatenation of string
    expression + str(num)

    #update equation by expression by using set method
    equation.set(expression)

#function to evaluate the final expression
def equalpress ():
    # try and except statement is used
    #for handling errors like zero  and division errors
    try:
        global expression


        total = str(eval(expression))
        equation.set(total)

        expression = ""
    except:
        equation.set(error)
        expression = ""










top.mainloop()
