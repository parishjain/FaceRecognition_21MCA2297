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

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_label = Label(self.root,text="FACE RECOGNITION",font=("times new roman",27,"bold"),bg="darkblue",fg="white")
        title_label.place(x=0,y=0,height=36,width=1540)
        
        # TOP IMAGE
        img1 = Image.open(r"C:\Users\paris\OneDrive\Desktop\Parish\college_images\face_detector1.jpg")
        img1 = img1.resize((700,755),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=36,width=700,height=755)
        
        img2 = Image.open(r"C:\Users\paris\OneDrive\Desktop\Parish\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img2 = img2.resize((835,755),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=701,y=36,width=835,height=755)
        
        b1_button=Button(f_lbl,text="DETECT FACE",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="darkgreen",bd=2,highlightbackground="white",highlightthickness = 2)
        b1_button.place(x=310,y=638,width=202,height=40)
        
    # # ============================RECOGNITION=============================
    def face_recog(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbours,color,text,clf):          
            # First we will convert image to gray scale
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)
            
            # list for coardinates to draw rectangle on face
            coard=[]
            
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                # Here we are applying formula
                confidence=int((100*(1-predict/300)))
                
                # To  get the data from the keyboard
                conn =mysql.connector.connect(host="localhost",username="root",password="3425",database="face_recognition")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Name from  student where id="+str(id))
                n=my_cursor.fetchone()
                n= "+".join(n)
                
                my_cursor.execute("select id from  student where id="+str(id))
                r=my_cursor.fetchone()
                r= "+".join(r)
                        
                my_cursor.execute("select Department from  student where id="+str(id))
                d=my_cursor.fetchone()
                d= "+".join(d)
                
                                                             
                
                if confidence>82:
                    cv2.putText(img,f"ID:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255),3)
                    cv2.putText(img,f"NAME:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255),3)
                    cv2.putText(img,f"DEPARTMENT:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255),3)
                    
                coard=[x,y,w,y]
                
            return coard
        
        # THIS FUNCTION IS FOR RECOGNIZE
        def recognize(img,clf,faceCascade):
            coard=draw_boundry(img,faceCascade,1.1,10,(255,25,255),"face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        
        
        
            
                    
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

print("Working..")
        