
from tkinter import *
from dictio import my_dictionary

#key down function
def click():
    entered_text=textentry.get() #this will collect the text from the text entry box
    output.delete(0.0, END)
    try:
        definition = my_dictionary[entered_text]
    except:
        definition = "sorry there is no word like that please try again"
    output.insert(END, definition)


#exit function
def close_window():
    window.destroy()
    exit()

def clear():
   output.delete(1.0,END)

#main
window = Tk()
window.title("UNIVERSSEL DICTIONARY")
window.configure(background="black")

# Set an image
photo = PhotoImage(file="c.png")
Label(window, image=photo, bg="black") .grid(row=0, column=0, sticky=E)

#create label
Label (window, text="Enter the word you would like a defenition for:", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)

#create a text entry
textentry = Entry(window, width=20, bg="white")
textentry.grid(row =2, column=0, sticky=W)

#add a submit button
Button(window, text="SUBMIT", width=6, command=click) .grid(row=3, column=0, sticky=W)

#create another label
Label (window, text="\nDefinition", bg="black", fg="white", font="none 12 bold") .grid(row=4, column=0, sticky=W)

#create a output text box
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)


#exit label
Label (window, text="Click to exit: ", bg="black", fg="white", font="none 12 bold") .grid(row=6, column=0, sticky=W)

#exit button
Button(window, text="EXIT", width=14, command=close_window) .grid(row=7, column=0, sticky=W)

Button(window, text="clear", width=6, command=clear) .grid(row=3, column=1, sticky=W)

##run the main loop
window.mainloop()