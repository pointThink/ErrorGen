from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from ttkthemes import ThemedStyle

main = Tk()
main.title("Error")
main.iconbitmap("icon.ico")

# setting theme
style = ThemedStyle(main)
style.set_theme("equilux")
main.configure(bg="grey27")


MsgType = IntVar() # this variable is here otherwise it causes an error


# Generate error function (this is where the action happens)
def Generate():
    Title = TitleInput.get()
    Msg = MsgInput.get()

    MsgTypeFinal = MsgType.get()

    # changing icon
    Icon = IconInput.get()

    if Icon == "":
        main.iconbitmap("blank.ico")
    else:
        main.iconbitmap(Icon)

    if MsgTypeFinal == 1:
        messagebox.showerror(Title, Msg)
    elif MsgTypeFinal == 2:
        messagebox.showwarning(Title, Msg)
    elif MsgTypeFinal == 3:
        messagebox.askquestion(Title, Msg)
    elif MsgTypeFinal == 4:
        messagebox.showinfo(Title, Msg)
    else:
        print("whoops das an error")

    # getting the icon back to normal    
    main.iconbitmap("icon.ico")



# Setting Up the UI
TitleLabel = Label(main, text="Error Title")
MsgLabel = Label(main, text="Error Message")
IconLabel = Label(main, text="Error Icon")
TitleInput = Entry(main)
MsgInput = Entry(main)
IconInput = Entry(main)

MsgTypeError = Radiobutton(main, text="Critical Error‎‎‎‎‎", variable=MsgType, value=1)
MsgTypeWarning = Radiobutton(main, text="Warning", variable=MsgType, value=2)
MsgTypeQuestion = Radiobutton(main, text="Question", variable=MsgType, value=3)
MsgTypeInfo = Radiobutton(main, text="Information", variable=MsgType, value=4)

GenerateButton = Button(main, text="Generate", command=Generate)


TitleLabel.grid(row=0, column=0)
MsgLabel.grid(row=1, column=0)
IconLabel.grid(row=2)
TitleInput.grid(row=0, column=1)
MsgInput.grid(row=1, column=1)
IconInput.grid(row=2, column=1)

MsgTypeError.grid(row=4, column=0,)
MsgTypeWarning.grid(row=3, column=1)
MsgTypeQuestion.grid(row=4, column=1)
MsgTypeInfo.grid(row=3, column=0)

GenerateButton.grid(row=5, column=0)

main.mainloop()