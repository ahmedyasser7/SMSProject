from tkinter import *
from tkinter import StringVar
from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk
from db import Database

        
db =Database("student.db")

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)
        


def delete():
    db.remove(row[0])
    Clear()
    displayAll()
        
        

def Clear():
    
    txtName.delete("0",END)  
    txtGPA.delete("0",END)
    txtemail.delete("0",END)
    txtsection.delete("0",END)
    txtlevel.delete("0",END)
    txtaddress.delete("0",END)

    
def get_data(event):
    selected_row=tv.focus()
    data1=tv.item(selected_row)
    global row
    row=data1["values"]
    name.set(row[1])
    gpa.set(row[2])
    email.set(row[3])
    section.set(row[4])
    level.set(row[5])
    address.set(row[6])
    
    

def add():
    if  txtName.get()== "" or txtGPA.get()== "" or txtemail.get()== "" or txtsection.get()== "" or txtlevel.get()== "" or txtaddress.get()== "":
        messagebox.showerror("Error","please fill all the entry")
        return
    db.insert(
        
        txtName.get(),
        txtGPA.get(),
        txtemail.get(),
        txtsection.get(),
        txtlevel.get(),
        txtaddress.get()
        )
    messagebox.showinfo("Success","Added new student")
    Clear()
    displayAll()



def update1():
    if  txtName.get()== "" or txtGPA.get()== "" or txtemail.get()== "" or txtsection.get()== "" or txtlevel.get()== "" or txtaddress.get()== "":
        messagebox.showerror("Error","please fill all the entry")
        return
    db.update(row[0],
        txtName.get(),
        txtGPA.get(),
        txtemail.get(),
        txtsection.get(),
        txtlevel.get(),
        txtaddress.get()
        )
    
    messagebox.showinfo("Success","the student data is update")
    Clear()
    displayAll()


    
    




root = Tk()   #
root.geometry('1240x620')
#------------Entries Frame------------
Entries_frame = Frame(root, bg ='#6b9080')
Entries_frame.place(x=1, y=1, width=1000, height=690)
title = Label(Entries_frame, text="student service potel ", font=('Calibri', 18, 'bold'),bg= '#6b9080', fg='white' )
title.place(x=10, y=1)

id=IntVar()
name=StringVar() 
gpa=StringVar()
email=StringVar()
section=StringVar()
level =StringVar()
address=StringVar()


lblName = Label(Entries_frame, text="Name :", font=('Calibri bold', 16),bg= '#6b9080', fg='white',bd=1)
lblName.place(x=10, y= 90)
txtName = Entry(Entries_frame, width=20,font=('Calibri ', 15),textvariable=name )
txtName.place(x=130, y = 90)



lblgpa = Label(Entries_frame, text="GPA :", font=('Calibri bold', 16),bg= '#6b9080', fg='white',bd=1)
lblgpa.place(x=10, y= 130)
txtGPA = Entry(Entries_frame, width=20,font=('Calibri ', 15),textvariable=gpa )
txtGPA.place(x=130, y = 130)


lblemail = Label(Entries_frame, text="Email:", font=('Calibri bold', 16),bg= '#6b9080', fg='white',bd=1)
lblemail.place(x=10, y= 170)
txtemail = Entry(Entries_frame, width=20,font=('Calibri ', 15),textvariable=email )
txtemail.place(x=130, y = 170)


lblsetion = Label(Entries_frame, text="Section :", font=('Calibri bold', 16),bg= '#6b9080', fg='white',bd=1)
lblsetion.place(x=10, y= 210)
txtsection = ttk.Combobox(Entries_frame,state='readonly',width=18,font=('Calibri ', 15),textvariable=section )
txtsection['values']=("CS","IS","AI","SC")
txtsection.place(x=130, y = 210)


lbllevel = Label(Entries_frame, text="Level :", font=('Calibri bold', 16),bg= '#6b9080', fg='white',bd=1)
lbllevel.place(x=10, y= 250)
txtlevel = ttk.Combobox(Entries_frame,state='readonly',width=18,font=('Calibri ', 15),textvariable=level)
txtlevel['values']=("one","two","thrid","fourth")
txtlevel.place(x=130, y = 250)


lbladdress = Label(Entries_frame, text="Address", font=('Calibri bold', 16),bg= '#6b9080', fg='white',bd=1)
lbladdress.place(x=10, y= 290)
txtaddress = Entry(Entries_frame,width=20,font=('Calibri ', 15) ,textvariable=address)
txtaddress.place(x=130, y = 290)

#------------Buttons------------
btn_frame = Frame(Entries_frame, bg='#6b9080', bd= 1 , relief= SOLID)
btn_frame.place(x=15, y= 390,width=335, height=100)


btnAdd= Button(btn_frame,
               text="Add Details",
               width=14,
               height=1,
               font=("calibri", 16),
               fg='#6b9080',
               bg = '#f6fff8',
               bd=0, command=add
               ).place(x=4, y=5)


btnEdit= Button(btn_frame,
               text="Update Details",
               width=14,
               height=1,
               font=("calibri", 16),
               fg='#6b9080',
               bg = '#f6fff8',
               bd=0, command=update1
               ).place(x=4, y=50)


btnDelete= Button(btn_frame,
               text="Delete Details",
               width=14,
               height=1,
               font=("calibri", 16),
               fg='#6b9080',
               bg = '#f6fff8',
               bd=0,command=delete
               ).place(x=170, y=5)


btnClear= Button(btn_frame,
               text="Clear Details",
               width=14,
               height=1,
               font=("calibri", 16),
               fg='#6b9080',
               bg = '#f6fff8',
               bd=0,command=Clear
               ).place(x=170, y=50)



#------------Table Frame------------

tree_frame = Frame(root, bg='white')
tree_frame.place(x=365, y = 1, width=875, height=615)
style = ttk.Style()
#style.theme_use('clam')
style.configure('Treeview',background='#6b9080',font=('Arial',12),rowheight=30,foreground='#e5e5e5')
style.map('Treeview',foreground=[('selected','black')],background=[('selected', '#f6fff8')])
style.configure('Treeview.Heading',font=('Arial',14))
#style.configure("mystyle.Treeview", font=('Calibri', 13), rowheight=50)
#style.configure("mystyle.Treeview.Heading", font=('Calibri', 13))


tv = ttk.Treeview(tree_frame, columns=(1,2,3,4,5,6,7), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width="40",anchor='c')

tv.heading("2", text="Name")
tv.column("2", width="140",anchor='c')

tv.heading("5", text="gpa")
tv.column("5", width="50",anchor='c')

tv.heading("3", text="email")
tv.column("3", width="120",anchor='c')

tv.heading("4", text="section")
tv.column("4", width="150",anchor='c')

tv.heading("6", text="level")
tv.column("6", width="150",anchor='c')

tv.heading("7", text="address")
tv.column("7", width="100",anchor='c')

tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>",get_data)
tv.place(x=1, y= 1, height=610, width=875)
displayAll()
root.mainloop()