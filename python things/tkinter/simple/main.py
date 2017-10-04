import Tkinter

def tell():
    print "Hallo welt"

l = Tkinter.Label(text = "See me?")
b = Tkinter.Button(text = "Hallo" ,command=tell())
l.pack()
b.pack()
l.mainloop()
