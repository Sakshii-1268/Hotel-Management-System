from tkinter import *
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk , Image
import time
import mysql.connector
import pyttsx3
from tkinter import messagebox
from time import strftime
import cv2
from datetime import datetime



def main():
    win = Tk()
    app = customer(win)
    win.mainloop()
    
class customer:
    def __init__(self,root):
        self.root = root
        self.root.title("New Customer Booking")
        self.root.geometry("1100x600+70+25")
        self.root.resizable(0,0)
        
        self.root1 = Frame(self.root,bg='aquamarine2')
        self.root1.place(x=0,y=0,height=600,width=1100)


        welcome = Label(self.root1,text="Add Customer Details",bg='aquamarine2',font=("Algerian",15,"bold"))
        welcome.place(x=200,y=10)
        
        # ============== Customer Name ================================
        self.cname = StringVar()
        cname = Label(self.root1,text="Name : ",bg='aquamarine2',font=("Garamond",17))
        cname.place(x=5,y=50)

        cname_entry = ttk.Entry(self.root1,textvariable=self.cname,font=("Arial",15,))
        cname_entry.place(x=180,y=50,width=250)

        # =================== Customer Age =============================
        self.cage = StringVar()
        cage = Label(self.root1,text="Age : ",bg='aquamarine2',font=("Garamond",17))
        cage.place(x=5,y=100)

        cage_entry = ttk.Entry(self.root1,textvariable=self.cage,font=("Arial",15,))
        cage_entry.place(x=180,y=100,width=250)
        
        # =================== Customer Age =============================
        self.cgender = StringVar()
        cgender = Label(self.root1,text="Gender : ",bg='aquamarine2',font=("Garamond",17))
        cgender.place(x=5,y=150)

        combocgender = ttk.Combobox(self.root1,textvariable=self.cgender,font=("Arial",15),state="readonly")
        combocgender["value"] = ("Male","Female")
        combocgender.current(0)
        combocgender.place(x=180,y=150,width=250)
                
        # =================== Customer mobile =============================
        self.mobile = StringVar()
        cmobile = Label(self.root1,text="Mobile : ",bg='aquamarine2',font=("Garamond",17))
        cmobile.place(x=5,y=200)

        cmobile_entry = ttk.Entry(self.root1,textvariable=self.mobile,font=("Arial",15),width=29)
        cmobile_entry.place(x=180,y=200,width=250)

        # =================== Customer email =============================
        self.cemail = StringVar()
        cemail = Label(self.root1,text="Email : ",bg='aquamarine2',font=("Garamond",17))
        cemail.place(x=5,y=250)

        cemail_entry = ttk.Entry(self.root1,textvariable=self.cemail,font=("Arial",15),width=29)
        cemail_entry.place(x=180,y=250,width=250)

        # =================== Id proof ====================================
        self.cid = StringVar()
        cid = Label(self.root1,text="Id Proof : ",bg='aquamarine2',font=("Garamond",17))
        cid.place(x=5,y=300)
    
        comboidproof = ttk.Combobox(self.root1,textvariable=self.cid,font=("Arial",15),state="readonly")
        comboidproof["value"] = ("Adhaar card","Pan card","Driving Licence")
        comboidproof.current(0)
        comboidproof.place(x=180,y=300,width=250)

        # =================== Id Number ======================
        self.cidno = StringVar()
        cidno = Label(self.root1,text="Id Number : ",bg='aquamarine2',font=("Garamond",17))
        cidno.place(x=5,y=350)
  
        cidno_entry = ttk.Entry(self.root1,textvariable=self.cidno,font=("Arial",15),width=29)
        cidno_entry.place(x=180,y=350,width=250)

        # =============== Chech in date =======================
        self.checkin = StringVar()
        checkin = Label(self.root1,text="Check In Date : ",bg='aquamarine2',font=("Garamond",17))
        checkin.place(x=5,y=400)

        self.checkin_entry = ttk.Entry(self.root1,textvariable=self.checkin,font=("Arial",15),width=29)
        self.checkin_entry.place(x=180,y=400,width=250)
        self.checkin_entry.insert(0,"dd/mm/yyyy")
        self.checkin_entry.bind("<1>",self.pick_date)
   
        # =============== Chech out date =======================
        self.checkout = StringVar()
        checkout = Label(self.root1,text="Check Out Date : ",bg='aquamarine2',font=("Garamond",17))
        checkout.place(x=5,y=450)

        self.checkout_entry = ttk.Entry(self.root1,textvariable=self.checkout,font=("Arial",15),width=29)
        self.checkout_entry.place(x=180,y=450,width=250)
        self.checkout_entry.insert(0,"dd/mm/yyyy")
        self.checkout_entry.bind("<1>",self.pick_date1)

        # ================ No of days =========================
        self.noofdays = StringVar()
        noofdays = Label(self.root1,text="No of Days : ",bg='aquamarine2',font=("Garamond",17))
        noofdays.place(x=5,y=500)
       
        noofdays_entry = ttk.Entry(self.root1,textvariable=self.noofdays,font=("Arial",15),width=29,state="readonly")
        noofdays_entry.place(x=180,y=500,width=250)

        # ================== Generate days ====================
        g_days = Button(self.root1,text="Get Days",command=self.getnoofdays,bg="black",fg="gold",cursor="hand2")
        g_days.place(x=250,y=550,width=150)

        # ============ Room Type  ===========================
        self.roomtype = StringVar()
        roomtype = Label(self.root1,text="Room Type : ",bg='aquamarine2',font=("Garamond",17))
        roomtype.place(x=460,y=50)

        comboroomtype = ttk.Combobox(self.root1,font=("Arial",15),textvariable=self.roomtype,state="readonly")
        comboroomtype["value"] = ("Grand Heritage Room","Art Deco Suite","Luxury Suite","Non-Ac Room")
        comboroomtype.current(0)
        comboroomtype.place(x=620,y=50,width=250)

        # ================= Bed Type =======================
        self.bedtype = StringVar()
        bedtype = Label(self.root1,text="Bed Type : ",bg='aquamarine2',font=("Garamond",17))
        bedtype.place(x=460,y=100)
        
        combobedtype = ttk.Combobox(self.root1,font=("Arial",15),textvariable=self.bedtype,state="readonly")
        combobedtype["value"] = ("Single Bed","Double Bed")
        combobedtype.current(0)
        combobedtype.place(x=620,y=100,width=250)
        
        # ====================== Room No =====================
        self.roomno = StringVar()
        room_no = Label(self.root1,text="Room No : ",bg='aquamarine2',font=("Garamond",17))
        room_no.place(x=460,y=150)

        conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
        my_cursor = conn.cursor()
        my_cursor.execute("select roomno from room")
        rows = my_cursor.fetchall()

        self.comboroomno = ttk.Combobox(self.root1,font=("times new roman",13),textvariable=self.roomno,width=27,state="readonly",)
        self.comboroomno["values"] = rows
        self.comboroomno.current(0)
        self.comboroomno.place(x=620,y=150,width=250)

        
        # =================== Capture Photo ====================
        photo = Label(self.root1,text="Photo :",bg='aquamarine2',font=("Garamond",17))
        photo.place(x=460,y=200)
        
        photo = Button(self.root1,text="Capture",command=self.capture,bg="black",fg="gold",cursor="hand2")
        photo.place(x=620,y=200,width=200)


        # ===================== Total cost =====================
        self.amount1 = StringVar()
        totalcost = Label(self.root1,text="Amount : ",bg='aquamarine2',font=("Garamond",17))
        totalcost.place(x=460,y=250)

        totalcost_entry = ttk.Entry(self.root1,font=("Arial",15),textvariable=self.amount1,width=29,state="readonly")
        totalcost_entry.place(x=620,y=250,width=250)

        # ================== Generate cost ====================
        g_cost = Button(self.root1,text="Generate Amount",command=self.amount,bg="black",fg="gold",cursor="hand2")
        g_cost.place(x=700,y=300,width=150)

        # ================== Bill Paid =======================
        self.billpaid = StringVar()
        billpaid = Label(self.root1,text="Bill paid : ",bg='aquamarine2',font=("Garamond",17))
        billpaid.place(x=460,y=350)
        
        billpaid_entry = ttk.Entry(self.root1,font=("Arial",15),textvariable=self.billpaid,width=29,)
        billpaid_entry.place(x=620,y=350,width=250)

        # ================== Balance =======================
        self.balance = StringVar()
        balance = Label(self.root1,text="Balance : ",bg='aquamarine2',font=("Garamond",17))
        balance.place(x=460,y=400)

        
        balance_entry = ttk.Entry(self.root1,font=("Arial",15),textvariable=self.balance,width=29,state="readonly")
        balance_entry.place(x=620,y=400,width=250)

        # ================== Generate Balance ====================
        g_cost = Button(self.root1,text="Balance Amount ",command=self.balance1,bg="black",fg="gold",cursor="hand2")
        g_cost.place(x=700,y=450,width=150)

        # ================== Payment =============================
        payment_type = Label(self.root1,text="Payment :",bg='aquamarine2',font=("Garamond",17))
        payment_type.place(x=460,y=500)

        combopaymenttype = ttk.Combobox(self.root1,font=("Arial",15),state="readonly")
        combopaymenttype["value"] = ("Cash","Debit Card")
        combopaymenttype.current(0)
        combopaymenttype.place(x=620,y=500,width=250)

        # ================== Qr Code =========================
        or1 = Label(self.root1,text=" OR ",bg='aquamarine2',font=("Garamond",17))
        or1.place(x=870,y=500)

        bg = Image.open('myqr.png')
        bg =bg.resize((150,150)) 
        self.bg= ImageTk.PhotoImage(bg)
        lbl_bg = Label(self.root1,image=self.bg,borderwidth=0)
        lbl_bg.place(x=930,y=430,width=150,height=150)


        
        # ============= Various Btns ==========================
        reset = Button(self.root1,text="Reset",command=self.reset,bg="black",fg="gold",cursor="hand2")
        reset.place(x=550,y=550,width=100)

        add = Button(self.root1,text="Add",command=self.add_customer,bg="black",fg="gold",cursor="hand2")
        add.place(x=670,y=550,width=100)


    # ================ Add to database ==================
    def add_customer(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
        my_cursor = conn.cursor()
        my_cursor.execute("select roomno from customer")
        rows = my_cursor.fetchall()

        if self.cname.get()=="" or self.cage.get()=="" or self.cgender.get()=="" or self.mobile.get()=="" or self.cemail.get()=="" or self.cid.get()=="" or self.cidno.get()=="" or self.checkin.get()=="" or self.checkout.get()=="" or self.noofdays.get()=="" or self.roomtype.get()=="" or self.bedtype.get()=="" or self.amount1.get()=="" or self.billpaid.get()=="" or self.balance.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
            engine = pyttsx3.init()
            engine.say("All field are required")
            engine.runAndWait()
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
            my_cursor = conn.cursor()
            my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.cname.get(),
                                                                                                            self.cage.get(),
                                                                                                            self.cgender.get(),
                                                                                                            self.mobile.get(),
                                                                                                            self.cemail.get(),
                                                                                                            self.cid.get(),
                                                                                                            self.cidno.get(),
                                                                                                            self.checkin.get(),
                                                                                                            self.checkout.get(),
                                                                                                            self.noofdays.get(),
                                                                                                            self.roomtype.get(),
                                                                                                            self.bedtype.get(),
                                                                                                            self.roomno.get(),
                                                                                                            self.amount1.get(),
                                                                                                            self.billpaid.get(),
                                                                                                            self.balance.get() 
                                                                                                            ))
            conn.commit()
            conn.close()
            engine = pyttsx3.init()
            messagebox.showinfo("Success","Customer Added Succesfully",parent=self.root)
            engine.say("Customer Added Succesfully")
            selected_item = self.roomno.get()
            self.comboroomno["values"] = [item for item in self.comboroomno["values"] if item != selected_item]

            engine.runAndWait()
          #  self.root.destroy()



        # ============== Reset function =====================
    def reset(self):
        self.cname.set("")
        self.cage.set("")
        self.mobile.set("")
        self.cemail.set("")
        self.cidno.set("")
        self.checkin.set("")
        self.checkout.set("")
        self.noofdays.set("")
        self.amount1.set("")
        self.billpaid.set("")
        self.balance.set("")

    # ================== image capture ======================
    def capture(self):
        cam = cv2.VideoCapture(0)
        cascade_classifier = cv2.CascadeClassifier(r'C:\Users\sakshi yadav\Desktop\Python Project\Face Detect\haarcascades\haarcascade_frontalface_default.xml')
        cv2.namedWindow("python webcam")
        img_counter = 0
        while True:
            ret,frame = cam.read()
            frame = cv2.cvtColor(frame,0)
            detections = cascade_classifier.detectMultiScale(frame)
            if(len(detections) > 0):
                (x,y,w,h) = detections[0]
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            if not ret:
                print("failed")
                break
            cv2.imshow("test",frame)
            k = cv2.waitKey(1)
            if k%256 == 27:
                print("Esc hit")
                break
            elif k%256 == 32:
                name = self.mobile.get()
                img_name = "{}.png".format(name)
                cv2.imwrite(img_name,frame)
                print("ss taken")
                img_counter += 1
        cam.release()
        cam.destroyAllWindows()
        
    # ============= Calaculate balance ==================
    def balance1(self):
        paid = float(self.billpaid.get())
        total = float(self.amount1.get())
        bal = float(total - paid)
        self.balance.set(bal)
        
    # =============== Amount function  ====================
    def amount(self):
        single_p = float(500)
        double_p = float(1000)
        grand_p = float(1000)
        art_p = float(1500)
        luxury_P = float(2000)
        nonac_p = float(700)
        days = float(self.noofdays.get())

        if self.bedtype.get() == 'Single Bed' and self.roomtype.get() == 'Grand Heritage Room':
            total = float((single_p + grand_p) * days)
            self.amount1.set(total)
        elif self.bedtype.get() == 'Double Bed' and self.roomtype.get() == 'Grand Heritage Room':
            total = float((double_p + grand_p) * days)
            self.amount1.set(total)
        elif self.bedtype.get() == 'Single Bed' and self.roomtype.get() == 'Art Deco Suite':
            total = float((single_p + art_p) * days)
            self.amount1.set(total)
        elif self.bedtype.get() == 'Double Bed' and self.roomtype.get() == 'Art Deco Suite':
            total = float((double_p + art_p) * days)
            self.amount1.set(total)
        elif self.bedtype.get() == 'Single Bed' and self.roomtype.get() == 'Luxury Suite':
            total = float((single_p + luxury_P) * days)
            self.amount1.set(total) 
        elif self.bedtype.get() == 'Double Bed' and self.roomtype.get() == 'Luxury Suite':
            total = float((double_p + luxury_P) * days)
            self.amount1.set(total)
        elif self.bedtype.get() == 'Single Bed' and self.roomtype.get() == 'Non-Ac Room':
            total = float((single_p + nonac_p) * days)
            self.amount1.set(total)
        elif self.bedtype.get() == 'Double Bed' and self.roomtype.get() == 'Non-Ac Room':
            total = float((double_p + nonac_p) * days)
            self.amount1.set(total)

    # ================= Get no of days Function =================   
    def getnoofdays(self):
        indate = self.checkin.get()
        outdate = self.checkout.get()
        indate = datetime.strptime(indate,"%d/%m/%Y")
        outdate = datetime.strptime(outdate,"%d/%m/%Y")
        self.noofdays.set(abs(outdate-indate).days)

    # =========== Date function =======================
    def pick_date(self,event):
        self.date_window = Toplevel()
        self.date_window.grab_set()
        self.date_window.title("Select the date")
        self.date_window.geometry("250x220+420+370")
        self.cal = Calendar(self.date_window, selectmode="day",date_pattern='dd/mm/y')
        self.cal.place(x=0,y=0)

        submit_btn = Button(self.date_window,text="OK",command=self.grab_date)
        submit_btn.place(x=50,y=190)

    # ================== Date function 2 ======================   
    def grab_date(self):
        self.checkin_entry.delete(0, END)
        self.checkin_entry.insert(0,self.cal.get_date())
        self.date_window.destroy()
    
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
    