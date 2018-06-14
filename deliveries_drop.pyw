#!/usr/local/bin/python3
"""Save text entered in fields to file. Messagebox showing user data. Clears text after save.
Exercise from headfirst book."""
from tkinter import *
from tkinter import messagebox
"""
depots = ["Cambridge, MA",
"Cambridge, UK",
"Seattle, WA",
"New York, NY",
"Dallas, TX",
"Boston, MA",
"Rome, Italy",
"Male, Maldives",
"Luxor, Egypt",
"Rhodes, Greece",
"Edinburgh, Scotland"]
"""
def read_depots(file):
    """read in data from file."""
    d = []
    depots_f = open(file)
    for line in depots_f:
        d.append(line.rstrip())
    depots_f.close()
    return(d)
    
def save_data():
    try:
        fileD = open("deliveries.txt", "a")
        fileD.write("Depot:\n")
        fileD.write("%s\n" % depot.get())
        #fileD.write("%s\n" % depot.get())
        fileD.write("Description:\n")
        fileD.write("%s\n" % description.get())
        fileD.write("Address:\n")
        fileD.write("%s\n" % address.get("1.0", END))
        depot.set(None)
        description.delete(0, 'end')
        address.delete(1.0, 'end')
        messagebox.showinfo(title="Head-Ex Deliveries Form", message="Order submitted!")
    except Exception as ex:
       app.title("Can't write to the file %s" %ex)
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

options = read_depots("depots.txt")
OptionMenu(app, depot, *options).pack()

Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()

Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

Button(app, text = "Save", command = save_data).pack()
    

app.mainloop()
      




