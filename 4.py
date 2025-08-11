from tkinter import *

top=Tk()
top.title("enter email")
top.geometry("600x450")
top.config(background="blue")

first_name = Label(top,
                text="first name").place(x=40,
                                        y=100)
last_name= Label(top,
                     text="last name").place(x=40,
                                            y=140)

email= Label(top,
                     text="email").place(x=40,
                                            y=180)
password= Label(top,
                     text="password").place(x=40,
                                            y=220)

user_password= Entry(top,
                  width=40).place(x=120,
                                  y=220)
user_email= Entry(top,
                  width=40).place(x=120,
                                  y=180)


user_first_name= Entry(top,
                  width=40).place(x=120,
                                  y=100)

register= Entry(top,
                width=40).place(x=120,
                                y=140)
register=Button(top,
              text="register").place(x=40,
                                   y=280)


top.mainloop()