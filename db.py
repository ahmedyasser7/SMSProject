import sqlite3
class Database():
    def __init__(self,db):

        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()

        sql="""
        CREATE TABLE if not exists student(
        id Integer Primary key autoincrement ,
        name text ,
        gpa text ,
        email text ,
        section text,
        level text,
        address text )
        
        """
        self.cur.execute(sql)
        self.con.commit() 
       
    
    def insert (self,name ,gpa,email,section,level,address):
        self.cur.execute("insert into student values (NULL,?,?,?,?,?,?)", (name ,gpa,email,section,level,address))
        self.con.commit()
       

    def fetch(self):
        self.cur.execute("SELECT * FROM student")                   
        rows=self.cur.fetchall()
        return rows 
    
    def remove(self,id):
        self.cur.execute("delete from student where id=?",(id,))
        self.con.commit()
       
        
    def update(self,id,name,gpa,email,section,level,address):
        self.cur.execute("update student set name=?,gpa=?,email=?,section=?,level=?,address=? where id=?",
                         (name ,gpa,email,section,level,address,id))
        self.con.commit()
        