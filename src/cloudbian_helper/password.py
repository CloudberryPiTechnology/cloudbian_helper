from tkinter import *
def start_password_entry(required="abcd1234"):
    root = Tk()
    root.title("Enter your password")
    password = Entry(root, show="*")
    password.pack()
    def submit():
        passw = password.get()
        if passw == required:
            return True
        else:
            return False
    Button(root, text="Submit", command=submit).pack()
    root.mainloop()