from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd


def get_csv_file():
    file_name = fd.askopenfilename(filetypes=[('CSV Files', '.csv')])
    txt_file_path.insert(0, file_name)


def parse_csv_into_card():
    csv_file_name = txt_file_path.get()
    if csv_file_name == '':
        return
    with open(csv_file_name, 'r') as csv_file:
        for line in csv_file:
            line = line.strip()
            if line == '':
                continue
            card_info = line.split(',')
            card_name = card_info[0]


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
txt_file_path = ttk.Entry(frm)
txt_location = ttk.Entry(frm)
ttk.Label(frm, text="Please select a csv file to import").grid(column=1, row=0)
txt_file_path.grid(column=1, row=1)
ttk.Button(frm, text="Select File", command=get_csv_file).grid(column=1, row=2)
ttk.Label(frm, text="Enter A Location for this").grid(column=1, row=3)
txt_location.grid(column=1, row=4)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=5)
ttk.Button(frm, text="Submit", command=submit_file).grid(column=2, row=5)
root.mainloop()