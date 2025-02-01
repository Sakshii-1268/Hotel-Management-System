from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image
import time
import mysql.connector
from tkinter import messagebox


def main():
    win = Tk()
    app = aboutus(win)
    win.mainloop()

    
class aboutus:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management")
        self.root.geometry("1300x650+0+0")
        
        frame1 = Frame(self.root,bg='aquamarine1')
        frame1.place(x=0,y=0,width=1300,height=650) 

        
        # ================== Title =========================
        hotel_name = Label(frame1,text="Royal Hotel",bg="aquamarine1",font=("Castellar",30,),fg="black")
        hotel_name.place(x=400,y=5)

        about = Label(self.root,text="Hotel Royal Is well know for its excellent ",bg='aquamarine1',font=("Lucida Handwriting",20))
        about.place(x=10,y=140)

        about = Label(self.root,text="services , friendly staff , wounderfull",bg='aquamarine1',font=("Lucida Handwriting",20))
        about.place(x=10,y=200)
        
        about = Label(self.root,text="lake and Mountain view .",bg='aquamarine1',font=("Lucida Handwriting",20))
        about.place(x=10,y=260)
        
        Room = Button(self.root,text="  Gallery  ",bg="white",cursor="hand2" ,command=self.room,font=("Book Antiqua",20,"bold"))
        Room.place(x=20,y=360)


        self.image = Image.open(r"Images\hotel1.jpg")
        self.image = self.image.resize((600,300))
        self.bg = ImageTk.PhotoImage(self.image)

        
        self.image1 = Image.open(r"Images\hotel2.jpg")
        self.image1 = self.image1.resize((600,300))
        self.bg1 = ImageTk.PhotoImage(self.image1)


        self.lbl1 = Label(frame1,image=self.bg,bd=0)
        self.lbl1.place(x=700,y=80,width=600,height=300)
        
        self.lbl2 = Label(frame1,image=self.bg1,bd=0)
        self.lbl2.place(x=1300,y=80,width=600,height=300)
        self.x = 1300
        self.slider()

    def room(self):
        self.new_window=Toplevel(self.root)
        self.new_window.title("Hotel Management")
        self.new_window.geometry("1300x650+0+0")
    
        
        artroom = Image.open(r"Images\artroom.jpg")
        artroom =artroom.resize((450,200)) 
        self.artroom= ImageTk.PhotoImage(artroom)
        self.lbl_artroom = Label(self.new_window,image=self.artroom,borderwidth=0)
        self.lbl_artroom.place(x=10,y=5,width=450,height=200)

        image1 = Image.open(r"Images\grandroom.jpg")
        image1 =image1.resize((450,200)) 
        self.image1= ImageTk.PhotoImage(image1)
        self.lbl_image1 = Label(self.new_window,image=self.image1,borderwidth=0)
        self.lbl_image1.place(x=470,y=5,width=450,height=200)
 
        image2 = Image.open(r"Images\luxuryroom.jpg")
        image2 =image2.resize((450,200)) 
        self.image2= ImageTk.PhotoImage(image2)
        self.lbl_image2 = Label(self.new_window,image=self.image2,borderwidth=0)
        self.lbl_image2.place(x=930,y=5,width=450,height=200)

        
        image3 = Image.open(r"Images\imperialroom.jpg")
        image3 =image3.resize((450,200)) 
        self.image3= ImageTk.PhotoImage(image3)
        self.lbl_image3 = Label(self.new_window,image=self.image3,borderwidth=0)
        self.lbl_image3.place(x=10,y=215,width=450,height=200)


        image4 = Image.open(r"Images\hotel4.jpg")
        image4 =image4.resize((450,200)) 
        self.image4= ImageTk.PhotoImage(image4)
        self.lbl_image4 = Label(self.new_window,image=self.image4,borderwidth=0)
        self.lbl_image4.place(x=470,y=215,width=450,height=200)

        
        image5 = Image.open(r"Images\hotel5.jpg")
        image5 =image5.resize((450,200)) 
        self.image5= ImageTk.PhotoImage(image5)
        self.lbl_image5 = Label(self.new_window,image=self.image5,borderwidth=0)
        self.lbl_image5.place(x=930,y=215,width=450,height=200)
        
        image6 = Image.open(r"Images\hotel6.jpg")
        image6 =image6.resize((450,200)) 
        self.image6= ImageTk.PhotoImage(image6)
        self.lbl_image6 = Label(self.new_window,image=self.image6,borderwidth=0)
        self.lbl_image6.place(x=10,y=425,width=450,height=200)
        
        image7 = Image.open(r"Images\hotel7.jpg")
        image7 =image7.resize((450,200)) 
        self.image7= ImageTk.PhotoImage(image7)
        self.lbl_image7 = Label(self.new_window,image=self.image7,borderwidth=0)
        self.lbl_image7.place(x=470,y=425,width=450,height=200)
        
        image8 = Image.open(r"Images\hotel2.jpg")
        image8 =image8.resize((450,200)) 
        self.image8= ImageTk.PhotoImage(image8)
        self.lbl_image8 = Label(self.new_window,image=self.image8,borderwidth=0)
        self.lbl_image8.place(x=930,y=425,width=450,height=200)
    

    def slider(self):
        self.x-=1
        if self.x==700:
            self.x=1300
            time.sleep(1)


            self.new_im = self.bg
            self.bg = self.bg1
            self.bg1 = self.new_im

            self.lbl1.config(image=self.bg1)
            self.lbl2.config(image=self.bg)

        self.lbl2.place(x=self.x,y=80,width=600,height=300)
        self.lbl2.after(2,self.slider)


        
if __name__ == "__main__":
    main()

    #total line = 1918