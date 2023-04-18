from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from subprocess import call
import mysql.connector

root=Tk()
root.title('login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)


def signup():   
    root.destroy()
    call(["python","signup.py"])


def signin():
    username=user.get()
    password=code.get()

    conn=mysql.connector.connect(host="localhost",user="root",password="Mkmysql2402",database="Mydata")
    my_cursor=conn.cursor()
    if username == 'Username' or password == 'Password':
        print("Error!")
        messagebox.showerror('Invalid','You need to fill both field!')
    else:
        my_cursor.execute("select * from signup where username =%s",(
                                                                user.get(),
        ))
        data = my_cursor.fetchall()
        print(data)
        if data:
            my_cursor.execute("select password from signup where username =%s",(
                                                                user.get(),
            ))
            check_password = my_cursor.fetchall()
            value = check_password[0][0]
            # print(my_cursor.fetchall())
            # print(check_password)
            print(value + " hello")
            if password == value:
                root.destroy()
                call(["python","airplane.py"])
            else:
                messagebox.showerror('Invalid','Invalid password!')
        else:
            messagebox.showerror('Invalid','Username does not exist!')


img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=70)


frame=Frame (root,width=350, height=350, bg="white") 
frame.place (x=480,y=70)

heading=Label(frame, text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light' ,23, 'bold'))  
heading.place(x=100,y=5)

Frame (frame, width=295, height=2,bg='black').place(x=25,y=107)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
     user.insert(0,'Username')

user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter) 
user.bind('<FocusOut>', on_leave)


Frame (frame, width=295, height=2,bg='black').place(x=25,y=107)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')



code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place (x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter) 
code.bind('<FocusOut>', on_leave)

Frame (frame, width=295, height=2,bg= 'black').place(x=25,y=177)
Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label = Label(frame,text="Dont have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place (x=75, y=270)
sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup)
sign_up.place(x=215,y=270)

root.mainloop()