from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image
import time
import mysql.connector
from tkinter import messagebox
from R_A_2 import R_A
import pyttsx3




def main():


    
    win = Tk()
    app = firstpage(win)
    win.mainloop()


class firstpage:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management")
        self.root.geometry("850x450+200+80")
        self.root.resizable(0,0)

        # ================== Variable =========================
        self.username = StringVar()
        self.password = StringVar()

        # ================== Background Image =========================
        bg = Image.open(r"Images\bg.jpg")
        bg =bg.resize((850,450)) 
        self.bg= ImageTk.PhotoImage(bg)
        lbl_bg = Label(self.root,image=self.bg,bg="black",borderwidth=0)
        lbl_bg.place(x=0,y=0,width=850,height=450)
         
        # ================== frame =========================
        frame1 = Frame(self.root,bg="white",highlightbackground="black",highlightthickness=1)
        frame1.place(x=100,y=50,height=350,width=650)
        
        # ================== Title =========================
        hotel_name = Label(frame1,text="Royal Hotel",bg="white",font=("Castellar",30,),fg="black")
        hotel_name.place(x=150,y=5)
        
        # ================== User name field =========================
        user_logo = Image.open(r"Images\username.jpg")
        user_logo =user_logo.resize((40,40)) 
        self.user_logo= ImageTk.PhotoImage(user_logo)
        lbl_user_logo = Label(frame1,image=self.user_logo,bg="black",borderwidth=0)
        lbl_user_logo.place(x=10,y=80,width=40,height=40)
        
        user_name = Label(frame1,text="Enter Username : ",bg="white",font=("Garamond",15,"bold"),fg="black")
        user_name.place(x=80,y=80)

        self.username_entry =ttk.Entry(frame1,textvariable=self.username,font=("Garamond",15,))
        self.username_entry.place(x=260,y=80,width=250)

        # ================== Password field =========================
        password_logo = Image.open(r"Images\password.jpg")
        password_logo =password_logo.resize((40,40)) 
        self.password_logo= ImageTk.PhotoImage(password_logo)
        lbl_password_logo = Label(frame1,image=self.password_logo,bg="black",borderwidth=0)
        lbl_password_logo.place(x=10,y=170,width=40,height=40)
     
        password = Label(frame1,text="Enter Password : ",bg="white",font=("Garamond",15,"bold"),fg="black")
        password.place(x=80,y=170)

        self.password_entry =ttk.Entry(frame1,textvariable=self.password,show='*',font=("Garamond",15,))
        self.password_entry.place(x=260,y=170,width=250)

        show_password = Checkbutton(frame1,text="Show Password",bg="white",command=self.show_password)
        show_password.place(x=520,y=170)

        # ================== Login Button =========================
        login_button = Image.open(r"Images\login_button1.jpg")
        login_button = login_button.resize((100,70))
        self.login_button = ImageTk.PhotoImage(login_button)
        lbl_login_button = Button(frame1,image=self.login_button,command=self.login_entry,borderwidth=0,cursor="hand2",bg="white")
        lbl_login_button.place(x=20,y=240,width=200,height=100)

        # ================== Hotel logo =========================    
        hotel_logo = Image.open(r"Images\logo.jpeg")
        hotel_logo =hotel_logo.resize((160,100)) 
        self.hotel_logo= ImageTk.PhotoImage(hotel_logo)
        lbl_hotel_logo = Label(frame1,image=self.hotel_logo,bg="black",borderwidth=0)
        lbl_hotel_logo.place(x=450,y=240,width=160,height=100)

        # ================== Show the password function =========================
    def show_password(self):
        if self.password_entry.cget('show') == '*':
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')

        # ================== Check from the database =========================
    def login_entry(self):
        if self.username.get()== "" or self.password.get() == "":
            messagebox.showerror("Error","All fields are required")
            engine = pyttsx3.init()
            engine.say("All fields are required")
            engine.runAndWait()
        
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Sakshi123@",database="hotel")   
            my_cursor = conn.cursor()
            my_cursor.execute("Select * from main_login where username=%s and password=%s",(
                                                                                            self.username.get(),
                                                                                            self.password.get()
                                                                                            ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or password",parent=self.root)
                engine = pyttsx3.init()
                engine.say("Invalid Username or password")
                engine.runAndWait()
        
            else:
                self.new_window=Toplevel(self.root)
                self.app = R_A(self.new_window)

                engine = pyttsx3.init()
                engine.say("Login Succesfully")
                engine.runAndWait()
                
# ================= main function ==========================
if __name__ == "__main__":
    main()
