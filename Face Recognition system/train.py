from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from pip import main
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
# ============== importing opencv-python========================
# opencv = OPEN SOURCE COMPUTER VISION LIBRARY
import cv2

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_label = Label(self.root,text="TRAIN DATA SET",font=("times new roman",27,"bold"),bg="lightblue",fg="black")
        title_label.place(x=0,y=0,height=35,width=1540)
        
        # TOP IMAGE
        img1 = Image.open(r"C:\Users\paris\OneDrive\Desktop\Parish\college_images\facialrecognition.png")
        img1 = img1.resize((1535,360),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=34,width=1535,height=362)
        
        # TRAIN Data Button
        btn1_frame = Button(self.root,text="TRAIN DATA",command=self.train_classifier,font=("times new roman",20,"bold"),fg="white",bg="blue",cursor="hand2")
        btn1_frame.place(x=0,y=395,height=40,width=1530)
        
        # down image
        img2 = Image.open(r"C:\Users\paris\OneDrive\Desktop\Parish\college_images\g.png")
        img2 = img2.resize((1535,360),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=435,width=1535,height=360)
        

        
    def train_classifier(self):
        # here we are putting data sample images to data_dir
        data_dir=("SamplePhotos")
        # Now we are giving path through os
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            # It will convert image to gray scale image
            img=Image.open(image).convert('L')
            # uint8 is the array
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            # "C:\Users\paris\OneDrive\Desktop\Parish\Project\Face Recognition system\SamplePhotos\user.2.1.jpg"
            ids.append(id)
            # To open training window
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        # Converting id's to numpy
        ids=np.array(ids)
        
        
        # ============================= Train Classifier =====================
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        # to store into  files
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data Set Completed")
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()

print("Working..")
        