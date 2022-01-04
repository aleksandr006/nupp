from tkinter import *
klik=0
def klikker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)
def klikker_minus(event):
    global klik
    klik-=1
    lbl.configure(text=klik)
def txt_to_lbl (event):
    #pass
    text=txt.get()#From Entry to text
    lbl.configure(text=text)
aken=Tk()
aken.title("Akna nimetus")
aken.geometry("600x500")
nupp=Button(aken,text="Mina olen nupp\nValjuta mind!",font="Arial 20",fg="red",bg="lightblue",height=4,width=20,relief=GROOVE)#RAISED, SUNKEN
nupp.bind("<Button-1>",klikker)
nupp.bind("<Button-3>",klikker_minus)
lbl=Label(aken,text="...",font="Arial 20",height=4,width=20,relief=GROOVE,bg="lightblue")
txt=Entry(aken,width=20,relief=GROOVE,bg="lightblue",justify=CENTER)
txt.bind("<Return>",txt_to_lbl)#enter

lbl.pack()
nupp.pack()#side=LEFT
txt.pack()

aken.mainloop()