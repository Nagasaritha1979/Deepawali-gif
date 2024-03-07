from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

win=Tk()
win.geometry('700x700')
win.title("LIVE STREAMING")
win.config(bg='#FFB90F')
win.resizable(False,False)

framecnt=10
frames=[PhotoImage(file='gif2.gif',format='gif -index %i' %(i)) for i in range(framecnt)]

def update(ind):
    frame=frames[ind]
    ind+=1
    if ind==framecnt:
        ind=0
    
    label1.config(image=frame)

    win.after(100,update,ind)

label=Label(win,text="HAPPY DEEPAVALI",font=("Arial",15,'bold'),fg='brown',bg='#FFB90F')
label.pack(padx=10,pady=10)

    
label1=Label(win)
label1.pack(padx=20,pady=20)    

label2=Label(win,text='May the festival of lights bring joy into your lives',font=("Arial",12,'italic','bold'),fg='brown',bg='#FFB90F')
label2.pack(padx=10,pady=10)

win.after(0,update,0)


win.mainloop()
