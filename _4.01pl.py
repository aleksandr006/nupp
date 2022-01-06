from tkinter import *
klik=0
def klikker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)
    aken.geometry(str(aken.winfo_width()+10)+"x"+str(aken.winfo_height()+10))
def klikker_minus(event):
    global klik
    klik-=1
    lbl.configure(text=klik)
def txt_to_lbl (event):
    #pass
    text=txt.get()#From Entry to text
    lbl.configure(text=text)
    txt.delete(0,END)
def valik():
    valik_=var.get()
    lbl.configure(text=valik_)
    txt.insert(0,valik_)
def vihd(event):
    aken.destroy()
aken=Tk()
aken.title("Akna nimetus")
aken.geometry("600x500")
knopka=Button(aken,text="ja knopka",font="Arial 20",fg="red",bg="lightblue",height=4,width=20,relief=GROOVE)
knopka.bind(aken.destroy)


nupp=Button(aken,text="Mina olen nupp\nValjuta mind!",font="Arial 20",fg="red",bg="lightblue",height=4,width=20,relief=GROOVE)#RAISED, SUNKEN
nupp.bind("<Button-1>",klikker)
nupp.bind("<Button-3>",klikker_minus)
lbl=Label(aken,text="...",font="Arial 20",height=4,width=20,relief=GROOVE,bg="lightblue")
txt=Entry(aken,width=20,relief=GROOVE,bg="lightblue",justify=CENTER)
txt.bind("<Return>",txt_to_lbl)#enter
i1=PhotoImage(file="gif.gif")
i2=PhotoImage(file="giphy (1).gif")
i3=PhotoImage(file="giphy (2).gif")
var=StringVar()
var.set("üks")
r1=Radiobutton(aken,image=i1 ,variable=var,value="üks",command=valik)
r2=Radiobutton(aken,image=i2,variable=var,value="kaks",command=valik)
r3=Radiobutton(aken,image=i3,variable=var,value="kolm",command=valik)
lbl.pack()
nupp.pack()#side=LEFT
knopka.pack()
txt.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)

aken.mainloop()
