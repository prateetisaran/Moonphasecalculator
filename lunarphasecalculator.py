from tkinter import *
from tkinter.ttk import *
from datetime import datetime,timedelta
from PIL import ImageTk, Image
screen=Tk()
screen.configure(background='black')
screen.title("Lunar Phases")
Label(screen,text="Welcome to the Lunar Phase Calculator!")
Tabs = Notebook(screen, width=600)
Tabs.pack()

def converttojulian (D,M,Y):
    # The Julian Date value is calculated for the given day, month and year using the following steps
    A = Y / 100
    B = A / 4
    C = 2 - A + B
    E = 365.25 * (Y + 4716)
    F = 30.6001 * (M + 1)
    JD = C + D + E + F - 1524.5
    # since no time has been specified, the JD variable is modified to show exactly 00:00 on the specified date
    return(int(JD) + 0.5)

def datetophase(D,M,Y):
    JD = converttojulian(D,M,Y)
    dayssince = JD - 28.4766799998
    #Here the number starting with 28 is the julian date of the Earliest New Moon in Julian Dates
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
    toprint.set(datetophase((int(D.get())),(int(M.get())),(int(Y.get()))))

def displayimage (x):
    mydict = {'waning crescent':'waningcrescent.png','waning gibbous':'waninggibbous.png','waxing gibbous':'waxinggibbous.png','waxing crescent':'waxingcrescent.png',
              'new moon':'newmoon.png','full moon':'fullmoon.png','first quarter':'firstquarter.png','third quarter':'thirdquarter.png'}

    for m,n in mydict.items():
        if m == x:
            return (n)

def nextphasefm():
    x = datetime.now()
    c = datetophase((int(x.strftime('%d'))), (int(x.strftime('%m'))), (int(x.strftime('%Y'))))
    D = int(x.strftime('%d'))
    M = int(x.strftime('%m'))
    Y = int(x.strftime('%Y'))
    JD = converttojulian(D,M,Y)
    dayssince = JD - 28.4766799998
    numberofnewmoons = dayssince / 29.53
    lastnewmoon = ((int(numberofnewmoons)) * 29.53) + 28.4766799998
    fullmoon = lastnewmoon + 14.765
    fullmoondate = fullmoon - JD
    if fullmoon > JD:
        fm = datetime.now() + timedelta(days=fullmoondate)
        fm = fm.strftime('%d %B %Y')
        full.set(fm)
    elif fullmoon < JD:
        fm = datetime.now() + timedelta(days=fullmoondate) + timedelta(days=29.53)
        fm = fm.strftime('%d %B %Y')
        full.set(fm)
    elif c == 'full moon':
        fm = datetime.now()
        fm = fm.strftime('%d %B %Y')
        full.set(fm)

def nextphasenm():
    x = datetime.now()
    c = datetophase((int(x.strftime('%d'))), (int(x.strftime('%m'))), (int(x.strftime('%Y'))))
    D = int(x.strftime('%d'))
    M = int(x.strftime('%m'))
    Y = int(x.strftime('%Y'))
    JD = converttojulian(D,M,Y)
    dayssince = JD - 28.4766799998
    numberofnewmoons = dayssince / 29.53
    lastnewmoon = ((int(numberofnewmoons)) * 29.53) + 28.4766799998
    nextnewmoon = lastnewmoon + 29.53
    newmoondate = nextnewmoon - JD
    if c == 'new moon':
        nm = datetime.now()
        nm = nm.strftime('%d %B %Y')
        new.set(nm)
    else:
        nm = datetime.now() + timedelta(days=newmoondate)
        nm = nm.strftime('%d %B %Y')
        new.set(nm)

SpecificDate= Frame(Tabs,borderwidth=10)
Tabs.add(SpecificDate, text="Specific Date")
#Specific Date Widgets
Label(SpecificDate, text="Enter a specific date to know the lunar phase").pack()
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
x=(datetophase((int(D)),(int(M.get())),(int(Y.get()))))
myimg = Image.open(displayimage(x))
myimg = myimg.resize((320,300))
myimg = ImageTk.PhotoImage(myimg)
Label(SpecificDate, image=myimg).pack()
#I want to add an image here that corresponds to the answer produced, to do that i would have to run
# the string value of toprint into the function displayimage and that would produce the name of the image

Whennext = Frame(Tabs, borderwidth=10)
Tabs.add(Whennext, text="When is the next...")
#When next widgets
Button(Whennext, text="Next Full Moon", command=nextphasefm).pack()
myim = Image.open('fullmoon.png')
myim = ImageTk.PhotoImage(myim)
Label(Whennext, image=myim).pack()
full = StringVar()
Label(Whennext, text="", textvariable=full).pack()
Button(Whennext, text="Next New Moon", command=nextphasenm).pack()
myimgx = Image.open('newmoon.png')
myimgx = ImageTk.PhotoImage(myimgx)
Label(Whennext, image=myimgx).pack()
new = StringVar()
Label(Whennext, text="", textvariable=new).pack()

Today = Frame(Tabs, borderwidth=10)
Tabs.add(Today, text="Today")
#Today Widgets
x = datetime.now()
datetoday = x.strftime('%A, %d %B %Y')
Label(Today, text=datetoday).pack()
c = datetophase((int(x.strftime('%d'))),(int(x.strftime('%m'))),(int(x.strftime('%Y'))))
ctwo = displayimage(c)
myimg = Image.open(ctwo)
myimg = myimg.resize((320,300))
myimg = ImageTk.PhotoImage(myimg)
Label(Today, image=myimg).pack()
Label(Today,text=c).pack()



screen.mainloop()

