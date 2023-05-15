from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator | Developed By Jaya")
        self.root.resizable(False,False)

        title=Label(self.root,text=" QR Code Generator",font=("times new roman",40),bg='#00e68a',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
        #Details Window
        #====variable======
        self.var_stu_code=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_address=StringVar()

        frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        frame.place(x=50,y=100,width=500,height=380)
        details_title=Label(frame,text="Enter Student Details",font=("goudy old style",20),bg='#00b36b',fg='white').place(x=0,y=0,relwidth=1)
        enroll_title=Label(frame,text="Enroll Id",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)
        enroll_name=Label(frame,text="Name",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
        enroll_course=Label(frame,text="Course",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
        enroll_address=Label(frame,text="Address",font=("times new roman",15,'bold'),bg='white').place(x=20,y=180)

        txt_details=Entry(frame,font=('times new roman',15),textvariable=self.var_stu_code,bg="lightyellow").place(x=200,y=60)
        txt_name=Entry(frame,font=('times new roman',15),textvariable=self.var_name,bg="lightyellow").place(x=200,y=100)
        txt_course=Entry(frame,font=('times new roman',15),textvariable=self.var_course,bg="lightyellow").place(x=200,y=140)
        txt_address=Entry(frame,font=('times new roman',15),textvariable=self.var_address,bg="lightyellow").place(x=200,y=180)

        btn_generate=Button(frame,text='Generate QR',command=self.generate,font=("times new roman",18,'bold'),bg='#00b36b',fg='white').place(x=90,y=250,width=180,height=30)
        btn_clear=Button(frame,text='Clear', command=self.clear,font=("times new roman",18,'bold'),bg='#00cc7a',fg='white').place(x=282,y=250,width=180,height=30)
        self.msg=''
        self.lbl_msg=Label(frame,text=self.msg,font=("times new roman",25,'bold'),bg='white',fg='#00995c')
        self.lbl_msg.place(x=0,y=310)
        #Student QR code window
        qr_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_frame.place(x=600,y=100,width=250,height=380)
        enroll_title=Label(qr_frame,text="Student QR Code",font=("goudy old style",20),bg='#00b36b',fg='white').place(x=0,y=0,relwidth=1)
        # Label(,font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)             
        self.qr_code=Label(qr_frame,text="Not available",font=('times new roman',15),bg='#00b36b',fg="white")
        self.qr_code.place(x=35,y=100,width=180,height=180)
    def clear(self):
        self.var_stu_code.set('')
        self.var_name.set('')
        self.var_course.set('')
        self.var_address.set('')
        self.msg=""
        self.lbl_msg.config(text=self.msg)

    def generate(self):
        if self.var_stu_code.get()=='' or self.var_name=='' or self.var_course=='' or self.var_address=='':
            self.msg="All Fields are Required"
            self.lbl_msg.config(text=self.msg,fg="red")
        else:
            qr_data=(f"Student Id:{self.var_stu_code.get()}\nStudent Name:{self.var_name.get()}\nStudent Course:{self.var_course.get()}\nStudent Adress:{self.var_address.get()}")
            qr_code=qrcode.make(qr_data)
            print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("Student_QR"+str(self.var_stu_code.get())+'.png')
            #qr image update
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            #======update
            self.msg="QR Code generated successfully..."
            self.lbl_msg.config(text=self.msg,fg="green")

    

root=Tk()
obj=Qr_Generator(root)
root.mainloop()