from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

screen = Tk()
screen.configure(background='red')

def CoursesWindow():

    popup = Toplevel(screen)
    popup.title("Window 2")
    popup.configure(background='red')

    Label(popup, text="Menu Selection").pack()

    Tabs = Notebook(popup, width=600)
    Tabs.pack()

    Starter = Frame(Tabs, borderwidth=10)
    Tabs.add(Starter, text="Starters")

    MainCourse = Frame(Tabs,borderwidth=10)
    Tabs.add(MainCourse, text="Main Course")

    Dessert = Frame(Tabs, borderwidth=10)
    Tabs.add(Dessert, text="Dessert")


    ###### Starters

    Label(Starter,text="Starters").pack()
    imagesonstarter= {'garlicbread.jpg':[1,1],'caesersalad.jpg':[1,2]}

    for name,position in imagesonstarter.items():
        

    ###### Main Course

    Label(MainCourse, text="Main Course").pack()

    ###### Desserts

    Label(Dessert, text="Desserts").pack()




def ReceiptWindow():




myimg = Image.open('project.png')
myimg = myimg.resize((100,100))
myimg = ImageTk.PhotoImage(myimg)

label = Label(screen, image=myimg)
label.grid(row=1,column=0)

Button(screen,text="Click Me",command=CoursesWindow()).grid(row=10,column=0)

screen.mainloop()