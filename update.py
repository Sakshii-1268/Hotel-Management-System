from tkinter import *
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk , Image
import time
import mysql.connector
from tkinter import messagebox


def main():
    win = Tk()
    app = update(win)
    win.mainloop()

class update:
    def __init__(self,root):
        self.root = root
        self.root.title("Upadate Customer Details")
        self.root.geometry("1100x600+70+25")
        self.frame3 = Frame(self.root,bg='aquamarine3')
        self.frame3.place(x=0,y=0,height=600,width=1100)
        # ================== Frame  ================================= 
        self.table_frame = LabelFrame(self.frame3,relief=RIDGE,text="Search Customer Details",bg="aquamarine1",font=("Arial",12,"bold"),padx=2)
        self.table_frame.place(x=100,y=50,width=900,height=500)
 
        # ===================== Search By Number ========================
        searchby = Label(self.table_frame,text="Enter phone Number : ",bg="aquamarine1",font=("Arial",10,"bold"))
        searchby.place(x=10,y=10)

        self.search = StringVar()
        searchby_entry = ttk.Entry(self.table_frame,textvariable=self.search,font=("Arial",15,"bold"),width=29)
        searchby_entry.place(x=170,y=10,width=250)

        # =================== Fetch Button =============================
        get = Button(self.table_frame,text="Fetch Data",bg="black",command=self.get_data,fg="gold",cursor="hand2")
        get.place(x=450,y=10,width=100)

        # ============== Customer Name ================================
        self.cname = StringVar()
        cname = Label(self.table_frame,text="Name : ",bg='aquamarine1',font=("Garamond",17))
        cname.place(x=50,y=50)

        cname_entry = ttk.Entry(self.table_frame,textvariable=self.cname,font=("Arial",15,))
        cname_entry.place(x=230,y=50,width=250)

        # =================== Customer Age =============================
        self.cage = StringVar()
        cage = Label(self.table_frame,text="Age : ",bg='aquamarine1',font=("Garamond",17))
        cage.place(x=50,y=100)

        cage_entry = ttk.Entry(self.table_frame,textvariable=self.cage,font=("Arial",15,))
        cage_entry.place(x=230,y=100,width=250)
        
        # =================== Customer Age =============================
        self.cgender = StringVar()
        cgender = Label(self.table_frame,text="Gender : ",bg='aquamarine1',font=("Garamond",17))
        cgender.place(x=50,y=150)

        combocgender = ttk.Combobox(self.table_frame,textvariable=self.cgender,font=("Arial",15),state="readonly")
        combocgender["value"] = ("Male","Female")
        combocgender.current(0)
        combocgender.place(x=230,y=150,width=250)
                
        # =================== Customer mobile =============================
        self.mobile = StringVar()
        cmobile = Label(self.table_frame,text="Mobile : ",bg='aquamarine1',font=("Garamond",17))
        cmobile.place(x=50,y=200)

        cmobile_entry = ttk.Entry(self.table_frame,textvariable=self.mobile,font=("Arial",15),width=29)
        cmobile_entry.place(x=230,y=200,width=250)

        # =================== Customer email =============================
        self.cemail = StringVar()
        cemail = Label(self.table_frame,text="Email : ",bg='aquamarine1',font=("Garamond",17))
        cemail.place(x=50,y=250)

        cemail_entry = ttk.Entry(self.table_frame,textvariable=self.cemail,font=("Arial",15),width=29)
        cemail_entry.place(x=230,y=250,width=250)

        # =============== Chech out date =======================
        self.checkout = StringVar()
        checkout = Label(self.table_frame,text="Check Out Date : ",bg='aquamarine1',font=("Garamond",17))
        checkout.place(x=50,y=300)

        self.checkout_entry = ttk.Entry(self.table_frame,textvariable=self.checkout,font=("Arial",15),width=29)
        self.checkout_entry.place(x=230,y=300,width=250)
        self.checkout_entry.insert(0,"dd/mm/yyyy")
        self.checkout_entry.bind("<1>",self.pick_date1)

        # ================== Bill Paid =======================
        self.billpaid = StringVar()
        billpaid = Label(self.table_frame,text="Bill paid : ",bg='aquamarine1',font=("Garamond",17))
        billpaid.place(x=50,y=350)
        
        billpaid_entry = ttk.Entry(self.table_frame,font=("Arial",15),textvariable=self.billpaid,width=29,)
        billpaid_entry.place(x=230,y=350,width=250)

        # ================== Balance =======================
        self.balance = StringVar()
        balance = Label(self.table_frame,text="Balance : ",bg='aquamarine1',font=("Garamond",17))
        balance.place(x=50,y=400)

        
        balance_entry = ttk.Entry(self.table_frame,font=("Arial",15),textvariable=self.balance,width=29,state="readonly")
        balance_entry.place(x=230,y=400,width=250)

    def get_data(self):
        if self.search.get() == "":
            messagebox.showerror("Error","Please Enter the Phone Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set age=%s where mobile=%s ",(
                self.cage.get(),
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Details get updated sucessfully")

   
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        conn.commit()
        conn.close()
# =========== Date function3 =======================
    def pick_date1(self,event):
        self.date_window = Toplevel()
        self.date_window.grab_set()
        self.date_window.title("Select the date")
        self.date_window.geometry("250x220+420+370")
        self.cal = Calendar(self.date_window, selectmode="day",date_pattern='dd/mm/y')
        self.cal.place(x=0,y=0)

        submit_btn = Button(self.date_window,text="OK",command=self.grab_date1)
        submit_btn.place(x=50,y=190)

    # ================== Date function 4 ======================   
    def grab_date1(self):
        self.checkout_entry.delete(0, END)
        self.checkout_entry.insert(0,self.cal.get_date())
        self.date_window.destroy()



if __name__ == "__main__":
    main()