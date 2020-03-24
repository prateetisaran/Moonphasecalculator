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
    #These get the date entered by the user and split it into 3 seperate values to be used for the calculation.
    x = sample_date.get()
    Y = int(x[0:4])
    M = int(x[5:7])
    D = int(x[8:])


    moon_phase = datetophase(D,M,Y)
    toprint.set(moon_phase)

    #These set up the corresponding image to be displayed based on the value obtained by the calculations.
    moon_phase = displayimage(moon_phase)
    moon_phase = ImageTk.PhotoImage(Image.open(moon_phase))
    imgLabel.configure(image=moon_phase)
    imgLabel.photo = moon_phase

def displayimage (x):
    #This function connects a result string to the name of the image corresponding to it. 
    global mydict

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



def calendar():
    def date_entry():
        sample_date.configure(state=NORMAL)
        sample_date.delete(0, 10)
        sample_date.insert(INSERT,cal.selection_get())
        sample_date.configure(state=DISABLED)


    top = Toplevel(screen)

    cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                   disabledforeground='red',cursor="hand1", year=2020, month=1,)
    cal.pack(fill="both", expand=True)

    Button(top, text="select date", command=date_entry).pack()








if __name__ == '__main__':


    mydict = {'waning crescent': 'waningcrescent.png',
              'waning gibbous': 'waninggibbous.png',
              'waxing gibbous': 'waxinggibbous.png',
              'waxing crescent': 'waxingcrescent.png',
              'new moon': 'newmoon.png',
              'full moon': 'fullmoon.png',
              'first quarter': 'firstquarter.png',
              'third quarter': 'thirdquarter.png'}


    from tkinter import *
    from tkinter.ttk import *
    from datetime import datetime, timedelta
    from PIL import ImageTk, Image
    from tkcalendar import Calendar

    screen = Tk()
    screen.configure(background='black')
    screen.title("Lunar Phases")
    Label(screen, text="Welcome to the Lunar Phase Calculator!")

#-- Tabs Setup --#

    Tabs = Notebook(screen, width=600)
    Tabs.pack()

    SpecificDate= Frame(Tabs,borderwidth=10)
    Tabs.add(SpecificDate, text="Specific Date")

    Whennext = Frame(Tabs, borderwidth=10)
    Tabs.add(Whennext, text="When is the next...")

    Today = Frame(Tabs, borderwidth=10)
    Tabs.add(Today, text="Today")

#-- Specific Date Widgets ---#

    Label(SpecificDate, text="Select a specific date to know the lunar phase").pack()

    Button(SpecificDate, text=' See Calendar', command=calendar).pack(padx=10, pady=10)



    sample_date = Entry(SpecificDate)
    sample_date.pack()
    Button(SpecificDate, text="Click to see the lunar phase!", command=specificdate).pack()




    toprint = StringVar()

    Label(SpecificDate, text="", textvariable=toprint).pack()



    imgLabel = Label(SpecificDate)
    imgLabel.pack()




#-- When next widgets

    Button(Whennext, text="Next Full Moon", command=nextphasefm).pack()

    myim = Image.open('fullmoon.png')
    myim = ImageTk.PhotoImage(myim)
    Label(Whennext, image=myim).pack()

    full = StringVar()
    Label(Whennext, text="", textvariable=full).pack()
    #This uses the current date and the previous formula to determine and print the date of the next full moon

    Button(Whennext, text="Next New Moon", command=nextphasenm).pack()

    myimgx = Image.open('newmoon.png')
    myimgx = ImageTk.PhotoImage(myimgx)
    Label(Whennext, image=myimgx).pack()

    new = StringVar()
    Label(Whennext, text="", textvariable=new).pack()
    # This uses the current date and the previous formula to determine and print the date of the next new moon




#-- Today Widgets

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
