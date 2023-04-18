from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
from subprocess import call


class Airplane:
    def __init__(self,root):
        self.root = root
        self.root.title("Airplane Management System")
        self.root.geometry("1540x800+0+0")


        self.Departure=StringVar()
        self.Destination =StringVar()
        self.Flight =StringVar()
        self.Distance =StringVar()
        self.Time =StringVar()
        self.Date =StringVar()



        btnTitle=Label(self.root,bd=20,text="AIRLINE BOOKING MANAGEMENT SYSTEM",bg="dodgerblue1",fg="white",font=("#0084FF",15,"bold"),width=23,padx=2,pady=4)
        btnTitle.pack(side=TOP,fill=X)


        #========= Dataframe ============================================

        DataSignOutframe=Frame(self.root,bd=20)
        DataSignOutframe.place(x=0,y=70,width=1530,height=50)
        
        Dataframe=Frame(self.root,bd=20)
        Dataframe.place(x=0,y=120,width=1530,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                                            font=("times new roman",12,"bold"),text="Flight Information")
        DataframeLeft.place(x=0,y=5,width=980,height=300)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                                        font=("times new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=300)

        #========= buttons frame ============================================

        Buttonframe=Frame(self.root,bd=20)
        Buttonframe.place(x=0,y=460,width=1530,height=70)


        #========= Details frame ============================================

        Detailsframe=Frame(self.root,bd=20)
        Detailsframe.place(x=0,y=550,width=1530,height=320)


        #========= DataSignOutframe ============================================

        sign_up=Button(DataSignOutframe,width=12,text='Log Out', command= self.signin,cursor='hand2',fg='white',bg="dodgerblue1")
        sign_up.place(x=1360,y=0)


        #========= DataframeLeft ============================================


        lblTablet=Label(DataframeLeft,font=("arial",12,"bold"),text="Departure:",padx=2,pady=6)
        lblTablet.grid(row=0,column=0,sticky=W)
        txtTablet=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Departure,width=40)
        txtTablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Destination:",padx=2,pady=6)
        lblref.grid(row=2,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Destination,width=40)
        txtref.grid(row=2,column=1)

        lblDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Distance:",padx=2,pady=6)
        lblDose.grid(row=4,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Distance,width=40)
        txtDose.grid(row=4,column=1)


        lblFurtherinfo=Label(DataframeLeft,font=("arial",12,"bold"),text="Flight:",padx=2,pady=25)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Flight,width=40)
        txtFurtherinfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,font=("arial",12,"bold"),text="Date:",padx=2,pady=25)
        lblBloodPressure.grid(row=2,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Date,width=40)
        txtBloodPressure.grid(row=2,column=3)

        lblStorage=Label(DataframeLeft,font=("arial",12,"bold"),text="Time:",padx=2,pady=25)
        lblStorage.grid(row=4,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Time,width=40)
        txtStorage.grid(row=4,column=3)


        sign_up=Button(DataframeLeft,width=12,text='Show all flights', command= self.fatch_all_data,bg='white',cursor='hand2',fg='#57a1f8')
        sign_up.place(x=780,y=220)
    

        #========= DataframeRight ============================================
        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=13,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #========= Buttons ============================================
        btnPrescription=Button(Buttonframe,command=self.fatch_search_data,text="Search",bg="dodgerblue1",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=8)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,command=self.iPrescriptionData,text="Save",bg="dodgerblue1",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=8)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,command=self.update_data,text="Update",bg="dodgerblue1",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=8)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="dodgerblue1",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=8)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="dodgerblue1",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=8)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,command=self.iExit,text="Exit",bg="dodgerblue1",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=8)
        btnExit.grid(row=0,column=5)


        #======================Table ============================================
        #========= Scrollbar ============================================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("Departure", "Flight", "Destination", "Distance", "Date", "Time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=BOTTOM,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("Departure",text="Departure")
        self.hospital_table.heading("Flight",text="Flight")
        self.hospital_table.heading("Destination",text="Destination")
        self.hospital_table.heading("Distance",text="Distance")
        self.hospital_table.heading("Date",text="Date")
        self.hospital_table.heading("Time",text="Time")

        self.hospital_table["show"]="headings"


        self.hospital_table.column("Departure",width=100)
        self.hospital_table.column("Flight",width=100)
        self.hospital_table.column("Destination",width=100)
        self.hospital_table.column("Distance",width=100)
        self.hospital_table.column("Date",width=100)
        self.hospital_table.column("Time",width=100)
    
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fatch_data()
       

       #======================Functionality Declaration ============================================

    def signin(self):
        root.destroy()
        call(["python","login.py"])

    def iPrescriptionData(self):
        if self.Departure.get()=="" or self.Flight.get()=="" or self.Destination.get()=="" or self.Distance.get() == " " or self.Date.get() == "" or self.Time.get() =="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Mkmysql2402",database="Mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from hospital where Flight =%s",(
                                                                self.Flight.get(),
            ))
            data = my_cursor.fetchall()
            # print(data)
            self.clear_prescrtption()
            if data:
                messagebox.showerror("Error","Flight already exist")
            else:
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s)",(

                                                                    self.Departure.get(),
                                                                    self.Flight.get(),
                                                                    self.Destination.get(),
                                                                    self.Distance.get(),
                                                                    self.Date.get(),
                                                                    self.Time.get(),
                                                                
                ))
                self.iPrectioption()
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("Success","Record has been inserted")

    
   

    def update_data(self):
        conn=mysql.connector.connect(host="localhost", user="root", password="Mkmysql2402", database="Mydata")
        my_cursor=conn.cursor()
        self.clear_prescrtption()
        
        my_cursor.execute("update hospital set Departure=%s, Destination=%s, Distance=%s, Date=%s, Time =%s where Flight=%s",(
                                                                self.Departure.get(),
                                                                self.Destination.get(),
                                                                self.Distance.get(),
                                                                self.Date.get(),
                                                                self.Time.get(),
                                                                self.Flight.get(),
                                                                
        )) 
       

        conn.commit()
        self.fatch_data()
        self.iPrectioption()
        conn.close()
        messagebox.showinfo("Update","Flight has been updated successfully")

        
    def fatch_search_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Mkmysql2402",database="Mydata")
        

        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital where Departure =%s or Destination=%s or Distance=%s or Date=%s or Time=%s or Flight=%s",(
                                                                self.Departure.get(),
                                                                self.Destination.get(),
                                                                self.Distance.get(),
                                                                self.Date.get(),
                                                                self.Time.get(),
                                                                self.Flight.get(),
        ))
        
       

        rows=my_cursor.fetchall()
        
        self.hospital_table.delete(*self.hospital_table.get_children())
        for i in rows:
            self.hospital_table.insert("",END,values=i)
        conn.commit()
        conn.close()


    def fatch_search_data1(self):
        self.hospital_table.delete(*self.hospital_table.get_children())

    def fatch_all_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Mkmysql2402",database="Mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        for i in rows:
                self.hospital_table.insert("",END,values=i)
        conn.commit()
        conn.close()

        

    
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Mkmysql2402",database="Mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        if len(rows)==0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values="")
            conn.commit()
        conn.close()
        

    def get_cursor(self,event=""):
        self.clear_prescrtption()
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]            
        self.Departure.set(row[0])
        self.Flight.set(row[1])
        self.Destination.set(row[2])
        self.Distance.set(row[3])
        self.Date.set(row[4])
        self.Time.set(row[5])
        self.iPrectioption()


    def iPrectioption(self):
        
        self.txtPrescription.insert(END,"Departure:\t\t\t"+self.Departure.get()+"\n")
        self.txtPrescription.insert(END,"Destination:\t\t\t"+self.Flight.get()+"\n")
        self.txtPrescription.insert(END,"Flight:\t\t\t"+self.Destination.get()+"\n")
        self.txtPrescription.insert(END,"Distance:\t\t\t"+self.Distance.get()+"\n")
        self.txtPrescription.insert(END,"Date:\t\t\t"+self.Date.get()+"\n")
        self.txtPrescription.insert(END,"Time:\t\t\t"+self.Time.get()+"\n")
    

    
    def idelete(self):
        conn=mysql.connector.connect(host="localhost", user="root", password="Mkmysql2402", database="Mydata")
        my_cursor=conn.cursor()
        query="delete from hospital where Flight=%s"
        value=(self.Flight.get(),)
        my_cursor.execute(query,value)
        
        self.clear()

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete","Flight has been delete successfully")


    def clear_prescrtption(self):
        self.txtPrescription.delete("1.0",END)

    def clear(self):
        self.Departure.set("")
        self.Flight.set("")
        self.Destination.set("")
        self.Distance.set("")
        self.Date.set("")
        self.Time.set("")
        self.txtPrescription.delete("1.0",END)

    def iExit(self):
        iExit=messagebox.askyesno("Airplane managemnt system","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return

                



root=Tk()
ob=Airplane(root)
root.mainloop()








