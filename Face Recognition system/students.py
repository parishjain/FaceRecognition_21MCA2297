import imghdr
from tkinter import *
from tkinter import ttk
from turtle import bgcolor, right
from PIL import Image,ImageTk
from colorama import Cursor
from h11 import MUST_CLOSE
from markupsafe import escape_silent
from pip import main
from tkinter import messagebox
import mysql.connector


# ============== importing opencv-python========================
# opencv = OPEN SOURCE COMPUTER VISION LIBRARY
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        # ======================= variable=======================================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_name = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_id = StringVar()
        
        
        # FIRST IMAGE
        
        img = Image.open(r"C:\Users\paris\OneDrive\Desktop\Parish\college_images\face_det.png")
        
        # Now we set image size height and width
        # ANTIALIAS will convert high level image into low level image
        
        img = img.resize((500,130),Image.ANTIALIAS)
        # Now we will store image into variable 
        self.photoimg = ImageTk.PhotoImage(img)
        
        # Now we will set image to window by using label
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        
        # SECOND IMAGE
        img1 = Image.open(r"C:\Users\paris\OneDrive\Desktop\Parish\college_images\gettyimages-1022573162.jpg")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        # THIRD IMAGE
        img2 = Image.open(r"C:\Users\paris\OneDrive\Desktop\Parish\college_images\face-recognition.png")
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
        
                
        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEN",font=("times new roman",30,"bold"),bg="white",fg="red")
        # place is used to place anything
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        # main_frame variable 
        # bd for border
        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=20,y=50,width=1500, height=600)
        
        # LEFT LABEL FRAME
        # Here we have pass main_frame because we wan't 
        # to make the left_frame inside the main_frame
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAIL",font=("times new roman",12,"bold"),bg="white")
        left_frame.place(x=10,y=10,height=660,width=680)
        
        img4 = Image.open(r"C:\Users\paris\OneDrive\Desktop\Parish\college_images\register.png")
        img4 = img4.resize((670,200),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        f_lbl = Label(left_frame,image=self.photoimg4)
        f_lbl.place(x=5,y=0,width=670,height=200)
        
        
        # CURRENT COURSE
        
        current_course_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="COURSE INFORMATION",font=("times new roman",12,"bold"),bg="white")
        current_course_frame.place(x=5,y=210,height=130,width=665)
        
        
        
        
        # DEPARTMENT
        dep_label = Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=25,sticky=W)
        # Combobox dropdown box
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","Civil","Mechanical","Electrical","Commerce","Management")

        dep_combo.current(0)
        # padx= for padding x-axis
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        
        
        course_label = Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=45)
        # Combobox dropdown box
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Course","MCA","B.Tech","M.Tech","MBA","BCA","M.Sc(Data Science)","B.Com","M.Com")

        dep_combo.current(0)
        # padx= for padding x-axis
        dep_combo.grid(row=0,column=3,padx=1,pady=10)
        
        
        # Semester
        semester_label = Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=0,padx=25,sticky=W)
        # Combobox dropdown box
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Semester","1st Sem","2nd Sem","3rd Sem","4th Sem","5th Sem","6th Sem","7th Sem","8th Sem" )

        dep_combo.current(0)
        # padx= for padding x-axis
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        
        
        #  Year
        Year_label = Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        Year_label.grid(row=1,column=2,padx=45,sticky=W)
        # Combobox dropdown box
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Year","2019-2020","2020-2021","2021-2022","2022-2023")

        dep_combo.current(0)
        # padx= for padding x-axis
        dep_combo.grid(row=1,column=3,padx=0,pady=10,stick=W)
        
        
        #STUDENT FRAME
        student_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="STUDENT INFORMATION",font=("times new roman",12,"bold"),bg="white")
        student_frame.place(x=5,y=350,height=200,width=665)
        
        
        # student id
        studentid_label = Label(student_frame,text="STUDENT ID",font=("times new roman",12,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,sticky=W,pady=10)
        
        studentid_entry=ttk.Entry(student_frame,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,sticky=W,pady=10)
        
        
        # student name
        studentname_label = Label(student_frame,text="STUDENT NAME",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,sticky=W,pady=10)
        
        studentname_entry=ttk.Entry(student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,sticky=W,pady=10)
        
        
        # student name
        email_label = Label(student_frame,text="STUDENT EMAIL",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        
        email_entry=ttk.Entry(student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=1,column=1,padx=10,sticky=W, pady=10)
        
        #PHONE NUMBER
        phonenumber_label = Label(student_frame,text="PHONE NUMBER",font=("times new roman",12,"bold"),bg="white")
        phonenumber_label.grid(row=1,column=2,padx=10,sticky=W,pady=10)
        
        phonenumber_entry=ttk.Entry(student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phonenumber_entry.grid(row=1,column=3,padx=10,sticky=W,pady=10)
        
        
        # RADIO BUTTON
        self.var_radio1=StringVar()
        photo_label = ttk.Radiobutton(student_frame,variable=self.var_radio1,text="TAKE SAMPLE PHOTO",value="Yes")
        photo_label.grid(row=2,column=0,padx=10,pady=10)
        
        photo_label = ttk.Radiobutton(student_frame,variable=self.var_radio1,text="NO SAMPLE PHOTO",value="No")
        photo_label.grid(row=2,column=1,padx=20,pady=10)
        
        
        # Button frame
        btn_frame = Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=120,width=660,height=30)
        
        save_btn=Button(btn_frame, cursor="hand2",text="SAVE",command=self.add_data,width=23,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        reset_btn=Button(btn_frame,text="RESET",cursor="hand2",width=23,command=self.reset_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=1)
        
        reset_btn=Button(btn_frame,text="UPDATE",cursor="hand2",command=self.update_data,width=23,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="DELETE",command=self.delete_data,cursor="hand2",width=22,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        btn_frame1 = Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=150,width=660,height=30)
        
        takephoto_btn=Button(btn_frame1,text="TAKE PHOTO SAMPLE",command=self.generate_dataset,cursor="hand2",width=46,font=("times new roman",10,"bold"),bg="blue",fg="white")
        takephoto_btn.grid(row=0,column=0)
        
        uploadphoto_btn=Button(btn_frame1,text="UPLOAD PHOTO SAMPLE",cursor="hand2",width=46,font=("times new roman",10,"bold"),bg="blue",fg="white")
        uploadphoto_btn.grid(row=0,column=1)
        
           
        
        
        
        
        # RIGHT FRAME
        
        right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"),bg="white")
        right_frame.place(x=700,y=10,height=660,width=780)
        
        img5 = Image.open(r"C:\Users\paris\OneDrive\Desktop\Parish\college_images\university2.jpg")
        img5 = img5.resize((750,200),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        f_lbl = Label(right_frame,image=self.photoimg5)
        f_lbl.place(x=10,y=0,width=750,height=200)
        
        
        
        
        
        # ========================== SEARCH SYSTEM ================================
        # SEARCH FRAME
        search_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,text="SEARCH SYSTEM",font=("times new roman",12,"bold"),bg="white")
        search_frame.place(x=5,y=210,height=70,width=750)
        
        sort_frame = Label(search_frame,bd=2,relief=RIDGE,text="SEARCH BY:",font=("times new roman",12,"bold"),bg="white")
        sort_frame.place(x=5,y=5,height=30,width=120)
        
        # Search combobox
        search_name_frame = ttk.Combobox(search_frame,font=("times new roman",15,"bold"),state="readonly")
        search_name_frame["values"] = ("Select","Name","id","Mobile Number")
        search_name_frame.current(0)
        search_name_frame.place(x=130,y=5,height=30,width=150)
        
        input_search_frame = ttk.Entry(search_frame,font=("times new roman",15,"bold"))
        input_search_frame.place(x=290,y=5,height=30,width=280)
        
        search_btn = Button(search_frame,text="SEARCH",bg="blue",fg="white",font=("times new roman",10,"bold"),cursor="hand2")
        search_btn.place(x=580,y=5,height=30,width=75)
        
        show_btn = Button(search_frame,text="SHOW ALL",bg="blue",fg="white",font=("times new roman",10,"bold"),cursor="hand2")
        show_btn.place(x=660,y=5,height=30,width=75)
        
        # =====================TABLE FRAMEE=======================================
        table_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,font=("times new roman",12,"bold"),bg="white")
        table_frame.place(x=5,y=290,height=250,width=750)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview( table_frame,columns=("dep","name","id","sem","course","year","phone","email","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("dep",text="DEPARTMENT")
        self.student_table.heading("name",text="NAME")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("sem",text="SEMESTER")
        self.student_table.heading("course",text="COURSE")
        self.student_table.heading("year",text="YEAR")
        self.student_table.heading("phone",text="PHONE")
        self.student_table.heading("email",text="EMAIL")
        self.student_table.heading("photo",text="PHOTO SAMPLE")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=150)
        self.student_table.column("name",width=150)
        self.student_table.column("id",width=150)
        self.student_table.column("sem",width=150)
        self.student_table.column("phone",width=150)
        self.student_table.column("email",width=150)
        self.student_table.column("course",width=150)
        self.student_table.column("year",width=150)
        self.student_table.column("photo",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
       
    # =========================== Error Function =============================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course"  or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_phone.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:    
                conn =mysql.connector.connect(host="localhost",username="root",password="3425",database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),
                                                                                    self.var_name.get(),
                                                                                    self.var_id.get(),
                                                                                    self.var_sem.get(),
                                                                                    self.var_course.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_radio1.get()                                                                              
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student record saved successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
    
    
    # ================================ FETCH DATA ============================================
    def fetch_data(self):
        conn =mysql.connector.connect(host="localhost",username="root",password="3425",database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
    # # ================================ get cursor ============================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        # . item is help to get content
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),           
        self.var_name.set(data[1]),           
        self.var_id.set(data[2]),           
        self.var_course.set(data[3]),           
        self.var_sem.set(data[4]),           
        self.var_year.set(data[5]),           
        self.var_phone.set(data[6]),           
        self.var_email.set(data[7]),           
        self.var_radio1.set(data[8])           
        
        
    # ========================UPDATE DATA=================================                                  
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course"  or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_phone.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if upadate>0:
                    conn =mysql.connector.connect(host="localhost",username="root",password="3425",database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department=%s,Name=%s,Semester=%s,Course=%s,Year=%s,Phone=%s,Email=%s,PhotoSample=%s where id=%s",(self.var_dep.get(),self.var_name.get(),self.var_sem.get(),self.var_course.get(),self.var_year.get(),self.var_phone.get(),self.var_email.get(),self.var_radio1.get(),self.var_id.get()))                                                                                                                
                else:
                    if not upadate:
                        return
                messagebox.showinfo("Success","Student Details Updated Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To {str(es)}",parent=self.root)
    
    
    # ===========================DELETE DATA====================================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Students ID Must be Required")
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Student id must be required",parent=self.root)
                if delete>0:
                    conn =mysql.connector.connect(host="localhost",username="root",password="3425",database="face_recognition")
                    my_cursor = conn.cursor()
                    sql="delete from student where id=%s"
                    val= (self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)    
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)
                
                
    # ============================ RESET =========================================
    def reset_data(self):
        self.var_dep.set("Select Department "),           
        self.var_name.set(""),           
        self.var_id.set(""),           
        self.var_course.set("Select Course"),           
        self.var_sem.set("Select Semester"),           
        self.var_year.set("Select Year"),           
        self.var_phone.set(""),           
        self.var_email.set(""),           
        self.var_radio1.set("")     
    
    
    # =============== GENERATE DATASET AND TAKE THE PHOTO SAMPLE =================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course"  or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_phone.get()=="":
                messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn =mysql.connector.connect(host="localhost",username="root",password="3425",database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                id = self.var_id.get()

                my_cursor.execute("update student set Department=%s,Name=%s,Semester=%s,Course=%s,Year=%s,Phone=%s,Email=%s,PhotoSample=%s where id=%s",(self.var_dep.get(),self.var_name.get(),self.var_sem.get(),self.var_course.get(),self.var_year.get(),self.var_phone.get(),self.var_email.get(),self.var_radio1.get(),self.var_id.get()))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                # ================= LOAD PREDEFINED DATA ON FACE FRONTALS FROM OPENCV==================================
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    # CONVERTING BGR COLOR IMAGES TO GREYSCALE
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    # 1.3 = Scaling Factor   5 = Minimum Neighbour
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cam_open = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cam_open.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        # file_name_path="SamplePhotos\\ " + "user." +str(id)+ "." + str(img_id) + ".jpg"
                        file_name_path="SamplePhotos/user." + str(id) + "." + str(img_id)+".jpg" 
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                        
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                    
                cam_open.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets Completed")        
            
            except Exception as es:
                print("here")
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                        
                        
                    
                    
                    
                
                
                                                                                   
                    
        
        
            
                     
                        
            
                    
                    
                
            
            
        
        
                    
                

    
        
             
            
        
        
            
        
        
        
        
        
        
        
        
      

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

print("Working..")