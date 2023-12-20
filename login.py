from tkinter import *
from tkinter import messagebox,ttk
class Login:
    def __init__ (self , root):
        self.root=root
        self.root.title('Login')
        self.root.resizable(False,False)
        self.root.configure(bg='#6b9080')
        width=350
        height=420
        screenwidth=self.root.winfo_screenwidth()
        screenheight=self.root.winfo_screenheight()
        x=int((screenwidth-width)/2)
        y=int((screenheight-height)/2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
        frame=Frame(self.root,bg='#6b9080')
        frame.place(x=1,y=1,width=350,height=310)
        title=Label(frame,text='Login',font=('Ashkar',18,'bold'),fg='#f6fff8', bg='#6b9080')
        title.pack(side='top')
        
        lb1=Label(frame,text='Username : ',font=('Ashkar',12),fg='#f6fff8',bg='#6b9080')
        lb1.place(x=30,y=50)
        txt_user=Entry(frame,width=40)
        txt_user.place(x=30,y=90)
        
        lb2=Label(frame,text='Password :',font=('Askhar',12),fg='#f6fff8', bg='#6b9080')
        lb2.place(x=30,y=130) 
        txt_pass=Entry(frame,show='*',width=40)
        txt_pass.place(x=30,y=170)
        
        def check():
            vaild_user='s'
            vaild_pass='1'
            username=txt_user.get()
            password=txt_pass.get()
            if vaild_user== username and password==vaild_pass:
                messagebox.showinfo('info','vaild')
                main=Toplevel()
                obj=ADMIN(main)
            else:
                messagebox.showerror('error','Invaild')
            
        but=Button(frame,text='login',command=check,font=('Ashkar',16,'bold'),bg='#6b9080',fg='#f6fff8',width=16,height=1)
        but.pack(side='bottom')
'''
root=Tk()
obj=Login(root)
root.mainloop()
'''