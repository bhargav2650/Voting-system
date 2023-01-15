from socket import *
from tkinter import *
import threading
import matplotlib.pyplot as plt

def updategraph(i,data1):
    plt.bar(data1, i,width = 0.4)
    plt.show()
def servercode(s,i, lab8,lab9,lab10,lab11,userDictionary):
    while True:
        c, addr= s.accept()
        c.send(bytes("Login", "utf-8"))
        print("connected with ", addr)
        userName=str(c.recv(1024).decode())
        passWord=str(c.recv(1024).decode())
        print(userName)
        print(passWord)
        try:
            if userDictionary[userName] == passWord:
                c.send(bytes("Login Success","utf-8"))
                del userDictionary[userName]
                vote=int(c.recv(1024).decode())
                if vote==1:
                    i[0]+=1
                elif vote==2:
                    i[1]+=1
                elif vote==3:
                    i[2]+=1
                else:
                    i[3]+=1
                lab8.config(text="BJP               "+str(i[0]))
                lab9.config(text="People's Dragon   "+str(i[1]))
                lab10.config(text="Congress         "+str(i[2]))
                lab11.config(text="Nation's Dictator"+str(i[3]))
                print("1 vote casted at poll ", addr)
                c.send(bytes("Voting done","utf-8"))
                k=0
            else:
                c.send(bytes("Login failure","utf-8"))
        except:
            c.send(bytes("Login failure","utf-8"))

if __name__ == "__main__":
    s= socket(AF_INET, SOCK_STREAM)
    i=[0,0,0,0]
    userDictionary = {
        "AB001": "abcd",
        "AB002": "boss",
        "AB003": "pess"
        }
    data1=['Batboys',"People's Dragon" ,"Congress","Nation's Dictator"]
    first=Tk()
    first.title("Voting Poll")
    lab1=Label(first,width=20, text="Candidates  --  Votes",font=('Arial Bold',25))
    lab1.grid(row=0,column=0)
    lab8=Label(first,width=20,height=3,text="BJP               "+str(i[0]),font=('',20))
    lab8.grid(row=1,column=0)
    lab9=Label(first,width=20,height=3,text="People's Dragon   "+str(i[1]),font=('',20))
    lab9.grid(row=2,column=0)
    lab10=Label(first,width=20,height=3,text="Congress         "+str(i[2]),font=('',20))
    lab10.grid(row=3,column=0)
    lab11=Label(first,width=20,height=3,text="Nation's Dictator"+str(i[3]),font=('',20))
    lab11.grid(row=4,column=0)
    b3=Button(first,padx=10,width=20,height=3, pady=10,text="Analysis",bg="grey",command=lambda: updategraph(i,data1))
    b3.grid(row=5, column=0)
    s.bind(('localhost', 9999))
    s.listen(5)
    print("waiting for connections")
    t1 = threading.Thread(target=servercode, args=(s,i,lab8,lab9,lab10,lab11,userDictionary))
    t1.start()
    first.mainloop()

    
