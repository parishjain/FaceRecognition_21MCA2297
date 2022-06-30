# Python offers multiple options for developing GUI (Graphical User Interface). Out of all the GUI methods, 
# tkinter is the most commonly used method. 
# It is a standard Python interface to the Tk GUI toolkit shipped with Python. 
# Python with tkinter is the fastest and easiest way to create the GUI applications. Creating a GUI using tkinter is an easy task.

from tkinter import *
# Tkinter.ttk is a module designed to make Tkinter widgets look really perfectly,
# So if you are making apps for your own private use, then use Tkinter and also use some ttk if needed, because ttk supports much cooler widgets that can change the look of your app.
# Simply it contains stylish toolkit

# We import os to take photos from directory
import os

from tkinter import ttk


# ==========IMPORTING STUDENT FILE==============================
from students import Student
from train import Train
from facerecog import Face_Recognition

# Now we will inistall Pilow Library
from PIL import Image,ImageTk
from numpy import imag  # This help us to Resize the image

class Face_Recognnition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        # FIRST IMAGE
        
        img = Image.open(r"C:\Users\paris\OneDrive\Desktop\Parish\college_images\unnamed.jpg")
        
        # Now we set image size height and width
        # ANTIALIAS will convert high level image into low level image
        
        img = img.resize((500,130),Image.ANTIALIAS)
        # Now we will store image into variable 
        self.photoimg = ImageTk.PhotoImage(img)
        
        # Now we will set image to window by using label
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        
        # SECOND IMAGE
        img1 = Image.open(r"C:\Users\paris\OneDrive\Desktop\Parish\college_images\facialrecognition.png")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        # THIRD IMAGE
        img2 = Image.open(r"C:\Users\paris\OneDrive\Desktop\Parish\college_images\unnamed.jpg")
        img2 = img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        # bg image
        img3 = Image.open(r"C:\Users\paris\OneDrive\Desktop\Parish\college_images\img3.jpg")
        img3 = img3.resize((1600,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1600,height=710)
        
        title_lbl = Label(bg_img,text="FACE RECOGNITION SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="darkblue")
        # place is used to place anything
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        #STUDENT DETAIL SECTION 
        img4 = Image.open(r"C:\Users\paris\OneDrive\Desktop\Parish\college_images\iStock-182059956_18390_t12.jpg")
        img4 = img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,command=self.student_details,image=self.photoimg4,cursor="hand2")
        b1.place(x=950,y=100,width=200,height=200)
        # BUTTON STUDENT DETAILS
        b1_button=Button(bg_img,command=self.student_details,text="STUDENT DETAILS",cursor="hand2",font=("times new roman",13,"bold"),fg="white",bg="darkblue")
        b1_button.place(x=950,y=280,width=202,height=40)
        
        
        
        # DETECT FACE
        img5 = Image.open(r"C:\Users\paris\OneDrive\Desktop\Parish\college_images\face_detector1.jpg")
        img5 = img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data,)
        b1.place(x=1250,y=100,width=200,height=200)
        # BUTTON STUDENT DETAILS
        b1_button=Button(bg_img,text="DETECT FACE",cursor="hand2",command=self.face_data,font=("times new roman",12,"bold"),fg="white",bg="darkblue")
        b1_button.place(x=1250,y=280,width=202,height=40)
             
        
        
        # ATTENDENCE RECORD
        img6 = Image.open(r"C:\Users\paris\OneDrive\Desktop\Parish\college_images\facialrecognition (1).png")
        img6 = img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.train_data)
        b1.place(x=950,y=350,width=200,height=200)
        b1_button=Button(bg_img,text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("times new roman",13,"bold"),fg="white",bg="darkblue")
        b1_button.place(x=950,y=530,width=202,height=40)
        
        
        
        # HELP DESK & ABOUT US
        img7 = Image.open(r"C:\Users\paris\OneDrive\Desktop\Parish\college_images\img2.jpg")
        img7 = img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.open_image)
        b1.place(x=1250,y=350,width=200,height=200)
        # BUTTON STUDENT DETAILS
        b1_button=Button(bg_img,text="SAMPLE COLLECTED",cursor="hand2",font=("times",12,"bold"),fg="white",bg="darkblue",)
        b1_button.place(x=1250,y=530,width=202,height=40)
        
    # ============================ open images =========================
    def open_image(self):
        os.startfile("SamplePhotos")
        
    
        
    # ================================== FUNCTION BUTTON=================================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    # ================================== DETECT FACE =================================
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    # ================================== TRAIN DATA =================================
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
        
    
                           
        
        
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognnition_System(root)
    root.mainloop()
    
        
        
print("Working..")