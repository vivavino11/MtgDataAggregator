#$env:FLASK_APP = "Controller.py"
#$env:FLASK_ENV = "development"
#flask run

from mtgsdk import Set


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    response = Set.all()
    test = response


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
