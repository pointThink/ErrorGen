from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from ttkthemes import ThemedStyle

main = Tk()
main.title("Error")
main.iconbitmap("blank.ico")

# setting theme
style = ThemedStyle(main)
style.set_theme("equilux")
main.configure(bg="grey27")


icon = IntVar() # this variable is here otherwise it causes an error

# Generate error function
def Generate():
    Title = TitleInput.get()
    Msg = MsgInput.get()
    
    ErrorIcon = icon.get()

    if ErrorIcon == 1:
        messagebox.showerror(Title, Msg)
    elif ErrorIcon == 2:
        messagebox.showwarning(Title, Msg)
    elif ErrorIcon == 3:
        messagebox.askquestion(Title, Msg)
    elif ErrorIcon == 4:
        messagebox.showinfo(Title, Msg)
    else:
        print("whoops das an error")



# Setting Up the UI
TitleLabel = Label(main, text="Error Title")
MsgLabel = Label(main, text="Error Message")
TitleInput = Entry(main)
MsgInput = Entry(main)

IconError = Radiobutton(main, text="Critical Error‎‎‎‎‎", variable=icon, value=1)
IconWarning = Radiobutton(main, text="Warning", variable=icon, value=2)
IconQuestion = Radiobutton(main, text="Question", variable=icon, value=3)
IconInfo = Radiobutton(main, text="Information", variable=icon, value=4)

GenerateButton = Button(main, text="Generate", command=Generate)


TitleLabel.grid(row=0, column=0)
MsgLabel.grid(row=1, column=0)
TitleInput.grid(row=0, column=1)
MsgInput.grid(row=1, column=1)

IconError.grid(row=3, column=0,)
IconWarning.grid(row=2, column=1)
IconQuestion.grid(row=3, column=1)
IconInfo.grid(row=2, column=0)

GenerateButton.grid(row=4, column=0)

main.mainloop()