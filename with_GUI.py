from tkinter import *
from tkinter import messagebox
import random
import non_GUI as TA


root = Tk()
root.geometry("800x600")
root.title("DwB Game's // Tebak Angka.")

# function

def start() :
    global nyawa
    global the_number
    nyawa = 5   # banyaknya kesempatan untuk menebak
    the_number = random.randint(1,50)   # angka acak
    user_number.delete(0,END)
    Label(root,text="Your Guess Number", font=("Stika Banner Regular",12), fg="green").place(x=440,y=120)
    user_number.config(state="normal")
    mainButton.config(text="S e a r c h",background="blue",fg="white",padx=8, command=searchNumber)
    mainButton.place(x=510,y=225)
    bantuanBool.config(text="Tebak !")
    bantuanBool.place(x=340, y=330)
    bantuanKata.config(text="")
    bantuanBanding.config(text="")
    numberPrivatFrame.config(text="  the number  ")
    theNumber.config(text=". . .")

def searchNumber():
    global nyawa
    global the_number
    try:
        player = int(user_number.get())
        if nyawa > 0:
            TA.helper(player,the_number)
            if player == the_number:
                nyawa = -22
                bantuanBool.config(text=" n i c e")
                bantuanBool.place(x=330, y=330)
                bantuanKata.config(text="Tebakan Anda ")
                bantuanKata.place(x=315,y=387)
                bantuanBanding.config(text="Benar!")
                numberPrivatFrame.config(text="  the number  ")
                theNumber.config(text=f"= {the_number}")
            elif player > the_number:
                nyawa -= 1
                bantuanBool.config(text=TA.help)
                if TA.help==" mendekati," :
                    bantuanBool.place(x=305, y=330)
                else:
                    bantuanBool.place(x=290, y=330)
                bantuanKata.config(text="Pilihan Anda ")
                bantuanKata.place(x=325,y=387)
                bantuanBanding.config(text="Lebih Besar.")
                bantuanBanding.place(x=425,y=385)
                numberPrivatFrame.config(text=f" tersisa {nyawa} chance ")
            else:
                nyawa -= 1
                bantuanBool.config(text=TA.help)
                if TA.help==" mendekati," :
                    bantuanBool.place(x=305, y=330)
                else:
                    bantuanBool.place(x=290, y=330)
                bantuanKata.config(text="Pilihan Anda ")
                bantuanKata.place(x=325,y=387)
                bantuanBanding.config(text="Lebih Kecil.")
                bantuanBanding.place(x=425,y=385)
                numberPrivatFrame.config(text=f" tersisa {nyawa} chance ")

    except ValueError:
        messagebox.showerror("ValueError!","Yang Anda Input Bukan Angka.")


    if nyawa == 0:
        bantuanBool.config(text="you lose")
        bantuanBool.place(x=320, y=330)
        bantuanKata.config(text="Nice Try, ")
        bantuanKata.place(x=325,y=387)
        bantuanBanding.config(text="Coba Lagi!")
        bantuanBanding.place(x=400,y=385)
        numberPrivatFrame.config(text="  the number  ")
        theNumber.config(text=f"{the_number}")
        nyawa = -22

    if nyawa == -22:
        mainButton.config(text="Main Lagi", background="green", fg="white", command=start)


    

def mainUlang():
    pass
# /Function

# Load Image
entryBgImg = PhotoImage(file="img/search_png.png")

# Title
Label(root, text="GUESS THE NUMBER", font=("DRYME PERSONAL USE", 30)).pack(pady=10)
# /title

# Rules
ruleFrame=LabelFrame(root,text="  Rules  ", font=("DRYME PERSONAL USE",18),fg="red", bd=5)
ruleFrame.place(x=20, y=120)
Label(ruleFrame, text="- Tebak Angka 0 s/d 50!", font=("",15)).grid(row=0, column=0, pady=4, sticky="w")
Label(ruleFrame, text="- Punya 5 Kesempatan untuk Menebak.", font=("",15)).grid(row=1, column=0, pady=4, sticky="w")
Label(ruleFrame, text="- Menang Jika Berhasil Menebak.", font=("",15)).grid(row=2, column=0, pady=4, sticky="w")
# /rules

# User number input 
Label(root, image=entryBgImg).place(x=410,y=130)
user_number = Entry(root, textvariable=StringVar(),state="disabled",width=17, bd=0, font=("arial",20), justify="center")
user_number.place(x=450,y=162)

# Enter Button
mainButton = Button(root,text="Start Game Here",borderwidth=0,cursor="hand2",bd=0,padx=4,pady=2,font=("Stencil",16),background="yellow", fg="orange", command=start)
mainButton.place(x=480,y=225)

# 
bantuanBool = Label(root, text="s t a r t", font=("DRYME PERSONAL USE", 30), fg="red")
bantuanBool.place(x=330, y=330)
#
bantuanKata = Label(root, text="", font=("Verdana Regular", 13))
bantuanKata.place(x=255,y=387)
bantuanBanding = Label(root, text="", font=("Verdana Bold", 13), fg="green")
bantuanBanding.place(x=426,y=385)

# Nomor Rahasia nya
numberPrivatFrame = LabelFrame(root, text="start the game", font=("Stencil", 15), borderwidth=5)
numberPrivatFrame.place(x=330,y=420)
theNumber = Label(numberPrivatFrame, text="0", font=("Verdana Bold", 15), fg="red")
theNumber.pack(pady=2)


root.mainloop()