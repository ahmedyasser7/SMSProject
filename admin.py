from tkinter import *
from tkinter import messagebox,ttk
class ADMIN:
    def __init__ (self , root):
        self.root=root
        self.root.title('student manemant system')
        self.root.geometry('1310x615+0+0')
        self.root.resizable(False,False)
        self.root.configure(bg='#6b9080')
        
        #=====Entries Frame=============#
        entries_frame=Frame(self.root,bg='#6b9080')
        entries_frame.place(x=1,y=1,width=560,height=500)
        
        title=Label(entries_frame,text='student service potal',font=('Ashkar',14,'bold'),bg='#6b9080',fg='#f6fff8')
        title.place(x=10,y=1)
        
        lb1_ID=Label(entries_frame,text='ID',font=('Ashkar',14),bg='#6b9080',fg='#f6fff8')
        lb1_ID.place(x=10,y=50)
        text_ID=Entry(entries_frame,width=20,font=('Ashkar',14))
        text_ID.place(x=120,y=50)
        
        lb1_name=Label(entries_frame,text='Name',font=('Ashkar',14),bg='#6b9080',fg='#f6fff8')
        lb1_name.place(x=10,y=90)
        text_name=Entry(entries_frame,width=20,font=('Ashkar',14))
        text_name.place(x=120,y=90)
        
        lb1_gba=Label(entries_frame,text='GPA',font=('Ashkar',14),bg='#6b9080',fg='#f6fff8')
        lb1_gba.place(x=10,y=130)
        text_gba=Entry(entries_frame,width=20,font=('Ashkar',14))
        text_gba.place(x=120,y=130)
        
        lb1_email=Label(entries_frame,text='Email',font=('Ashkar',14),bg='#6b9080',fg='#f6fff8')
        lb1_email.place(x=10,y=170)
        text_email=Entry(entries_frame,width=20,font=('Ashkar',14))
        text_email.place(x=120,y=170)
        
        lb1_section=Label(entries_frame,text='Section',font=('Ashkar',14),bg='#6b9080',fg='#f6fff8')
        lb1_section.place(x=10,y=210)
        combosection=ttk.Combobox(entries_frame,state='readonly',width=18,font=('Ashkar',14))
        combosection['values']=("CS","IS","AI","SC")
        combosection.place(x=120,y=210)
        
        lb1_level=Label(entries_frame,text='Level',font=('Ashkar',14),bg='#6b9080',fg='#f6fff8')
        lb1_level.place(x=10,y=250)
        combolevel=ttk.Combobox(entries_frame,state='readonly',width=18,font=('Ashkar',14))
        combolevel['values']=("one","two","thrid","fourth")
        combolevel.place(x=120,y=250)
        
        """lb1_address=Label(entries_frame,text='Address : ',font=('Ashkar',14),bg='#6b9080',fg='#f6fff8')
        lb1_address.place(x=10,y=290)
        text_address=Entry(entries_frame,width=25,font=('Ashkar',14))
        text_address.place(x=10,y=330,width=300,height=50)"""
        lb1_address=Label(entries_frame,text='Address: ',font=('Ashkar',16),bg='#6b9080',fg='#f6fff8')
        lb1_address.place(x=10,y=290)
        text_address=Entry(entries_frame,width=20,font=('Ashkar',16))
        text_address.place(x=120,y=290,width=220,height=50)
        #===========Button Frame============#
        btn_frame=Frame(entries_frame,bg='#f6fff8',bd=1,relief=RAISED)
        btn_frame.place(x=50,y=400,width=335,height=100)
        def sure():
            result=messagebox.askyesno('Exit','Are you sure want to do this operation ')
            #if result == True:# go to database and make this operation
            #else:
               # messagebox.showinfo('info','Done')

    
        btn_add=Button(btn_frame,text='Add Details',width=10,height=1,padx= 10,pady=10,font=('Ashkar',14),fg='#6b9080',bg='#f6fff8',bd=2,command=sure).place(x=4,y=5)
        btn_delete=Button(btn_frame,text='Delete Details',width=10,height=1,padx= 10,pady=10,font=('Ashkar',14),fg='#6b9080',bg='#f6fff8',bd=2,command=sure).place(x=170,y=5)
        btn_update=Button(btn_frame,text='Update Details',width=10,height=1,padx= 10,pady=10,font=('Ashkar',14),fg='#6b9080',bg='#f6fff8',bd=2,command=sure).place(x=4,y=50)
        btn_clear=Button(btn_frame,text='Clear Details',width=10,height=1,padx= 10,pady=10,font=('Ashkar',14),fg='#6b9080',bg='#f6fff8',bd=2,command=sure).place(x=170,y=50)
        #=============Table Frame===============#
        tree_farm=Frame(root,bg='#f6fff8')
        tree_farm.place(x=450,y=1,width=875,height=610)
        style=ttk.Style()
        style.configure("mystyle.Treeview",font=('Ashkar',13),rowheight=60)
        style.configure("mystyle.Treeview.Heading",font=('Ashkar',13))
        tv=ttk.Treeview(tree_farm,columns=(1,2,3,4,5,6,7),style="mystyle.Treeview")
        
        tv.heading("1",text="ID")
        tv.column("1", width=40)
        
        tv.heading("2",text="Name")
        tv.column("2", width=140)
        
        tv.heading("3",text="GPA")
        tv.column("3", width=50)
        
        tv.heading("4",text="Section")
        tv.column("4", width=120)
        
        tv.heading("5",text="level")
        tv.column("5", width=60)
        
        tv.heading("6",text="Email")
        tv.column("6", width=150)
        
        tv.heading("7",text="Address")
        tv.column("7", width=180)
        
        tv['show']='headings'
        tv.place(x=1,y=1,height=610,width=875)
        #=======define==============#
        def hide():
            self.root.geometry("360x510")
        def show():
            self.root.geometry('1210x615+0+0')
            
        btnhide=Button(entries_frame,text='HIDE',cursor='hand2',command=hide,bd=1,relief=SOLID)
        btnhide.place(x=250,y=10)
        
        btnshow=Button(entries_frame,text='SHOW',cursor='hand2',command=show,bd=1,relief=SOLID)
        btnshow.place(x=300,y=10)
        
        
'''
root=Tk()
obj=ADMIN(root)
root.mainloop()
'''