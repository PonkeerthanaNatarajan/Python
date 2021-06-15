from tkinter import *
from tkinter import ttk


window=Tk()
window.title("Registration Form")
window.geometry('500x500')
window.configure(background="grey")


Caption=Label(window,text="REGISTRATION FORM").grid(row=3,column=2)

Firstname=Label(window,text="First Name").grid(row=5,column=1)

Middlename=Label(window,text="Middle Name").grid(row=10,column=1)

Lastname=Label(window,text="Last Name").grid(row=15,column=1)

Gender=Label(window,text="Gender").grid(row=20,column=1)
var=IntVar()
Radiobutton(window,text="Male",variable=var,value=1).grid(row=20,column=2)
Radiobutton(window,text="Female",variable=var,value=2).grid(row=20,column=3)

Age=Label(window,text="Age").grid(row=25,column=1)

Email=Label(window,text="Email Id").grid(row=30,column=1)

Mobile=Label(window,text="Contact Number").grid(row=35,column=1)

Employeeid=Label(window,text="Employee Id").grid(row=40,column=1)

Designation=Label(window,text="Designation").grid(row=45,column=1)
options=["Labour","Assistant Manager","Manager","HR","CEO","M.D"]
clicked=StringVar()
droplist=OptionMenu(window,clicked,*options)
clicked.set('Select your Designation')
droplist.grid(row=45,column=3)

Salary=Label(window,text="Salary Expected").grid(row=50,column=1)


Firstname1=Entry(window).grid(row=5,column=3)

Middlename1=Entry(window).grid(row=10,column=3)

Lastname1=Entry(window).grid(row=15,column=3)

Age1=Entry(window).grid(row=25,column=3)

Email1=Entry(window).grid(row=30,column=3)

Mobile1=Entry(window).grid(row=35,column=3)

Employeeid1=Entry(window).grid(row=40,column=3)

Salary1=Entry(window).grid(row=50,column=3)

def onClick():
    tkinter.messagebox.showinfo("Welcome","Registration Form Submitted succesfully")

btn=ttk.Button(window,text="Submit").grid(row=55,column=5)

window.mainloop()
