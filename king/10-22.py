from tkinter import * 
from tkinter.filedialog import * 

def func_open():
    filename = askopenfilename(parent = window, filetypes = (("GIF file", "*.gif"), ("all files", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def func_exit():
    window.quit()
    window.destroy()
    
window = Tk()
window.geometry("400x400")
window.title("appreciate famouse painting")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "file", menu = fileMenu)
fileMenu.add_command(label = "file open", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "end program", command = func_exit)

window.mainloop()