from tkinter import *
root = Tk()
root.geometry("500x300")


def getvals():
    print("Accepted")
#Hading
Label(root, text="Python Registration Form", font="arial 15 bold").grid(row=0, column=3)
#Fieldname
name= Label(root, text="name")
phone= Label(root, text="phone")
gender= Label(root, text="gender")
emergency= Label(root, text="emergency")
paymentmood= Label(root, text="paymentmood")

#packing Field
name.grid(row=1, column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmood.grid(row=5,column=2)

#Variable for storing data
namevalue=StringVar
phonevalue=StringVar
gendervalue=StringVar
emergencyvalue=StringVar
paymentmoodvalue=StringVar
checkvalue=IntVar

#Creating entry field
nameentry=Entry(root,textvariable = namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymentmoodentry=Entry(root,textvariable=paymentmoodvalue)

#Packing entry fields
nameentry.grid(row=1 ,column=3)
phoneentry.grid(row=2 ,column=3)
genderentry.grid(row=3 ,column=3)
emergencyentry.grid(row=4 ,column=3)
paymentmoodentry.grid(row=5 ,column=3)

#Creating Checkbox
checkbtn=Checkbutton(text="Remeber me", variable=checkvalue)
checkbtn.grid(row=6,column=3)

#submit button
Button(text="Submit",command=getvals).grid(row=7,column=3)

root.mainloop()

