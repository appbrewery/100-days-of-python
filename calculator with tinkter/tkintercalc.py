import tkinter as tk

calc = tk.Tk()
calc.title("CrappyCalc")

buttons = [
    '7', '8', '9', '*', 'C',
    '4', '5', '6', '/', 'Neg',
    '1', '2', '3', '-', '$',
    '0', '.', '=', '+', '@']

# set up GUI
row = 1
col = 0
for i in buttons:
    button_style = 'raised'
    action = lambda x=i: click_event(x)
    tk.Button(calc, text=i, width=7, height=7, relief=button_style, command=action) \
        .grid(row=row, column=col, sticky='nesw', )
    col += 1
    if col > 4:
        col = 0
        row += 1

display = tk.Entry(calc, width=40, bg="white")
display.grid(row=0, column=0, columnspan=5)


def click_event(key):
    # = -> calculate results
    if key == '=':
        # safeguard against integer division
        if '/' in display.get() and '.' not in display.get():
            display.insert(tk.END, ".0")

        # attempt to evaluate results
        try:
            result = eval(display.get())
            display.insert(tk.END, " = " + str(result))
        except:
            display.insert(tk.END, "   Error, use only valid chars")

    # C -> clear display
    elif key == 'C':
        display.delete(0, tk.END)


    # $ -> clear display
    elif key == '$':
        display.delete(0, tk.END)
        display.insert(tk.END, "$$$$C.$R.$E.$A.$M.$$$$")


    # @ -> clear display
    elif key == '@':
        display.delete(0, tk.END)
        display.insert(tk.END, "wwwwwwwwwwwwwwwwebsite")


    # neg -> negate term
    elif key == 'neg':
        if '=' in display.get():
            display.delete(0, tk.END)
        try:
            if display.get()[0] == '-':
                display.delete(0)
            else:
                display.insert(0, '-')
        except IndexError:
            pass

    # clear display and start new input
    else:
        if '=' in display.get():
            display.delete(0, tk.END)
        display.insert(tk.END, key)


# RUNTIME
calc.mainloop()
