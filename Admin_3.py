from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image
import time
import mysql.connector
import pyttsx3
from tkinter import messagebox
from reception import reception


def main():
    win = Tk()
    app = admin_page1(win)
    win.mainloop()


class admin_page1:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management")
        self.root.geometry("1300x650+0+0")
 
        bg = Image.open(r"Images\bg.jpg")
        bg =bg.resize((1300,650)) 
        self.bg= ImageTk.PhotoImage(bg)
        lbl_bg = Label(self.root,image=self.bg,bg="black",borderwidth=0)
        lbl_bg.place(x=0,y=0,width=1300,height=650)

        self.frame1 = LabelFrame(self.root,bd=2,relief=RIDGE,text="Menu",font=("times new roman",20,"bold"))
        self.frame1.place(x=5,y=50,width=300,height=350)

        Employee = Button(self.frame1, text="Add Employee", fg="gold" ,command=self.addemp,bg="Black",font=("Garamond",15),cursor="hand2")
        Employee.place(x=50 , y=50 ,width=200,height=30)

        Room = Button(self.frame1, text="Add Room", fg="gold" ,command=self.addroom, bg="Black",font=("Garamond",15),cursor="hand2")
        Room.place(x=50 , y=150 ,width=200,height=30)

        Driver = Button(self.frame1, text="Add Driver", fg="gold" ,command=self.adddriver, bg="Black",font=("Garamond",15),cursor="hand2")
        Driver.place(x=50 , y=250 ,width=200,height=30)

