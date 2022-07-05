# vote favorite pet
from tkinter import *

## function declaration part ##
def myFunc():
    if var.get() == 1:
        labelImage.configure(image = photo1)
    elif var.get() == 2:
        labelImage.configure(image = photo2)
    else:
        labelImage.configure(image = photo3)
        
## global function declaration ##
var, labelImage = 0, None
photo1, photo2, photo3 = [None]*3

## main code part ##
if __name__ == "__main__":
    window = Tk()
    window.geometry("400x400")
    window.title("select pet")
    labelText = Label(window, text = "vote favorite animal", fg = "Red", font = ("궁서체", 20))
    
var = IntVar()
rb1 = Radiobutton(window, text = "dog", variable = var, value = 1)
rb2 = Radiobutton(window, text = "cat", variable = var, value = 2)
rb3 = Radiobutton(window, text = "rabbit", variable = var, value = 3)
buttonOk = Button(window, text = "see picture", command = myFunc)

photo1 = PhotoImage(file = "gif/dog3.gif")
photo2 = PhotoImage(file = "gif/cat.gif")
photo3 = PhotoImage(file = "gif/rabbit.gif")

labelImage = Label(window, width = 200, height = 200, bg = "blue", image = None)

labelText.pack(padx = 5, pady = 5)
rb1.pack(padx = 5, pady = 5)
rb2.pack(padx = 5, pady = 5)
rb3.pack(padx = 5, pady = 5)
buttonOk.pack(padx = 5, pady = 5)
labelImage.pack(padx = 5, pady = 5)

window.mainloop()