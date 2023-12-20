import  sqlite3
from tkinter import *
import admin1
conn=sqlite3.connect("run4.db")
conn.execute("""
CREATE TABLE ADMIN(
ADMIN_ID INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL ,
USERNAME TEXT NOT NULL, 
PASSWORD TEXT NOT NULL)
""")

print ("Table ADMIN created successfully")

conn.execute("INSERT INTO ADMIN(USERNAME,PASSWORD) VALUES ('admin', 'admin789')");

conn.execute("INSERT INTO ADMIN(USERNAME,PASSWORD) VALUES ('krazy', 'krazy789')");

conn.commit()
print ("Records inserted successfully")
#conn.close()

cursor = conn.execute("SELECT * from ADMIN")
print("ID\tUSERNAME\tPASSWORD")
for row in cursor:
   print ("{}\t{}\t\t{}".format(row[0],row[1],row[2]))
conn.close()

def login():
    #getting form data
    uname=username.get()
    pwd=password.get()
    #applying empty validation
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
      #open database
      conn = sqlite3.connect('strr.db')
      #select query
      cursor = conn.execute('SELECT * from ADMIN where USERNAME="%s" and PASSWORD="%s"'%(uname,pwd))
      #fetch data 
      if cursor.fetchone():
          admin1.displayAll()
          message.set("Login success")
       
       
      else:
       message.set("Wrong username or password!!!")
#defining loginform function
def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("login")
    #setting height and width of screen
    login_screen.geometry("350x350")
    login_screen["bg"]="#6b9080"
    #declaring variable
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login form
    Label(login_screen,width="300", text="Login From",font=('Ashkar',14,'bold'),fg='#f6fff8', bg='#6b9080').pack()
    #Username Label
    Label(login_screen, text="Username * ",font=('Ashkar',14,'bold'),fg='#f6fff8', bg='#6b9080').place(x=20,y=40)
    #Username textbox
    Entry(login_screen, textvariable=username).place(x=120,y=42)
    #Password Label
    Label(login_screen, text="Password * ",font=('Ashkar',14,'bold'),fg='#f6fff8', bg='#6b9080').place(x=20,y=80)
    #Password textbox
    Entry(login_screen, textvariable=password ,show="*").place(x=120,y=82)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message,font=('Ashkar',14,'bold'),fg='#f6fff8', bg='#6b9080').place(x=95,y=120)
    #Login button
    Button(login_screen, text="Login", width=10, height=1, command=login,font=('Ashkar',14,'bold'),fg='#f6fff8', bg='#6b9080').place(x=125,y=170)
    login_screen.mainloop()
#calling function Loginform
Loginform()