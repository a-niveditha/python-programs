from tkinter import *
#import class02  # handle SQLDB
#import class03  # handle Files

# create root window
root = Tk()

# root.title("hello workld - wordle")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.state("zoomed")


# GEOMETRY SIZE  - HORIZ * VERTICAL IN PIXEL
# root.geometry('800x600')
# function to show a frame
def show_frame(frame):
    frame.tkraise()


frame2 = Frame(root, bg='black')
frame2.grid(row=0, column=0, sticky="nsew")
frame2_title = Label(frame2, text=" WORDLE", bg="black", fg='#4ad0e8', font='georgia 36 bold')
frame2_title.place(x=460, y=10)

attempt = 0
GREEN = "#007d21"
YELLOW = "#e2e600"
BLACK = "#000000"
WHITE = "#f5e4df"
GREY = "#505050"
LGREY = "#808080"

r1 = 0
# title
# label_1=Label(root,text="Welcome to WORDLE")
# label_1.place(x=300,y=5)

r1 += 1
# take input
choice1 = Label(frame2, text="Guess the word [5 letters] : ", bg='black', fg='#4ad0e8', font='georgia 14')
choice1.place(x=5, y=75)
input1 = Entry(frame2, width=20)
input1.place(x=250, y=75)
btn1 = Button(frame2, text="Submit", bg='#fcd9c0', fg='#de3507', font='georgia 14')
btn1.place(x=475, y=75)
btn2 = Button(frame2, text="Return to main page", bg='#fcd9c0', fg='#de3507', font='georgia 14')
btn2.configure(command=lambda: show_frame(frame2))
btn2.place(x=575, y=75)

r1 += 1
# display output
selected = ['T','R','A','C','E']

# msg1 = Label(frame2,text = selected)
# msg1.place(x=5,y=480)
msg2 = Label(frame2)
msg2.place(x=300, y=460)
msg2.configure(bg='black', fg='black')

# set x,y to display each attempt
x1 = 50
y1 = 100

# set x,y for displaying keyboard
x2 = 200
y2 = 500
dict_keys = {}

def dispKB():
    global x2, y2, dict_keys

    # line 1 Q W E R T Y U I O P
    for ch in "QWERTYUIOP":
        label_1 = Label(frame2, text=ch)
        label_1.configure(bg=WHITE, fg=BLACK)
        label_1.place(height=50, width=50, x=x2, y=y2)
        dict_keys[ch] = (label_1, "WHITE")
        x2 += 52
    # 2nd line
    x2 = 225
    y2 = 552
    for ch in "ASDFGHJKL":
        label_1 = Label(frame2, text=ch)
        label_1.configure(bg=WHITE, fg=BLACK)
        label_1.place(height=50, width=50, x=x2, y=y2)
        dict_keys[ch] = (label_1, "WHITE")
        x2 += 52
    # 3rd line
    x2 = 275
    y2 = 604
    for ch in "ZXCVBNM":
        label_1 = Label(frame2, text=ch)
        label_1.configure(bg=WHITE, fg=BLACK)
        label_1.place(x=x2, y=y2, height=50, width=50)
        dict_keys[ch] = (label_1, "WHITE")
        x2 += 52

    return


def getGuess():
    global attempt, x1, y1, dict_keys

    inputword = input1.get().upper()
    print("get guess ", inputword)
    if len(inputword) != 5:
        msg2.configure(text="Please enter word of 5 characters", fg='#4ad0e8', font='georgia 16 bold')
        return

    attempt += 1
    print("attempt ", attempt)
    y1 += 52
    msg2.configure(text='', fg=BLACK, bg=BLACK)
    x1 = 50

    for i, letter in enumerate(inputword):
        x1 += 52
        label = Label(frame2, text=letter)
        label.place(height=50, width=50, x=x1, y=y1)
        if letter == selected[i]:  # if inputword[i] == selected[i]
            label.config(bg=GREEN, fg=YELLOW, font='georgia 10')
            (l1, c1) = dict_keys.get(letter)
            l1.configure(bg=GREEN, fg=YELLOW, font='georgia 10')
            dict_keys[letter] = (l1, "GREEN")

        if letter in selected and not letter == selected[i]:
            label.config(bg=YELLOW, fg=BLACK, font='georgia 10')
            (l1, c1) = dict_keys.get(letter)
            if c1 == "GREEN":
                pass
            else:
                l1.configure(bg=YELLOW, fg=BLACK)
                dict_keys[letter] = (l1, "YELLOW")

        if letter not in selected:
            label.config(bg=GREY, fg=WHITE, font='georgia 10')
            (l1, c1) = dict_keys.get(letter)
            l1.configure(bg=GREY, fg=WHITE)
            dict_keys[letter] = (l1, "BLACK")

    if inputword == selected:
        msg2.configure(text="Congrats, you have guessed it correct!!!", fg='#4ad0e8', font='georgia 16 bold')
        return

    if attempt >= 5:
        msg2.configure(text=f"Maximum attempts used, selected word is {selected}", fg='red', font='georgia 16')
        btn1.configure(state=DISABLED)
        return


btn1.configure(command=getGuess)

dispKB()

# execute tkinter
root.mainloop()
