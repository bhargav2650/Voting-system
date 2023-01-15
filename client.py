from socket import *
from tkinter import *
from functools import partial

def sel(first,c,b,x):
    b["state"]="disabled"
    if x==0:
        c.send(bytes("1", "utf-8"))
    elif x==1:
        c.send(bytes("2", "utf-8"))
    elif x==2:
        c.send(bytes("3", "utf-8"))
    else:
        c.send(bytes("4", "utf-8"))
    first.destroy()
    
def validateLogin(c,username, password,tkWindow):
                  print(type(username))
                  
                  username=str(username.get())
                  password=str(password.get())
                  c.send(bytes(username, "utf-8"))
                  c.send(bytes(password, "utf-8"))
                  loginStatus=c.recv(1024).decode()
                  print(loginStatus)
                  tkWindow.destroy()
                  if loginStatus=='Login Success':
                    
                     first=Tk()
                     first.title("Voting Poll")
                     first.configure()
                     lab1=Label(first,width=20, text="Login Success.Please Vote.",font=('Arial Bold',25))
                     lab1=Label(first,width=20, text="Candidates",font=('Arial Bold',25))
                     lab1.grid(row=0,column=0)
                     lab7=Label(first,width=20, text="Party name",font=('Arial Bold',25))
                     lab7.grid(row=0,column=1)
                     lab2=Label(first,width=20,text="Voting Button",font=('Arial Bold',25))
                     lab2.grid(row=0,column=2)
                     lab3=Label(first,width=20,height=3,text="Bhargav",font=('Arial Bold',20))
                     lab3.grid(row=1,column=0)
                     lab8=Label(first,width=20,height=3,text="BJP",font=('Arial Bold',20))
                     lab8.grid(row=1,column=1)
                     b1=Button(first,padx=10,width=20,height=3, pady=10,bg="red",command=lambda: sel(first,c,b1,0))
                     b1.grid(row=1, column=2)
                     lab4=Label(first,width=20,height=3,text="Chaitu",font=('Arial Bold',20))
                     lab4.grid(row=2,column=0)
                     lab9=Label(first,width=20,height=3,text="People's Dragon",font=('Arial Bold',20))
                     lab9.grid(row=2,column=1)
                     b2=Button(first,padx=10,width=20,height=3, pady=10,bg="red",command=lambda: sel(first,c,b2,1))
                     b2.grid(row=2, column=2)
                     lab5=Label(first,width=20,height=3,text="Mahesh",font=('Arial Bold',20))
                     lab5.grid(row=3,column=0)
                     lab10=Label(first,width=20,height=3,text="Congress",font=('Arial Bold',20))
                     lab10.grid(row=3,column=1)
                     b3=Button(first,padx=10,width=20,height=3, pady=10,bg="red",command=lambda: sel(first,c,b3,2))
                     b3.grid(row=3, column=2)
                     lab6=Label(first,width=20,height=3,text="Manoj",font=('Arial Bold',20))
                     lab6.grid(row=4,column=0)
                     lab11=Label(first,width=20,height=3,text="Nation's Dictator",font=('Arial Bold',20))
                     lab11.grid(row=4,column=1)
                     b4=Button(first,padx=10,width=20,height=3,pady=10,bg="red",command=lambda: sel(first,c,b4,3))
                     b4.grid(row=4, column=2)
                     first.mainloop()
                  else:
                     print('\ninvalid login')
                     c.close()
                  return

c= socket(AF_INET, SOCK_STREAM)
c.connect(('localhost', 9999))
print(c.recv(1024).decode())
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Welcome to Online Voting System')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  
validateLogin = partial(validateLogin,c,username, password,tkWindow)
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

tkWindow.mainloop()
print(c.recv(1024).decode())
c.close()