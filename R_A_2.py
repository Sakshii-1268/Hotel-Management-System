from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image
import time
import mysql.connector
import pyttsx3
from tkinter import messagebox
from Admin_3 import admin_page1
from reception import reception


def main():
    win = Tk()
    app = R_A(win)
    win.mainloop()

class R_A:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management")
        self.root.geometry("1300x650+0+0")

        # ================== Background image =========================      
        bg = Image.open(r"Images\bg.jpg")
        bg =bg.resize((1300,650)) 
        self.bg= ImageTk.PhotoImage(bg)
        lbl_bg = Label(self.root,image=self.bg,borderwidth=0)
        lbl_bg.place(x=0,y=0,width=1300,height=650)

        # ================== Frame ========================= 
        frame2 = Frame(self.root,bg="white",highlightbackground="black",highlightthickness=1)
        frame2.place(x=200,y=150,height=300,width=400)

        # ================== Reception Field =========================
        reception = Image.open(r"Images\recepyion.jpeg")
        reception =reception.resize((300,200)) 
        self.reception= ImageTk.PhotoImage(reception)
        lbl_reception = Label(frame2,image=self.reception,borderwidth=0)
        lbl_reception.place(x=50,y=10,width=300,height=200)

        rbutton = Button(frame2, text="Reception", fg="gold" ,command=self.reception1, bg="Black" ,font=("Garamond",20),cursor="hand2")
        rbutton.place(x=150 , y=230 ,width=120,height=30)

        # ================== frame =========================
        frame3 = Frame(self.root,bg="white",highlightbackground="black",highlightthickness=1)
        frame3.place(x=700,y=150,height=300,width=400)

        # ================== Admin field =========================
        admin = Image.open(r"Images\admin.jpeg")
        admin =admin.resize((300,200)) 
        self.admin= ImageTk.PhotoImage(admin)
        lbl_admin = Label(frame3,image=self.admin,borderwidth=0)
        lbl_admin.place(x=50,y=10,width=300,height=200)

        abutton = Button(frame3, text="Admin", fg="gold",command=self.admin1,bg="Black",font=("Garamond",20),cursor="hand2")
        abutton.place(x=150 , y=230 ,width=120,height=30)

    # ================== admin function ========================= 
    def admin1(self):
        self.new_window=Toplevel(self.root)
        self.app = Admin(self.new_window)

    
    # ================== reception function ========================= 
    def reception1(self):
        self.new_window=Toplevel(self.root)
        self.app = reception(self.new_window)

# ================== Admin class for login  =========================
class Admin():
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management")
        self.root.geometry("850x450+200+80")
        self.root.resizable(0,0)

        # ================== Variable =========================
        self.username1 = StringVar()
        self.password1 = StringVar()

        # ================== bg image =========================
        bg1 = Image.open(r"Images\bg.jpg")
        bg1 =bg1.resize((850,450)) 
        self.bg1= ImageTk.PhotoImage(bg1)
        lbl_bg1 = Label(self.root,image=self.bg1,bg="black",borderwidth=0)
        lbl_bg1.place(x=0,y=0,width=850,height=450)

        # ================== frame =========================
        frame1 = Frame(self.root,bg="white",highlightbackground="black",highlightthickness=1)
        frame1.place(x=100,y=50,height=350,width=650)

        # ================== title =========================
        admin_login = Label(frame1,text="Admin Login",bg="white",font=("Castellar",30,),fg="black")
        admin_login.place(x=150,y=5)

        # ================== Username field =========================
        user_logo1 = Image.open(r"Images\username.jpg")
        user_logo1 =user_logo1.resize((40,40)) 
        self.user_logo1= ImageTk.PhotoImage(user_logo1)
        lbl_user_logo1 = Label(frame1,image=self.user_logo1,bg="black",borderwidth=0)
        lbl_user_logo1.place(x=10,y=80,width=40,height=40)
        
        user_name1 = Label(frame1,text="Enter Username : ",bg="white",font=("Garamond",15,"bold"),fg="black")
        user_name1.place(x=80,y=80)

        self.username_entry1 =ttk.Entry(frame1,textvariable=self.username1,font=("Garamond",15,))
        self.username_entry1.place(x=260,y=80,width=250)

        # ================== Password field =========================
        password_logo1 = Image.open(r"Images\password.jpg")
        password_logo1 =password_logo1.resize((40,40)) 
        self.password_logo1= ImageTk.PhotoImage(password_logo1)
        lbl_password_logo1 = Label(frame1,image=self.password_logo1,bg="black",borderwidth=0)
        lbl_password_logo1.place(x=10,y=170,width=40,height=40)
     
        password1 = Label(frame1,text="Enter Password : ",bg="white",font=("Garamond",15,"bold"),fg="black")
        password1.place(x=80,y=170)

        self.password_entry1 =ttk.Entry(frame1,show='*',textvariable=self.password1,font=("Garamond",15,))
        self.password_entry1.place(x=260,y=170,width=250)

        show_password1 = Checkbutton(frame1,text="Show Password",command=self.show_password1,bg="white")
        show_password1.place(x=520,y=170)

        # ================== login button =========================
        login_button1 = Image.open(r"Images\login_button1.jpg")
        login_button1 = login_button1.resize((100,70))
        self.login_button1 = ImageTk.PhotoImage(login_button1)
        lbl_login_button1 = Button(frame1,image=self.login_button1,command=self.login_entry1,borderwidth=0,cursor="hand2",bg="white")
        lbl_login_button1.place(x=20,y=240,width=200,height=100)

        # ================== back button =========================
        backbutton = Button(frame1, text="Back", command=self.back,fg="gold",bg="Black",font=("Garamond",15),cursor="hand2")
        backbutton.place(x=400 , y=260 ,width=100,height=30)

    # ================== back button function =========================
    def back(self):
        self.root.destroy()


    # ================== show password function =========================    
    def show_password1(self):
        if self.password_entry1.cget('show') == '*':
            self.password_entry1.config(show='')
        else:
            self.password_entry1.config(show='*')
    
    # ================== check from the database =========================
    def login_entry1(self):
        if self.username1.get()== "" or self.password1.get() == "":
            messagebox.showerror("Error","All fields are required",parent=self.root)
            engine = pyttsx3.init()
            engine.say("All fields are required")
            engine.runAndWait()
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
            my_cursor = conn.cursor()
            my_cursor.execute("Select * from admin_login where username=%s and password=%s",(
                                                                                            self.username1.get(),
                                                                                            self.password1.get()
                                                                                            ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or password",parent=self.root)
                engine = pyttsx3.init()
                engine.say("Invalid Username or password")
                engine.runAndWait()
            else:
                self.new_window=Toplevel(self.root)
                self.app = admin_page1(self.new_window)

                engine = pyttsx3.init()
                engine.say("Login Succesfully")
                engine.runAndWait()
    

if __name__ == "__main__":
    main()
