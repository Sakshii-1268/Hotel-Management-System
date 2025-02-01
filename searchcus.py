from tkinter import *
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk , Image
import time
import mysql.connector
from tkinter import messagebox
from time import strftime
import cv2
import pyttsx3
from datetime import datetime


def main():
    win = Tk()
    app = search_cust(win)
    win.mainloop()
    
class search_cust:
    def __init__(self,root):
        self.root = root
        self.root.title("New Customer Booking")
        self.root.geometry("1100x600+70+25")
        self.root.resizable(0,0)

        
        self.frame3 = Frame(self.root,bg='aquamarine4')
        self.frame3.place(x=0,y=0,height=600,width=1100)
        # ================== Frame  ================================= 
        self.table_frame = LabelFrame(self.frame3,relief=RIDGE,text="Search Customer Details",bg="aquamarine",font=("Arial",12,"bold"),padx=2)
        self.table_frame.place(x=20,y=20,width=1050,height=570)
 
        # ===================== Search By Number ========================
        searchby = Label(self.table_frame,text="Enter phone Number : ",bg="aquamarine1",font=("Arial",10,"bold"))
        searchby.place(x=10,y=10)

        self.search = StringVar()
        searchby_entry = ttk.Entry(self.table_frame,textvariable=self.search,font=("Arial",15,"bold"),width=29)
        searchby_entry.place(x=170,y=10,width=250)

        # =================== Fetch Button =============================
        get = Button(self.table_frame,text="Fetch Data",command=self.get_data,bg="black",fg="gold",cursor="hand2")
        get.place(x=450,y=10,width=100)
        
    
    # ======================== fetch data function =======================
    def get_data(self):
        if self.search.get() == "":
            messagebox.showerror("Error","Please Enter the Phone Number",parent=self.root)
            engine = pyttsx3.init()
            engine.say("Please Enter the Phone Number")
            engine.runAndWait()
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
            my_cursor = conn.cursor()
            # ===================== Name fetch =================================
            query = ("Select name from customer where mobile=%s")
            value = (self.search.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","This Number Not Found",parent=self.root)
                engine = pyttsx3.init()
                engine.say("This Number Not Found")
                engine.runAndWait()               
            else:
                conn.commit()
                conn.close()

                showdataframe = Frame(self.table_frame,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=70,y=70,width=900,height=400)

                lblname = Label(showdataframe,text='Name : ',font=("Arial",15,"bold"))
                lblname.place(x=0,y=5)

                lblname1 = Label(showdataframe,text=row,font=("Arial",15,"bold"))
                lblname1.place(x=130,y=5)

                # ==================== Age fetch ================================
                conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
                my_cursor = conn.cursor()
                query = ("Select age from customer where mobile=%s")
                value = (self.search.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblage = Label(showdataframe,text='Age : ',font=("Arial",15,"bold"))
                lblage.place(x=0,y=50)

                lblage1 = Label(showdataframe,text=row,font=("Arial",15,"bold"))
                lblage1.place(x=130,y=50)

                # ==================== Gender fetch ================================
                conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
                my_cursor = conn.cursor()
                query = ("Select gender from customer where mobile=%s")
                value = (self.search.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblage = Label(showdataframe,text='Gender :',font=("Arial",15,"bold"))
                lblage.place(x=0,y=100)

                lblage1 = Label(showdataframe,text=row,font=("Arial",15,"bold"))
                lblage1.place(x=130,y=100)

                # ==================== Email fetch ================================
                conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
                my_cursor = conn.cursor()
                query = ("Select email from customer where mobile=%s")
                value = (self.search.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblage = Label(showdataframe,text='Email : ',font=("Arial",15,"bold"))
                lblage.place(x=0,y=150)

                lblage1 = Label(showdataframe,text=row,font=("Arial",15,"bold"))
                lblage1.place(x=130,y=150)

                # ==================== Id Number ================================
                conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
                my_cursor = conn.cursor()
                query = ("Select idno from customer where mobile=%s")
                value = (self.search.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblage = Label(showdataframe,text='ID No. : ',font=("Arial",15,"bold"))
                lblage.place(x=0,y=200)

                lblage1 = Label(showdataframe,text=row,font=("Arial",15,"bold"))
                lblage1.place(x=130,y=200)
                
                # ==================== Check in ================================
                conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
                my_cursor = conn.cursor()
                query = ("Select checkin from customer where mobile=%s")
                value = (self.search.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblage = Label(showdataframe,text='check In : ',font=("Arial",15,"bold"))
                lblage.place(x=0,y=250)

                lblage1 = Label(showdataframe,text=row,font=("Arial",15,"bold"))
                lblage1.place(x=130,y=250)

                # ==================== Room Type ================================
                conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
                my_cursor = conn.cursor()
                query = ("Select roomtype from customer where mobile=%s")
                value = (self.search.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblage = Label(showdataframe,text='Room Type : ',font=("Arial",15,"bold"))
                lblage.place(x=0,y=300)

                lblage1 = Label(showdataframe,text=row,font=("Arial",15,"bold"))
                lblage1.place(x=130,y=300)

                # ==================== Amount ================================
                conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
                my_cursor = conn.cursor()
                query = ("Select amount from customer where mobile=%s")
                value = (self.search.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblage = Label(showdataframe,text='Amount : ',font=("Arial",15,"bold"))
                lblage.place(x=0,y=350)

                lblage1 = Label(showdataframe,text=row,font=("Arial",15,"bold"))
                lblage1.place(x=130,y=350)

                # ==================== Bill Paid ================================
                conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
                my_cursor = conn.cursor()
                query = ("Select billpaid from customer where mobile=%s")
                value = (self.search.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblage = Label(showdataframe,text='Amount Paid: ',font=("Arial",15,"bold"))
                lblage.place(x=300,y=5)

                lblage1 = Label(showdataframe,text=row,font=("Arial",15,"bold"))
                lblage1.place(x=450,y=5)

                # ==================== Balance ================================
                conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
                my_cursor = conn.cursor()
                query = ("Select balance from customer where mobile=%s")
                value = (self.search.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblage = Label(showdataframe,text='Balance : ',font=("Arial",15,"bold"))
                lblage.place(x=300,y=50)

                lblage1 = Label(showdataframe,text=row,font=("Arial",15,"bold"))
                lblage1.place(x=450,y=50)

                # ================== Image ===================================
                imgno = self.search.get()
                path = "{}.png".format(imgno) 
                img = Image.open(path)
                img =img.resize((250,250)) 
                self.img= ImageTk.PhotoImage(img)
                image_C = Label(showdataframe,image=self.img,bg="black",borderwidth=0)
                image_C.place(x=550,y=100,width=250,height=250)

        




if __name__ == "__main__":
    main()
    