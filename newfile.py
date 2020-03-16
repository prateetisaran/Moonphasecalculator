from tkcalendar import Calendar

from tkinter import *
from tkinter.ttk import *

def calendar():
    def date_entry():
        sample_date.configure(state=NORMAL)
        sample_date.delete(0, 10)
        sample_date.insert(INSERT,cal.selection_get())
        sample_date.configure(state=DISABLED)

        print(cal.selection_get())

    top = Toplevel(root)

    cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                   disabledforeground='red',cursor="hand1", year=2020, month=1, day=22)
    cal.pack(fill="both", expand=True)

    Button(top, text="ok", command=date_entry).pack()


root = Tk()

Button(root, text='Calendar', command=calendar).pack(padx=10, pady=10)

sample_date = Entry(root)
sample_date.pack()

root.mainloop()