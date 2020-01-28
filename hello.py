from tkinter import *
import sys

window = Tk()
window.title("my OS")
window.geometry("200x100")
myos = sys.platform
app = Frame(window)
app.grid()

w = Label(app, text=str(myos),font=("Courier", 20))
w.grid(padx=50, pady=50)


window.mainloop()
