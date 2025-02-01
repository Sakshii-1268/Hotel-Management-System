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
    app = roomdetails(win)
    win.mainloop()
    
class roomdetails:
    def __init__(self,root):
        self.root = root
        self.root.title("New Customer Booking")
        self.root.geometry("1100x600+70+25")

        self.frame3 = Frame(self.root,bg='aquamarine1')
        self.frame3.place(x=0,y=0,height=600,width=1100)

        table_frame = LabelFrame(self.frame3,relief=RIDGE,text="Room Details",font=("Arial",12,"bold"),padx=2)
        table_frame.place(x=100,y=50,width=900,height=490)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.room_table = ttk.Treeview(table_frame,columns=("Room No","Floor","Room Type"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        self.room_table.heading("Room No",text="Room No")
        self.room_table.heading("Floor",text="Floor")
        self.room_table.heading("Room Type",text="Room Type")
        
        self.room_table["show"] = "headings"

        self.room_table.column("Room No",width=100)
        self.room_table.column("Floor",width=100)
        self.room_table.column("Room Type",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    # =========================== Fetch function for room ======================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.roomno.set(row[0]),
        self.floor.set(row[1]),
        self.roomtype.set(row[2])


        
        
  
        

if __name__ == "__main__":
    main()