# ======================= Add Driver =================================
    
    def adddriver(self):
        self.frame3 = Frame(self.root,bg='white')
        self.frame3.place(x=400,y=50,height=500,width=850)
        
        welcome = Label(self.frame3,text="Add Driver Details",bg="white",font=("Algerian",15,"bold"))
        welcome.place(x=200,y=10)
         
        # ====================== Driver Name =====================================
        self.dname = StringVar()
        dname = Label(self.frame3,text="Name : ",bg="white",font=("Garamond",20,"bold"))
        dname.place(x=5,y=50)

        dname_entry = ttk.Entry(self.frame3,textvariable=self.dname,font=("Arial",15,))
        dname_entry.place(x=160,y=50,width=250)

        # ===================== Driver Age =====================================
        self.dage = StringVar()
        dage = Label(self.frame3,text="Age : ",bg="white",font=("Garamond",20,"bold"))
        dage.place(x=5,y=100)

        dage_entry = ttk.Entry(self.frame3,textvariable=self.dage,font=("Arial",15,))
        dage_entry.place(x=160,y=100,width=250)

        # ====================== Driver Gender =================================
        self.dgender = StringVar()
        dgender = Label(self.frame3,text="Gender : ",bg="white",font=("Garamond",20,"bold"))
        dgender.place(x=5,y=150)

        combodgender = ttk.Combobox(self.frame3,textvariable=self.dgender,font=("times new roman",15,"bold"),state="readonly")
        combodgender["value"] = ("Male","Female")
        combodgender.current(0)
        combodgender.place(x=160,y=150,width=250)

        # ====================== Driver Car =================================
        self.car = StringVar()
        car = Label(self.frame3,text="Car Name : ",bg="white",font=("Garamond",20,"bold"))
        car.place(x=5,y=200)

        car_entry = ttk.Entry(self.frame3,textvariable=self.car,font=("Arial",15,))
        car_entry.place(x=160,y=200,width=250)
   
        # ===================== Loaction ===================================
        self.loaction = StringVar()
        loaction = Label(self.frame3,text="Location : ",bg="white",font=("Garamond",20,"bold"))
        loaction.place(x=5,y=250)

        
        loaction_entry = ttk.Entry(self.frame3,textvariable=self.loaction,font=("Arial",15,))
        loaction_entry.place(x=160,y=250,width=250)

        
        # ================== Back Button =========================
        back_btn = Button(self.frame3, text="Back", fg="gold" , command=self.close,bg="Black",font=("Garamond",15),cursor="hand2")
        back_btn.place(x=50 , y=370 ,width=150,height=30)

        # ================== Add Button ===========================
        add_btn = Button(self.frame3,text="Add", fg="gold",bg="Black",command=self.add_driver1,font=("Garamond",15),cursor="hand2")
        add_btn.place(x=250 , y=370 ,width=150,height=30)
  
        # ================= Image ==============================     
        img6 = Image.open(r"Images\car.jpg")
        img6 = img6.resize((250,250)) 
        self.photoimage4= ImageTk.PhotoImage(img6)
        lblimg4 = Label(self.frame3,image=self.photoimage4,bg="black",borderwidth=0)
        lblimg4.place(x=500,y=100,width=250,height=250)

    
    # ======================= Add Driver to database =====================================
    def add_driver1(self):
        if self.dname.get()=="" or self.dage.get()=="" or self.dgender.get()=="" or self.car.get()=="" or self.loaction.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
            engine = pyttsx3.init()
            engine.say("All field are required")
            engine.runAndWait()
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
            my_cursor = conn.cursor()
            my_cursor.execute("insert into driver values(%s,%s,%s,%s,%s)",(
                                                                   self.dname.get(),
                                                                   self.dage.get(),
                                                                   self.dgender.get(),
                                                                   self.car.get(),
                                                                   self.loaction.get()
                                                                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Driver Added Succesfully",parent=self.root) 
            engine = pyttsx3.init()
            engine.say("Driver Added Succesfully")
            engine.runAndWait()
            self.frame3.destroy()







# ======================= Add Room =====================================

    def addroom(self):
        self.frame3 = Frame(self.root,bg='white')
        self.frame3.place(x=400,y=50,height=500,width=850)

        self.roomno = StringVar()
        self.floor = StringVar()
        self.roomtype = StringVar()

        welcome = Label(self.frame3,text="Add Room Details",bg="white",font=("Algerian",15,"bold"))
        welcome.place(x=200,y=10)
        # ====================== Room No =====================================
        roomno = Label(self.frame3,text="Room Number : ",bg="white",font=("Garamond",20,"bold"))
        roomno.place(x=5,y=50)

        roomno_entry = ttk.Entry(self.frame3,textvariable=self.roomno,font=("Arial",15,))
        roomno_entry.place(x=210,y=50,width=250)

        # ====================== Floor No =====================================
        floor = Label(self.frame3,text="Floor Number : ",bg="white",font=("Garamond",20,"bold"))
        floor.place(x=5,y=100)

        floor_entry = ttk.Entry(self.frame3,textvariable=self.floor,font=("Arial",15,))
        floor_entry.place(x=210,y=100,width=250)

        # ====================== Room Type =====================================
        roomtype = Label(self.frame3,text="Room Tpye : ",bg="white",font=("Garamond",20,"bold"))
        roomtype.place(x=5,y=150)

        
        comboroomtype = ttk.Combobox(self.frame3,font=("Arial",15,"bold"),textvariable=self.roomtype,state="readonly")
        comboroomtype["value"] = ("Grand Heritage Room","Art Deco Suite","Luxury Suite","Non-Ac Room")
        comboroomtype.current(0)
        comboroomtype.place(x=210,y=150,width=250)


        # ====================== Back button =====================================
        back_btn = Button(self.frame3, text="Back", fg="gold" , command=self.close,bg="Black",font=("Garamond",15),cursor="hand2")
        back_btn.place(x=50 , y=250 ,width=150,height=30)

        
        # ====================== Room Image =====================================
        img6 = Image.open(r"Images\room.jpeg")
        img6 = img6.resize((250,250)) 
        self.photoimage4= ImageTk.PhotoImage(img6)
        lblimg4 = Label(self.frame3,image=self.photoimage4,bg="black",borderwidth=0)
        lblimg4.place(x=500,y=100,width=250,height=250)

        # ====================== Add Button =====================================
        add_btn = Button(self.frame3,text="Add", fg="gold",bg="Black",command=self.add_room1,font=("Garamond",15),cursor="hand2")
        add_btn.place(x=250 , y=250 ,width=150,height=30)

     
    # ======================= Add Room to database =====================================
    def add_room1(self):
        if self.roomno.get()=="" or self.floor.get()=="" or self.roomtype.get()=="" :
            messagebox.showerror("Error","All field are required",parent=self.root)
            engine = pyttsx3.init()
            engine.say("All field are required")
            engine.runAndWait()
        
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
            my_cursor = conn.cursor()
            my_cursor.execute("insert into room values(%s,%s,%s)",(
                                                                   self.roomno.get(),
                                                                   self.floor.get(),
                                                                   self.roomtype.get()
                                                                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Room Added Succesfully",parent=self.root) 
            engine = pyttsx3.init()
            engine.say("Room Added Succesfully")
            engine.runAndWait()
            self.frame3.destroy()
  


# ======================= Add Employee =====================================
    def addemp(self):
        self.frame3 = Frame(self.root,bg='white')
        self.frame3.place(x=400,y=50,height=500,width=850)

        welcome = Label(self.frame3,text="Add Employee Details",bg="white",font=("Algerian",15,"bold"))
        welcome.place(x=200,y=10)
        
        # ====================== Emp Name =====================================
        self.ename = StringVar()
        ename = Label(self.frame3,text="Name : ",bg="white",font=("Garamond",20,"bold"))
        ename.place(x=5,y=50)

        ename_entry = ttk.Entry(self.frame3,textvariable=self.ename,font=("Arial",15,))
        ename_entry.place(x=120,y=50,width=250)

        # ===================== Emp Age =====================================
        self.age = StringVar()
        age = Label(self.frame3,text="Age : ",bg="white",font=("Garamond",20,"bold"))
        age.place(x=5,y=100)

        age_entry = ttk.Entry(self.frame3,textvariable=self.age,font=("Arial",15,))
        age_entry.place(x=120,y=100,width=250)

        # ====================== Gender =================================
        self.gender = StringVar()
        gender = Label(self.frame3,text="Gender : ",bg="white",font=("Garamond",20,"bold"))
        gender.place(x=5,y=150)

        combogender = ttk.Combobox(self.frame3,textvariable=self.gender,font=("times new roman",15,"bold"),state="readonly")
        combogender["value"] = ("Male","Female")
        combogender.current(0)
        combogender.place(x=120,y=150,width=250)

        # ===================== Job =====================================
        self.job = StringVar()
        job = Label(self.frame3,text="Job : ",bg="white",font=("Garamond",20,"bold"))
        job.place(x=5,y=200)

        combojob = ttk.Combobox(self.frame3,font=("times new roman",15,"bold"),textvariable=self.job,state="readonly")
        combojob["value"] = ("Front Desk Clerks","Porters","HouseKeeping","Kitchen Staff","Room Service","Waiter/Waitress","Manager","Accountant")
        combojob.current(0)
        combojob.place(x=120,y=200,width=250)

        # ===================== Salary ===================================
        self.salary = StringVar()
        salary = Label(self.frame3,text="Salary : ",bg="white",font=("Garamond",20,"bold"))
        salary.place(x=5,y=250)

        
        salary_entry = ttk.Entry(self.frame3,textvariable=self.salary,font=("Arial",15,))
        salary_entry.place(x=120,y=250,width=250)

        # =============== phone =================================    
        self.phone = StringVar()    
        phone = Label(self.frame3,text="Phone : ",bg="white",font=("Garamond",20,"bold"))
        phone.place(x=5,y=300)

        
        phone_entry = ttk.Entry(self.frame3,textvariable=self.phone,font=("Arial",15,))
        phone_entry.place(x=120,y=300,width=250)

        # ============== adhar =============================  
        self.adhar = StringVar()      
        adhaar = Label(self.frame3,text="Aadhar : ",bg="white",font=("Garamond",20,"bold"))
        adhaar.place(x=5,y=350)

        
        adhaar_entry = ttk.Entry(self.frame3,textvariable=self.adhar,font=("Arial",15,))
        adhaar_entry.place(x=120,y=350,width=250)

        # =============== Email =============================== 
        self.email =  StringVar()      
        email = Label(self.frame3,text="Email : ",bg="white",font=("Garamond",20,"bold"))
        email.place(x=5,y=400)

        
        email_entry = ttk.Entry(self.frame3,textvariable=self.email,font=("Arial",15,))
        email_entry.place(x=120,y=400,width=250)

        img6 = Image.open(r"Images\employee.jpeg")
        img6 = img6.resize((250,250)) 
        self.photoimage4= ImageTk.PhotoImage(img6)
        lblimg4 = Label(self.frame3,image=self.photoimage4,bg="black",borderwidth=0)
        lblimg4.place(x=500,y=100,width=250,height=250)

        # ================== Back Button =========================
        back_btn = Button(self.frame3, text="Back", fg="gold" , command=self.close,bg="Black",font=("Garamond",15),cursor="hand2")
        back_btn.place(x=50 , y=450 ,width=150,height=30)

        # ================== Add Button ===========================
        add_btn = Button(self.frame3,text="Add", fg="gold",bg="Black",command=self.add_emp1,font=("Garamond",15),cursor="hand2")
        add_btn.place(x=250 , y=450 ,width=150,height=30)

    # ======================= Add Employee to Database =====================================
    def add_emp1(self):
        if self.ename.get()=="" or self.age.get()=="" or self.gender.get()=="" or self.job.get()=="" or self.salary.get()=="" or self.adhar.get()=="" or self.email.get()=="" :
            messagebox.showerror("Error","All field are required",parent=self.root)
            engine = pyttsx3.init()
            engine.say("All field are required")
            engine.runAndWait()
           
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
            my_cursor = conn.cursor()
            my_cursor.execute("insert into emp values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                   self.ename.get(),
                                                                   self.age.get(),
                                                                   self.gender.get(),
                                                                   self.job.get(),
                                                                   self.salary.get(),
                                                                   self.phone.get(),
                                                                   self.adhar.get(),
                                                                   self.email.get()
                                                                ))
            conn.commit()
            #self.fetch_data1()
            conn.close()
            messagebox.showinfo("Success","Employee Added Succesfully",parent=self.root) 
            engine = pyttsx3.init()
            engine.say("Employee Added Succesfully")
            engine.runAndWait()
            self.frame3.destroy()
  

# ======================= Destroy =====================================
    def close(self):
        self.frame3.destroy()


if __name__ == "__main__":
    main()
    