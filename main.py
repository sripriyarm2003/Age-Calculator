from tkinter import *
from datetime import date

root=Tk()
root.geometry("800x600")
root.resizable(False,False)
root.title("Age Calculator")

photo=PhotoImage(file="age.png")
myimage=Label(image=photo,width=400,height=280)
myimage.pack(padx=15,pady=15)

def calculateAge():
    today=date.today()
    birthDate=date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age=today.year-birthDate.year-((today.month,today.day)<(birthDate.month,birthDate.day))
    Label(text=f"{nameValue.get()}, your age is {age}", font=30).place(x=300,y=550)

Label(text="Name",font=23).place(x=200,y=300)
Label(text="Year",font=23).place(x=200,y=350)
Label(text="Month",font=23).place(x=200,y=400)
Label(text="Day",font=23).place(x=200,y=450)

nameValue=StringVar()
yearValue=StringVar()
monthValue=StringVar()
dayValue=StringVar()

nameEntry=Entry(root,textvariable=nameValue,width=20,bd=3,font=20)
nameEntry.place(x=300,y=300)
yearEntry=Entry(root,textvariable=yearValue,width=20,bd=3,font=20)
yearEntry.place(x=300,y=350)
monthEntry=Entry(root,textvariable=monthValue,width=20,bd=3,font=20)
monthEntry.place(x=300,y=400)
dayEntry=Entry(root,textvariable=dayValue,width=20,bd=3,font=20)
dayEntry.place(x=300,y=450)

Button(text="Calculate age",font=20,bg="sky blue",fg="black",width=11,height=2,command=calculateAge).place(x=350,y=500)

root.mainloop()
