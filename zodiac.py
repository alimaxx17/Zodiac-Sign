from tkinter import *
root=Tk()
root.title("Zodiac Sign Generator")
root.geometry("400x300")
root.configure(bg="white")
result=Label(root,bg="white")
result.grid(row=4,column=0,columnspan=2)
def get_zodiac(date,month):
    global result
    result.grid_forget()
    date=int(entry1.get())
    month=int(entry2.get())
    if (month==3 and date>=21) or (month==4 and date<20):
        result=Label(root,text="Your Zodiac Sign is ARIES",borderwidth=12,bg="white")
        result.config(font=("Britannic Bold",18))
        result.grid(row=4,column=0,columnspan=2)
    elif (month==4 and date>=20) or (month==5 and date<21):
        result=Label(root,text="Your Zodiac Sign is TAURUS",borderwidth=12,bg="white")
        result.config(font=("Britannic Bold",18))
        result.grid(row=4,column=0,columnspan=2)
    elif (month==5 and date>=21) or (month==6 and date<21):
        result=Label(root,text="Your Zodiac Sign is GEMINI",borderwidth=12,bg="white")
        result.config(font=("Britannic Bold",18))
        result.grid(row=4,column=0,columnspan=2)
    elif (month==6 and date>=21) or (month==7 and date<23):
        result=Label(root,text="Your Zodiac Sign is CANCER",borderwidth=12,bg="white")
        result.config(font=("Britannic Bold",18))
        result.grid(row=4,column=0,columnspan=2)
    elif (month==7 and date>=23) or (month==8 and date<23):
        result=Label(root,text="Your Zodiac Sign is LEO",borderwidth=12,bg="white")
        result.config(font=("Britannic Bold",18))
        result.grid(row=4,column=0,columnspan=2)
    elif (month==8 and date>=23) or (month==9 and date<23):
        result=Label(root,text="Your Zodiac Sign is VIRGO",borderwidth=12,bg="white")
        result.config(font=("Britannic Bold",18))
        result.grid(row=4,column=0,columnspan=2)
    elif (month==9 and date>=23) or (month==10 and date<23):
        result=Label(root,text="Your Zodiac Sign is LIBRA",borderwidth=12,bg="white")
        result.config(font=("Britannic Bold",18))
        result.grid(row=4,column=0,columnspan=2)
    elif (month==10 and date>=23) or (month==11 and date<22):
        result=Label(root,text="Your Zodiac Sign is SCORPIO",borderwidth=12,bg="white")
        result.config(font=("Britannic Bold",18))
        result.grid(row=4,column=0,columnspan=2)
    elif (month==11 and date>=22) or (month==12 and date<22):
        result=Label(root,text="Your Zodiac Sign is SAGITTARIUS",borderwidth=12,bg="white")
        result.config(font=("Britannic Bold",18))
        result.grid(row=4,column=0,columnspan=2)
    elif (month==12 and date>=22) or (month==1 and date<20):
        result=Label(root,text="Your Zodiac Sign is CAPRICORN",borderwidth=12,bg="white")
        result.config(font=("Britannic Bold",18))
        result.grid(row=4,column=0,columnspan=2)
    elif (month==1 and date>=20) or (month==2 and date<19):
        result=Label(root,text="Your Zodiac Sign is AQUARIUS",borderwidth=12,bg="white")
        result.config(font=("Britannic Bold",18))
        result.grid(row=4,column=0,columnspan=2)
    elif (month==2 and date>=19) or (month==3 and date<21):
        result=Label(root,text="Your Zodiac Sign is PISCES",borderwidth=12,bg="white")
        result.config(font=("Britannic Bold",18))
        result.grid(row=4,column=0,columnspan=2)
    else:
        result=Label(root,text="YOUR INPUTS ARE FALSE",borderwidth=12,bg="white")
        result.config(font=("Britannic Bold",18))
        result.grid(row=4,column=0,columnspan=2)

label1=Label(root,text="Welcome To Zodiac Sign Generator ",borderwidth=18,bg="purple",fg="white")
label1.config(font=("Britannic Bold",15))
label1.grid(row=0,column=0,columnspan=2)
label2=Label(root,text="What is Birth Date?:",borderwidth=25,bg="white")
label2.config(font=("Britannic Bold",15))
label2.grid(row=1,column=0)
label3=Label(root,text="What is Birth Month?:",borderwidth=25,bg="white")
label3.config(font=("Britannic Bold",15))
label3.grid(row=2,column=0)
entry1=Entry(root,borderwidth=3,width=7)
entry1.grid(row=1,column=1)
entry2=Entry(root,borderwidth=3,width=7)
entry1.grid(row=1,column=1)
entry2.grid(row=2,column=1)
date=entry1.get()
month=entry2.get()
get_button=Button(root,text="Zodiac Sign",anchor=CENTER,command=lambda:get_zodiac(date,month),height=2,width=20,bg="purple",fg="white")

get_button.grid(row=3,column=0,columnspan=2)
root.mainloop()

