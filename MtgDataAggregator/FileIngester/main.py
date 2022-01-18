from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd


def open_file_dialog():
    file_name = fd.askopenfilename()
    txt_file_path.insert(0, file_name)


def submit_file():
    file_name = txt_file_path.get()
    location = txt_location.get()


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
txt_file_path = ttk.Entry(frm)
txt_location = ttk.Entry(frm)
ttk.Label(frm, text="Please select a csv file to import").grid(column=1, row=0)
txt_file_path.grid(column=1, row=1)
ttk.Button(frm, text="Select File", command=open_file_dialog).grid(column=1, row=2)
ttk.Label(frm, text="Enter A Location for this").grid(column=1, row=3)
txt_location.grid(column=1, row=4)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=5)
ttk.Button(frm, text="Submit", command=submit_file).grid(column=2, row=5)
root.mainloop()

