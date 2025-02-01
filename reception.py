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
from newcustomer import customer
from roomdetails import roomdetails
from employeedetails import employeedetails
from searchcus import search_cust
from About import aboutus
from checkout import checkout




def main():
    win = Tk()
    app = reception(win)
    win.mainloop()
    
class reception:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management")
        self.root.geometry("1300x650+0+0")
        
        # ============= Background images =======================
        bg = Image.open(r"Images\bg.jpg")
        bg =bg.resize((1300,650)) 
        self.bg= ImageTk.PhotoImage(bg)
        lbl_bg = Label(self.root,image=self.bg,bg="black",borderwidth=0)
        lbl_bg.place(x=0,y=0,width=1300,height=650)
        
        # ================== Title =========================
        hotel_name = Label(self.root,text="Menu",bg="black",fg="gold",font=("Castellar",30,"bold"))
        hotel_name.place(x=0,y=0,width=1300)


        # ================= Frame 1 =========================
        frame1 = Frame(self.root,bg="white",highlightbackground="black",highlightthickness=1)
        frame1.place(x=30,y=70,height=250,width=250)
        
        searc = Image.open(r"Images\cust.jpeg")
        searc =searc.resize((240,200)) 
        self.searc= ImageTk.PhotoImage(searc)
        lbl_searc= Label(frame1,image=self.searc,bg="black",borderwidth=0)
        lbl_searc.place(x=5,y=5,width=240,height=200)

        customer = Button(frame1, text="Add New Customer ",command=self.new_customer , fg="gold" ,bg="Black",font=("Garamond",15),cursor="hand2")
        customer.place(x=5 , y=210 ,width=240,height=30)


        # ================= Frame 2 =========================
        frame2 = Frame(self.root,bg="white",highlightbackground="black",highlightthickness=1)
        frame2.place(x=330,y=70,height=250,width=250)
              
        roomimg = Image.open(r"Images\room.jpeg")
        roomimg =roomimg.resize((240,200)) 
        self.roomimg= ImageTk.PhotoImage(roomimg)
        lbl_roomimg= Label(frame2,image=self.roomimg,borderwidth=0)
        lbl_roomimg.place(x=5,y=5,width=240,height=200)

        Room = Button(frame2, text="Room Details  ",command=self.room_d, fg="gold" ,bg="Black",font=("Garamond",15),cursor="hand2")
        Room.place(x=5 , y=210 ,width=240,height=30)


        # ================= Frame 3 =========================
        frame3 = Frame(self.root,bg="white",highlightbackground="black",highlightthickness=1)
        frame3.place(x=640,y=70,height=250,width=250)
        
        sear = Image.open(r"Images\employee.jpeg")
        sear =sear.resize((240,200)) 
        self.sear= ImageTk.PhotoImage(sear)
        lbl_sear= Label(frame3,image=self.sear,bg="black",borderwidth=0)
        lbl_sear.place(x=5,y=5,width=240,height=200)

        emp = Button(frame3, text="Employee Details  ", command=self.employee_d,fg="gold" ,bg="Black",font=("Garamond",15),cursor="hand2")
        emp.place(x=5 , y=210 ,width=240,height=30)


        # ================= Frame 4 =========================
        frame4 = Frame(self.root,bg="white",highlightbackground="black",highlightthickness=1)
        frame4.place(x=950,y=70,height=250,width=250)


        search = Image.open(r"Images\search.jpeg")
        search =search.resize((240,200)) 
        self.search= ImageTk.PhotoImage(search)
        lbl_search= Label(frame4,image=self.search,bg="black",borderwidth=0)
        lbl_search.place(x=5,y=5,width=240,height=200)

        #search_c = Button(frame4, text="Search Customer  ",command=self.search,fg="gold" ,bg="Black",font=("Garamond",15),cursor="hand2")
        #search_c.place(x=5 , y=210 ,width=240,height=30)
        
        search_cust = Button(frame4, text="Search Customer ", fg="gold",command=self.search1,bg="Black",font=("Garamond",15),cursor="hand2")
        search_cust.place(x=5, y=210 ,width=240,height=30)


        # ================= Frame 6 =========================
        frame6 = Frame(self.root,bg="white",highlightbackground="black",highlightthickness=1)
        frame6.place(x=180,y=380,height=250,width=250)

        
        checkout = Image.open(r"Images\checkou.jpeg")
        checkout =checkout.resize((240,200)) 
        self.checkout= ImageTk.PhotoImage(checkout)
        lbl_checkout= Label(frame6,image=self.checkout,bg="black",borderwidth=0)
        lbl_checkout.place(x=5,y=5,width=240,height=200)

        checkout = Button(frame6, text="Checkout ", fg="gold" ,command=self.chekout,bg="Black",font=("Garamond",15),cursor="hand2")
        checkout.place(x=5 , y=210,width=240,height=30)


        # ================= Frame 7 =========================
        frame7 = Frame(self.root,bg="white",highlightbackground="black",highlightthickness=1)
        frame7.place(x=490,y=380,height=250,width=250)

        aboutus = Image.open(r"Images\aboutus.jpeg")
        aboutus =aboutus.resize((240,200)) 
        self.aboutus= ImageTk.PhotoImage(aboutus)
        lbl_aboutus = Label(frame7,image=self.aboutus,bg="black",borderwidth=0)
        lbl_aboutus.place(x=5,y=5,width=240,height=200)

        about = Button(frame7, text="About ", fg="gold",command=self.about ,bg="Black",font=("Garamond",15),cursor="hand2")
        about.place(x=5, y=210 ,width=240,height=30)
        

        # ================= Frame 8 =========================
        frame8 = Frame(self.root,bg="white",highlightbackground="black",highlightthickness=1)
        frame8.place(x=800,y=380,height=250,width=250)

        logout = Image.open(r"Images\logout.jpeg")
        logout =logout.resize((240,200)) 
        self.logout= ImageTk.PhotoImage(logout)
        lbl_logout = Label(frame8,image=self.logout,bg="black",borderwidth=0)
        lbl_logout.place(x=5,y=5,width=240,height=200)

        logout = Button(frame8, text="Logout  ", fg="gold" ,bg="Black",command=self.log,font=("Garamond",15),cursor="hand2")
        logout.place(x=5 , y=210,width=240,height=30)
        



    # ================== New customer =======================
    def new_customer(self):
        self.new_window=Toplevel(self.root)
        self.app = customer(self.new_window)

    # ================== Room details =======================
    def room_d(self):
        self.new_window=Toplevel(self.root)
        self.app = roomdetails(self.new_window)

    # ================== Employee details =======================
    def employee_d(self):
        self.new_window=Toplevel(self.root)
        self.app = employeedetails(self.new_window)


    # ================== search function ========================= 
    def search1(self):
        self.new_window=Toplevel(self.root)
        self.app = search_cust(self.new_window)

    # ================== About function ========================= 
    def about(self):
        self.new_window=Toplevel(self.root)
        self.app = aboutus(self.new_window)
    
    # ================== Checkout function ========================= 
    def chekout(self):
        self.new_window=Toplevel(self.root)
        self.app = checkout(self.new_window)
    
    # ================== logout  function ========================= 
    def log(self):
        self.root.destroy()


if __name__ == "__main__":
    main()
    