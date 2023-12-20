from tkinter import *
from tkinter import messagebox, ttk
from login import *
from to_student import *
root=Tk()
root.title('Welcome')
root.resizable(False,False)
width=1000
height=700
font = 'Akshar'
def center_screen(width, height):      
   screenwidth=root.winfo_screenwidth()
   screenheight=root.winfo_screenheight()
   x=int((screenwidth-width)/2)
   y=int((screenheight-height)/2)
   root.geometry(f"{width}x{height}+{x}+{y}")

center_screen(width, height)

padx = 10
pady = 10

# photo of the start page

def new_window():
    root.destroy()
    window=Tk()
    obj=Login(window)
    
def new_window2():
    root.destroy()
    window2=Tk()
    obj2=to_student(window2)    
# 52796f
btn=Button(root,text='Admins and Teachers',padx= padx,pady =pady,bg='#52796f',width = 20,height =2,relief=RAISED,
    font=('Akshar Bold', 14),fg= '#f6fff8',command=new_window)
btn.place(x = 200, y = 600)


btn1=Button(root,text='Students',bg='#52796f',fg= '#f6fff8',padx = padx, pady =pady,width = 10,height =2,relief=RAISED,
    font=('Akshar Bold', 14),command=new_window2)
btn1.place(x = 600, y = 600)
root.mainloop()
# ALL DONE
# font for all project is Akshar