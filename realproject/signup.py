from tkinter import *
from tkinter import messagebox
import ast
import mysql.connector
from subprocess import call

window=Tk()
window.title("Sign up")
window.geometry('925x500+300+200')
window.configure(bg="#fff")
window.resizable(False,False)



def signup():
        username=user.get()
        password=code.get()
        conformpassword = conform_code.get()

        if username == 'Username' or password == 'Password' or conformpassword == 'Conformpassword':
            messagebox.showerror('Invalid','You need to fill all field!')
        else:

            conn=mysql.connector.connect(host="localhost",user="root",password="Mkmysql2402",database="Mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from signup where username =%s",(
                                                                    user.get(),
            ))
            data = my_cursor.fetchall()
            if data:
                messagebox.showerror("Error","Username already exist")
            else:
                if password==conformpassword:
                    my_cursor.execute("insert into signup values(%s,%s)",(
                                                                    user.get(),
                                                                    code.get()
                                                            
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","User has been inserted")
                else:
                    messagebox.showerror('Invalid','Both password should match')

def signin():
    window.destroy()
    call(["python","login.py"])

img = PhotoImage(file='login.png')
Label(window,image=img,bg='white').place(x=50,y=80)



Label(window,border=0,bg='white').place(x=50,y=90)

frame=Frame (window,width=350, height=390, bg="#fff") 
frame.place(x=480,y=50)

heading=Label(frame, text='Sign up',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light' ,23, 'bold'))  
heading.place(x=100,y=5)

#---------username

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    if user.get()=='':
     user.insert(0,'Username')

user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter) 
user.bind('<FocusOut>', on_leave)


Frame (frame, width=295, height=2,bg='black').place(x=25,y=107)

#--------- password

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    if code.get()=='':
     code.insert(0,'Password')

code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter) 
code.bind('<FocusOut>', on_leave)


Frame (frame, width=295, height=2,bg='black').place(x=25,y=177)

#---------confirm password

def on_enter(e):
    conform_code.delete(0, 'end')

def on_leave(e):
    if conform_code.get()=='':
     conform_code.insert(0,'Confirm Password')

conform_code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
conform_code.place(x=30,y=220)
conform_code.insert(0,'Confirm Password')
conform_code.bind('<FocusIn>', on_enter) 
conform_code.bind('<FocusOut>', on_leave)


Frame (frame, width=295, height=2,bg='black').place(x=25,y=247)


Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
label = Label(frame,text="I have an account",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place (x=90, y=340)

signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signin)
signin.place(x=200,y=340)


window.mainloop()