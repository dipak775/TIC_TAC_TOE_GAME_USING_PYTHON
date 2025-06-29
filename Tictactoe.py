from tkinter import*
root=Tk()
root.geometry("350x350")
root.resizable(0,0)
root.title("TIC TAC TOE")
root.configure(background="black")
n=1
def nam(a):
    global n
    if(a["text"]==""):
        if(n%2==0):
            a["text"]="O"
            va="O"
        else:
            a["text"]="X"
            va="X"
        n+=1
    if(b1["text"]==b2["text"]==b3["text"]==va):
        print("player ",va," won")
        exit()
    elif(b4["text"]==b5["text"]==b6["text"]==va):
        print("player ",va," won")
        exit()
    elif(b7["text"]==b8["text"]==b9["text"]==va):
        print("player ",va," won")
        exit()
    elif(b1["text"]==b4["text"]==b7["text"]==va):
        print("player ",va," won")
        exit()
    elif(b2["text"]==b5["text"]==b8["text"]==va):
        print("player ",va," won")
        exit()
    elif(b3["text"]==b6["text"]==b9["text"]==va):
        print("player ",va," won")
        exit()
    elif(b1["text"]==b5["text"]==b9["text"]==va):
        print("player ",va," won")
        exit()
    elif(b7["text"]==b5["text"]==b3["text"]==va): 
        print("player ",va," won")
        exit()

b1=Button(root,background="gold",foreground="blue",command=lambda:nam(b1))
b1.place(x=10,y=10,height=100,width=100)
b2=Button(root,background="gold",foreground="blue",command=lambda:nam(b2))
b2.place(x=120,y=10,height=100,width=100)
b3=Button(root,background="gold",foreground="blue",command=lambda:nam(b3))
b3.place(x=230,y=10,height=100,width=100)
b4=Button(root,background="gold",foreground="blue",command=lambda:nam(b4))
b4.place(x=10,y=120,height=100,width=100)
b5=Button(root,background="gold",foreground="blue",command=lambda:nam(b5))
b5.place(x=120,y=120,height=100,width=100)
b6=Button(root,background="gold",foreground="blue",command=lambda:nam(b6))
b6.place(x=230,y=120,height=100,width=100)
b7=Button(root,background="gold",foreground="blue",command=lambda:nam(b7))
b7.place(x=10,y=230,height=100,width=100)
b8=Button(root,background="gold",foreground="blue",command=lambda:nam(b8))
b8.place(x=120,y=230,height=100,width=100)
b9=Button(root,background="gold",foreground="blue",command=lambda:nam(b9))
b9.place(x=230,y=230,height=100,width=100)

root.mainloop()
