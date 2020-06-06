# Tic Tac Toe by Pic7oR
from tkinter import *
import tkinter.font as font

root = Tk()
# Font

new_font = font.Font(size=9, weight='bold')

# Functions

root.counter = 0

def clear(entry):
    button_1['text'] = " "
    button_2['text'] = "  "

    button_3['text'] = "   "
    button_4['text'] = "    "
    button_5['text'] = "     "
    button_6['text'] = "      "
    button_7['text'] = "       "
    button_8['text'] = "        "
    button_9['text'] = "         "
    entry.destroy()
    for j in (button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9):
        j.config(state=NORMAL, bg="#0052cc")
    root.counter = 0

def win_check():
    if button_1["text"] == button_2['text'] == button_3['text'] or button_1['text'] == button_4['text'] == button_7['text'] or button_1['text'] == button_5['text'] == button_9['text'] or button_2['text'] == button_4['text'] == button_7['text'] or button_4['text'] == button_5['text'] == button_6['text'] or button_7['text'] == button_8['text'] == button_9['text'] or button_3['text'] == button_6['text'] == button_9['text'] or button_3['text'] == button_5['text'] == button_7['text']:
        entry_display = Entry(root)
        entry_display.grid(row=0, column=0)
        entry_display.insert(END, "We have a WINNER!!!")
        button_clear = Button(root, text="New Game?", command= lambda: clear(entry_display))
        button_clear.grid(row=0, column=2)
        for j in (button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9):
            j.config(state= DISABLED, bg="red")


def x_and_o_1():
    root.counter += 1
    if root.counter % 2 == 0:
        button_1['text'] = "O"
    else:
        button_1['text'] = "X"
    win_check()

def x_and_o_2():
    root.counter += 1
    if root.counter % 2 == 0:
        button_2['text'] = "O"
    else:
        button_2['text'] = "X"
    win_check()

def x_and_o_3():
    root.counter += 1
    if root.counter % 2 == 0:
        button_3['text'] = "O"
    else:
        button_3['text'] = "X"
    win_check()

def x_and_o_4():
    root.counter += 1
    if root.counter % 2 == 0:
        button_4['text'] = "O"
    else:
        button_4['text'] = "X"
    win_check()

def x_and_o_5():
    root.counter += 1
    if root.counter % 2 == 0:
        button_5['text'] = "O"
    else:
        button_5['text'] = "X"
    win_check()

def x_and_o_6():
    root.counter += 1
    if root.counter % 2 == 0:
        button_6['text'] = "O"
    else:
        button_6['text'] = "X"
    win_check()

def x_and_o_7():
    root.counter += 1
    if root.counter % 2 == 0:
        button_7['text'] = "O"
    else:
        button_7['text'] = "X"
    win_check()

def x_and_o_8():
    root.counter += 1
    if root.counter % 2 == 0:
        button_8['text'] = "O"
    else:
        button_8['text'] = "X"
    win_check()

def x_and_o_9():
    root.counter += 1
    win_check()
    if root.counter % 2 == 0:
        button_9['text'] = "O"
    else:
        button_9['text'] = "X"
    win_check()

# Buttons

button_1 = Button(root, text=" ",height = 20, width = 40, command=x_and_o_1, bg='#0052cc', fg='#ffffff')
button_2 = Button(root, text="  ",height = 20, width = 40, command=x_and_o_2, bg='#0052cc', fg='#ffffff')
button_3 = Button(root, text="   ",height = 20, width = 40, command=x_and_o_3, bg='#0052cc', fg='#ffffff')

button_4 = Button(root, text="    ",height = 20, width = 40, command=x_and_o_4, bg='#0052cc', fg='#ffffff')
button_5 = Button(root, text="     ",height = 20, width = 40, command=x_and_o_5, bg='#0052cc', fg='#ffffff')
button_6 = Button(root, text="      ",height = 20, width = 40, command=x_and_o_6, bg='#0052cc', fg='#ffffff')

button_7 = Button(root, text="       ",height = 20, width = 40, command=x_and_o_7, bg='#0052cc', fg='#ffffff')
button_8 = Button(root, text="        ",height = 20, width = 40, command=x_and_o_8, bg='#0052cc', fg='#ffffff')
button_9 = Button(root, text="         ",height = 20, width = 40, command=x_and_o_9, bg='#0052cc', fg='#ffffff')
### Buttons on screen ###
button_1.grid(row=1 , column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2 , column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3 , column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

# Main Loop
root.mainloop()
