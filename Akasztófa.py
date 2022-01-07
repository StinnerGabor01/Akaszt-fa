from tkinter import *
from tkinter import messagebox


def submit():
    global word
    global betük
    global canvas
    global hiba
    global input2
    global veg

    word=input1.get()
    betük= split(word)

    fel.destroy()
    input1.destroy()
    submit_button.destroy()
    csillag_gomb.destroy()

    hiba=0

    canvas.create_line(100, 330, 300, 330, width=10, fill="black")

    hiba_szam= Label(window, textvariable=hiba)
    hiba_szam.pack()

    üres_hely()

def split(i):
    return list(i)

def elrejtés():
    global input1
    input1.config(show="*")

def üres_hely():
    global betük
    global canvas
    global karakter
    global input2
    global vonalak
    global max
    global maxrow
    global maxcolumn

    for i in range(len(betük)):
        karakter+=1

    if karakter>45:
        window.destroy()

    canvas.place(x=10, y=100)

    input2.place(x=400, y=350)
    max.trace("w", lambda *args: character_limit(max))

    betü_button= Button(window, text="Betü megadása", command=betü_megjelenítés,)
    betü_button.place(x=400, y=320)

    frame= Frame(window)
    frame.place(x=30, y=450,)

    szo_veg=0
    for row in range(0,3):
        if szo_veg == karakter:
            maxrow=row-1
            maxcolumn=column
            break
        for column in range(0, 15):
            vonalak[row][column] = Label(frame, text="_ ", font=('consolas', 40), width=1, height=1,)
            vonalak[row][column].grid(row=row,column=column)
            szo_veg+=1

            if szo_veg == karakter:
                break

    helyr= 0
    helyc = -1
    for i in betük:
        helyc += 1
        if helyc==15:
            helyc=0
            helyr+=1

        if i == " ":
            vonalak[helyr][helyc].config(text=i)
            global veg
            veg+= 1

def character_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[-1])

def pluszhiba():
    global hiba
    global canvas

    hiba+=1

    if hiba==1:
        canvas.create_line(100, 330, 100, 30, width=10, fill="black")

    elif hiba==2:
        canvas.create_line(97, 30, 300, 30, width=10, fill="black")

    elif hiba==3:
        canvas.create_line(300, 30, 300, 80, width=10, fill="black")

    elif hiba==4:
        canvas.create_oval(273,80,325,130, width=5, )

    elif hiba==5:
        canvas.create_line(297, 130, 297, 150, width=5, fill="black")

    elif hiba==6:
        canvas.create_rectangle(273, 150, 325, 220, width=5,)

    elif hiba==7:
        canvas.create_line(273, 150, 220, 180, width=6, fill="black")

    elif hiba==8:
        canvas.create_line(325, 150, 378, 180, width=6, fill="black")

    elif hiba==9:
        canvas.create_line(290, 220, 290, 280, width=6, fill="black")

    elif hiba>=10:
        canvas.create_line(308, 220, 308, 280, width=6, fill="black")
        if messagebox.askyesno(title="Vesztettél!", message="Az akasztás végrehajtva! Te vesztettél."
                                                         "Szeretnéd megnézni a megfejtést?"):
            helyr=0
            helyc=-1
            for i in betük:
                helyc += 1
                if helyc==15:
                    helyc=0
                    helyr += 1
                for j in all:
                    if i.lower() == j:
                        vonalak[helyr][helyc].config(text=i)

def betü_megjelenítés():
    global betük
    global input2
    global canvas
    global vonalak
    global veg
    global volt
    global maxrow
    global maxcolumn

    helyc=-1
    helyr=0
    nem=0
    for a in range(3):
        for i in betük:
            helyc+=1
            if helyc==15:
                helyc=0
                helyr+=1

            if helyr>= maxrow and helyc>=maxcolumn:
                break

            if input2.get().lower() in volt and nem==0 :
                messagebox.showinfo(title="Volt már",message="Ez a betű már volt.")
                nem+=1
                break

            elif i.lower()==input2.get().lower() and i!=" ":
                vonalak[helyr][helyc].config(text=i)
                volt.append(input2.get().lower())
                veg+=1
                nem+=1

                if veg==karakter:
                    messagebox.showinfo(title="Nyertél!", message="Nyertél!")
                    break

        if helyr >= maxrow and helyc >= maxcolumn:
            break

    if nem==0 and i!=" ":
        pluszhiba()
        volt.append(input2.get().lower())

window= Tk()

window.geometry("600x670-400-55")
window.title("Akasztófa")

word=""
betük=""
karakter=0
hiba=IntVar()
veg=0
max=StringVar()
volt=[" "]
all=["ö","ü","ó","q","w","e","r","t","z","u","i","o","p","ő","ú","a","s","d","f","g","h","j","k","l","é","á","ű","í","y","x","c","v","b","n","m","0","1","2","3","4","5","6","7","8","9","&","@","<",">","[","]","{","}","#",",","?",";",".",":","-","*","_","/","'","","+","!","%","=","(",")","$","€",]
maxrow=""
maxcolumn=""


Label(window, text="Akasztófa", font=("Arial", 40),).pack()
fel=Label(window, text="Itt add meg a szót:", font=("Arial", 30))
fel.pack()
input1= Entry(window, font=("Arial", 35),)
input1.pack()

submit_button= Button(window, text="Szó megadása", command=submit, font=("Arial", 20))
submit_button.place(x=100, y=180)

csillag_gomb=Button(window,text="Szó elrejtés", command=elrejtés, font=("Arial", 20))
csillag_gomb.place(x=350, y=180)

canvas = Canvas(window, width=400, height=350)

input2 = Entry(window, textvariable=max)

vonalak= [["_","_","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ "],
          ["_","_","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ "],
          ["_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ "]]

window.mainloop()