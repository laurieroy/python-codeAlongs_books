#!/usr/local/bin/python3
"""Save text entered in fields to file. Messagebox showing user data. Clears text after save.
Exercise from headfirst book."""
from tkinter import *
from tkinter import messagebox

def save_data():
    fileD = open("deliveries.txt", "a")
    fileD.write("Depot:\n")
    fileD.write(depot.get())
    #fileD.write("%s\n" % depot.get())
    fileD.write("\nDescription:\n")
    fileD.write("%s\n" % description.get())
    fileD.write("Address:\n")
    fileD.write("%s\n" % address.get("1.0", END))
    depot.set(None)
    description.delete(0, 'end')
    address.delete(1.0, 'end')
    messagebox.showinfo(title="Head-Ex Deliveries Form", message="Order submitted!")
"""
def clear():
    description.delete(0, 'end')
    depot.delete(0, 'end')
    address.delete(1.0, 'end')
"""       
app = Tk()
app.title("Head-Ex Deliveries")
Label(app, text = "Depot:").pack()
depot = StringVar()
depot.set(None)
Radiobutton(app, text ="Cambridge, MA", value = "Cambridge, MA", variable = depot).pack()
Radiobutton(app, text ="Cambridge, UK", value = "Cambridge, UK", variable = depot).pack()
Radiobutton(app, text ="Seattle, WA", value = "Seattle, WA", variable = depot).pack()

Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()

Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

Button(app, text = "Save", command = save_data).pack()
    

app.mainloop()
      




