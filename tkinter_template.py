#GUI
from tkinter import *

app = Tk()
app.title("Your tkinter application")
app.geometry("450x100+200+100")


b1 = Button(app, text = "Click me!", width = 10)
b1.pack()




app.mainloop()
