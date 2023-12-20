from tkinter import *
from tkinter import messagebox,ttk
from to_student import *
# import db
class STUDENT:
    def __init__ (self , root):
        self.root=root
        self.root.title('student manemant system')
        self.root.geometry('1000x615+0+0')
        self.root.resizable(False,False)
        self.root.configure(bg='#6b9080')
        
        #===============student_info Frame=============#
        student_info=Frame(self.root,bg='#6b9080')
        
        lb1_ID=Label(student_info,text='ID: ',font=('Ashkar',16),bg='#6b9080',fg='#f6fff8')
        lb1_ID.grid(row= 0, column= 0)
        text_ID=Entry(student_info,width=20,font=('Ashkar',16))
        text_ID.grid(row= 0, column= 1)
        lb1_name=Label(student_info,text='Name: ',font=('Ashkar',16),bg='#6b9080',fg='#f6fff8')
        lb1_name.grid(row= 1, column=0)
        text_name=Entry(student_info,width=20,font=('Ashkar',16))
        text_name.grid(row= 1,column=1)
        
        lb1_gba=Label(student_info,text='GPA: ',font=('Ashkar',16),bg='#6b9080',fg='#f6fff8')
        lb1_gba.grid(row= 2, column= 0)
        text_gba=Entry(student_info,width=20,font=('Ashkar',16))
        text_gba.grid(row= 2, column= 1)
        
        lb1_email=Label(student_info,text='Email: ',font=('Ashkar',16),bg='#6b9080',fg='#f6fff8')
        lb1_email.grid(row= 3, column= 0)
        text_email=Entry(student_info,width=20,font=('Ashkar',16))
        text_email.grid(row=3, column=1)
        
        lb1_section=Label(student_info,text='Section: ',font=('Ashkar',16),bg='#6b9080',fg='#f6fff8')
        lb1_section.grid(row= 4, column= 0)
       
        text_section=Entry(student_info,width=20,font=('Ashkar',16))
        text_section.grid(row= 4,column= 1)
    
        
        lb1_level=Label(student_info,text='Level: ',font=('Ashkar',16),bg='#6b9080',fg='#f6fff8')
        lb1_level.grid(row=5, column=0)
        
        text_level=Entry(student_info,width=20,font=('Ashkar',16))
        text_level.grid(row= 5, column=1)
        
        
        lb1_address=Label(student_info,text='Address: ',font=('Ashkar',16),bg='#6b9080',fg='#f6fff8')
        lb1_address.grid(row= 6, column= 0)
        text_address=Entry(student_info,width=20,font=('Ashkar',16))
        text_address.grid(row=6, column= 1)
        """ def go_back():
            student_info.destroy()
            frame()
        """
        """btn=Button(student_info,text='Back',bg='#6b9080',fg= '#f6fff8',width = 10,height =2,relief=RAISED,
        font=('Ashkar Bold', 14), command=go_back)
        btn.grid(row = 7, column= 0,columnspan=2)"""
        student_info.place(anchor='center', relx = 0.5, rely =0.5)
        
        
    
'''    
root=Tk()
obj=STUDENT(root)
root.mainloop()
'''
    


