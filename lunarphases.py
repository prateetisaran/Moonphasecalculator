from tkinter import *
from tkinter.ttk import *
from datetime import datetime

screen=Tk()
screen.configure(background='black')

screen.title("Lunar Phases")
label=label(screen,text="Welcome to the Lunar Phase Calculator!")
Tabs = Notebook(popup, width=600)
Tabs.pack()

Today = Frame(Tabs, borderwidth=10)
Tabs.add(Today, text="Today")

SpecificDate= Frame(Tabs,borderwidth=10)
Tabs.add(SpecificDate, text="Specific Date")
Label(SpecificDate, text="Main Course").pack()
Label(SpecificDate, text="Day").pack()
D = Entry(SpecificDate)
D.pack()
Label(SpecificDate, text="Month").pack()
M = Entry(SpecificDate)
M.pack()
Label(SpecificDate, text="Year").pack()
Y = Entry(SpecificDate)
Y.pack()
Button(SpecificDate, text="See the lunar phase!", command=specificdate).pack()
toprint = StringVar()
Label(SpecificDate, text="", textvariable=toprint).pack()
displaytheimage(toprint)


Thisweek= Frame(Tabs, borderwidth=10)
Tabs.add(Thisweek, text="This Week")

def datetophase(D,M,Y):

    # The Julian Date value is calculated for the given day, month and year using the following steps
    A = Y / 100
    B = A / 4
    C = 2 - A + B
    E = 365.25 * (Y + 4716)
    F = 30.6001 * (M + 1)
    JD = C + D + E + F - 1524.5

    # since no time has been specified, the JD variable is modified to show exactly 00:00 on the specified date
    JD = int(JD) + 0.5

    dayssince = JD - 28.4766799998
    numberofnewmoons = dayssince / 29.53

    #This determines the Julian Date of the last new moon before the specified date
    #Using that date, it determines the dates of the rest of the stages.
    lastnewmoon = ((int(numberofnewmoons)) * 29.53) + 28.4766799998
    fullmoon = lastnewmoon + 14.765
    firstquarter = (lastnewmoon + 7.3825)
    thirdquarter = (lastnewmoon + 22.1475)
    nextnewmoon = lastnewmoon + 29.53


    #These if statements determine if any of the 4 phases occurs on any the date specified.
    if (lastnewmoon >= JD and lastnewmoon < (JD + 1))or(nextnewmoon >= JD and nextnewmoon < (JD + 1)):
        return ('new moon')
    elif firstquarter >= JD and firstquarter < (JD + 1):
        return ('first quarter')
    elif fullmoon >= JD and fullmoon < (JD + 1):
        return ('full moon')
    elif thirdquarter >= JD and thirdquarter < (JD + 1):
        return ('third quarter')

    #If any of those 4 phases do not occur on this date, these if statements determine what phases this date is in between
    elif lastnewmoon < JD and firstquarter >= (JD + 1):
        return ('waxing crescent')
    elif firstquarter < JD and fullmoon >= (JD + 1):
        return ('waxing gibbous')
    elif fullmoon < JD and thirdquarter >= (JD + 1):
        return ('waning gibbous')
    elif thirdquarter < JD:
        return ('waning crescent')

def specificdate():
    toprint.set(datetophase((int(D.get()),(int(M.get())),(int(Y.get()))))







def displaytheimage(x):
    if x == 'new moon':
        myimg = Image.open('newmoon.png')
        myimg = myimg.resize((100, 100))
        myimg = ImageTk.PhotoImage(myimg)
    elif x == 'first quarter':
        myimg = Image.open('firstquarter.png')
        myimg = myimg.resize((100, 100))
        myimg = ImageTk.PhotoImage(myimg)
    elif x == 'full moon':
        myimg = Image.open('fullmoon.png')
        myimg = myimg.resize((100, 100))
        myimg = ImageTk.PhotoImage(myimg)
    elif x == 'third quarter':
        myimg = Image.open('thirdquarter.png')
        myimg = myimg.resize((100, 100))
        myimg = ImageTk.PhotoImage(myimg)
    elif x == 'waxing crescent':
        myimg = Image.open('waxingcrescent.png')
        myimg = myimg.resize((100, 100))
        myimg = ImageTk.PhotoImage(myimg)
    elif x == 'waxing gibbous':
        myimg = Image.open('waxinggibbous.png')
        myimg = myimg.resize((100, 100))
        myimg = ImageTk.PhotoImage(myimg)
    elif x == 'waning gibbous':
        myimg = Image.open('waninggibbous.png')
        myimg = myimg.resize((100, 100))
        myimg = ImageTk.PhotoImage(myimg)
    elif x == 'waning crescent':
        myimg = Image.open('waningcrescent.png')
        myimg = myimg.resize((100, 100))
        myimg = ImageTk.PhotoImage(myimg)






def today():
    x = datetime.now()
    today.set(datetophase((x.strftime('%d')),(x.strftime('%m')),(x.strftime('%Y'))))
    today=StringVar
    displaytheimage(today)










#Things in today











screen.mainloop()
