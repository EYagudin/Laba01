from tkinter import *

#var
root = Tk()
root.title("Symbol Finder")
root.wm_attributes("-topmost", True)
root.geometry('525x180')
root.resizable(width=False, height=False)
img1 = PhotoImage(file='roof.gif')
space= Label(root, text="")

#countchar
def count():
    if (line.get()=="") or (char.get()=="") :
        labelres.config(text="X")
        restext.config(text="Please enter\n correct data!")
    elif len(char.get())>1:
        labelres.config(text="X")
        restext.config(text="Please enter\n ONE symbol!")
    else:
        result=line.get().count(char.get())
        labelres.config(text=result)
        restext.config(text= "'"+char.get()+"' symbols\n in line")
#clearline
def clear():
        line.delete(0, 'end')
        char.delete(0, 'end')
        line.focus_set()

#imgup
lmageup = Label(root,
                image=img1)
lmageup.pack()
space.pack()

#line label
label1= Label(root,
              text="Enter line:",
              font = "Verdana 10 bold",
              fg = "#555",
              compound=LEFT,
              )
label1.place(x=20, y=20)

#line enter
line = Entry(root,
             width=80)
line.place(x=20, y=45)
line.focus_set()

#char label
label2= Label(root,
              text="Enter symbol:",
              font="Verdana 10 bold",
              fg="#555",
              compound=LEFT
              )
label2.place(x=20, y=70)
#char enter
char = Entry(root,
             width=5)
char.place(x=20, y=95)

#butt action
actionbut = Button(root,
           text = "Count",
           width = 10,
           background="#555",
           foreground="#ccc",
           command = count)
actionbut.place(x=20, y=130)

#butt clear
clearbut = Button(root,
           text = "Clear",
           width = 10,
           background="#555",
           foreground="#ccc",
           command = clear)
clearbut.place(x=130, y=130)

#result label
labelres= Label(root,
              text="☺",
              font="sans-serif 50 bold",
              fg="#555",
              compound=LEFT
              )
labelres.place(x=340, y=80)
restext= Label(root,
              text="Welcome to\n Symbol Finder!",
              font="sans-serif 10",
              fg="#555",
               justify=LEFT
              )
restext.place(x=400, y=105)

#imgdown
lmagedn = Label(root,
                image=img1)

mainloop()

