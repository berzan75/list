from tkinter import *

top=Tk()
top.geometry("300x450")
top.title("listbox")

label=Label(top,
            text="food items")

listbox=Listbox(top,
                width=10,
                height=15,
                bg="light blue",
                fg="white",
                activestyle="dotbox",
                font="Helvetica",
                )
listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(4,"rice")
listbox.insert(3,"ice cream")


label.pack()
listbox.pack()

top.mainloop()