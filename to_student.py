# before student enter the system
from tkinter import *
from tkinter import messagebox,ttk
from student import *
class to_student:
    def __init__ (self , root):
        self.root=root
        self.root.title('student manemant system')
        self.root.geometry('1000x615+0+0')
        self.root.resizable(False,False)
        self.root.configure(bg='#6b9080')
       
        width=500
        height=500
        padx= 15
        pady= 15
        def center_screen(width, height):      
           screenwidth=root.winfo_screenwidth()
           screenheight=root.winfo_screenheight()
           x=int((screenwidth-width)/2)
           y=int((screenheight-height)/2)
           root.geometry(f"{width}x{height}+{x}+{y}")
        
        center_screen(width, height)
        frame=Frame(root,bg='#6b9080')
        lb1=Label(frame,text='Your Name: ',font=('Ashkar',14),fg='#f6fff8',bg='#6b9080',padx= padx, pady=pady)
        
        lb1.grid(row = 0, column = 0)
        txt_name=Entry(frame,width=40)
        txt_name.grid(row = 0, column = 1)
        
        
        lb2=Label(frame,text='Your ID: ',font=('Ashkar',14),fg='#f6fff8',bg='#6b9080',padx= padx, pady=pady )
         
        lb2.grid(row = 2, column= 0)
        txt_id=Entry(frame,width=40)
        txt_id.grid(row = 2, column = 1)
        
        
        
        frame.place(anchor='center', relx = 0.5, rely =0.5) # relation x, relation y
        def new_window():
            root.destroy()
            window=Tk()
            obj=STUDENT(window)
        
        btn=Button(frame,text='Show info',bg='#6b9080',fg= '#f6fff8',width = 10,height =2,relief=RAISED,
        font=('Ashkar Bold', 14), command= new_window)
        btn.grid(row = 3, column= 0,columnspan=2)
        
# root.mainloop()