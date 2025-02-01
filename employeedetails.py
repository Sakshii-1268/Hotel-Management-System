from tkinter import *
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk , Image
import time
import mysql.connector
from tkinter import messagebox
from time import strftime
import cv2
from datetime import datetime


def main():
    win = Tk()
    app = employeedetails(win)
    win.mainloop()
    
class employeedetails:
    def __init__(self,root):
        self.root = root
        self.root.title("New Customer Booking")
        self.root.geometry("1100x600+70+25")
        self.root.resizable(0,0)

        self.frame3 = Frame(self.root,bg='aquamarine1')
        self.frame3.place(x=0,y=0,height=600,width=1100)

        table_frame = LabelFrame(self.frame3,relief=RIDGE,text="Employee Details",font=("Arial",12,"bold"),padx=2)
        table_frame.place(x=100,y=50,width=900,height=490)
   
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.emp_table = ttk.Treeview(table_frame,columns=("Name","Age","Gender","Job","Salary","Phone","Adhaar No","Email"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.emp_table.xview)
        scroll_y.config(command=self.emp_table.yview)

        self.emp_table.heading("Name",text="Name")
        self.emp_table.heading("Age",text="Age")
        self.emp_table.heading("Gender",text="Gender")
        self.emp_table.heading("Job",text="Job")
        self.emp_table.heading("Salary",text="Salary")
        self.emp_table.heading("Phone",text="Phone")
        self.emp_table.heading("Adhaar No",text="Adhaar No")
        self.emp_table.heading("Email",text="Email")
        
        self.emp_table["show"] = "headings"

        self.emp_table.column("Name",width=100)
        self.emp_table.column("Age",width=100)
        self.emp_table.column("Gender",width=100)
        self.emp_table.column("Job",width=100)
        self.emp_table.column("Salary",width=100)
        self.emp_table.column("Phone",width=100)
        self.emp_table.column("Adhaar No",width=100)
        self.emp_table.column("Email",width=100)
        
        self.emp_table.pack(fill=BOTH,expand=1)
        self.emp_table.bind("<ButtonRelease>",self.get_cursor1)
        self.fetch_data1()

    
    # =================== Fetch data from Employee =========================
    def fetch_data1(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
        my_cursor = conn.cursor()
        my_cursor.execute("select * from emp")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.emp_table.delete(*self.emp_table.get_children())
            for i in rows:
                self.emp_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    # ==================== Cursor function of employee ========================
    def get_cursor1(self,event=""):
        cursor_row = self.emp_table.focus()
        content = self.emp_table.item(cursor_row)
        row = content["values"]

        self.ename.set(row[0]),
        self.age.set(row[1]),
        self.gender.set(row[2]),
        self.job.set(row[3]),
        self.salary.set(row[4]),
        self.phone.set(row[5]),
        self.adhar.set(row[6]),
        self.email.set(row[7])
    



if __name__ == "__main__":
    main()
    