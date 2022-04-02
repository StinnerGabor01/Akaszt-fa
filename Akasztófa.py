from tkinter import *
from tkinter import messagebox

class Game():
    def __init__(self):
        self.word = ""
        self.betük = ""
        self.karakter = 0
        self.hiba = IntVar()
        self.veg = 0
        self.volt = [" ", ""]
        self.all = ["ö", "ü", "ó", "q", "w", "e", "r", "t", "z", "u", "i", "o", "p", "ő", "ú", "a", "s", "d", "f", "g", "h",
               "j", "k", "l", "é", "á", "ű", "í", "y", "x", "c", "v", "b", "n", "m", "0", "1", "2", "3", "4", "5", "6",
               "7", "8", "9", "&", "@", "<", ">", "[", "]", "{", "}", "#", ",", "?", ";", ".", ":", "-", "*", "_", "/",
               "'", "", "+", "!", "%", "=", "(", ")", "$", "€", ]
        self.maxrow = ""
        self.maxcolumn = ""

        self.canvas = Canvas(window, width=400, height=350)

        self.vonalak = [["_", "_", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ "],
                   ["_", "_", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ "],
                   ["_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ "]]

    def sp(self,word):
        return list(word)

    def submit(self):
        self.word=input1.get()
        self.betük= self.sp(self.word)

        fel.destroy()
        input1.destroy()
        submit_button.destroy()
        csillag_gomb.destroy()

        self.hiba=0

        self.canvas.create_line(100, 330, 300, 330, width=10, fill="black")

        hiba_szam= Label(window, textvariable=self.hiba)
        hiba_szam.pack()

        self.üres_hely()

    def elrejtés(self):

        input1.config(show="*")

    def üres_hely(self):

        for i in range(len(self.betük)):
            self.karakter+=1

        if self.karakter>45:
            window.destroy()

        self.canvas.place(x=10, y=100)

        input2.place(x=400, y=350)
        max.trace("w", lambda *args: self.character_limit(max))

        betü_button= Button(window, text="Betü megadása", command=self.betü_megjelenítés,)
        betü_button.place(x=400, y=320)

        frame= Frame(window)
        frame.place(x=30, y=450,)

        szo_veg=0
        for row in range(0,3):
            if szo_veg == self.karakter:
                self.maxrow=row-1
                self.maxcolumn=column
                break
            for column in range(0, 15):
                self.vonalak[row][column] = Label(frame, text="_ ", font=('consolas', 40), width=1, height=1,)
                self.vonalak[row][column].grid(row=row,column=column)
                szo_veg+=1

                if szo_veg == self.karakter:
                    break

        helyr= 0
        helyc = -1
        for i in self.betük:
            helyc += 1
            if helyc==15:
                helyc=0
                helyr+=1

            if i == " ":
                self.vonalak[helyr][helyc].config(text=i)
                self.veg+= 1

    def character_limit(self,entry_text):
        if len(entry_text.get()) > 0:
            entry_text.set(entry_text.get()[-1])

    def pluszhiba(self):

        self.hiba+=1

        if self.hiba==1:
            self.canvas.create_line(100, 330, 100, 30, width=10, fill="black")

        elif self.hiba==2:
            self.canvas.create_line(97, 30, 300, 30, width=10, fill="black")

        elif self.hiba==3:
            self.canvas.create_line(300, 30, 300, 80, width=10, fill="black")

        elif self.hiba==4:
            self.canvas.create_oval(273,80,325,130, width=5, )

        elif self.hiba==5:
            self.canvas.create_line(297, 130, 297, 150, width=5, fill="black")

        elif self.hiba==6:
            self.canvas.create_rectangle(273, 150, 325, 220, width=5,)

        elif self.hiba==7:
            self.canvas.create_line(273, 150, 220, 180, width=6, fill="black")

        elif self.hiba==8:
            self.canvas.create_line(325, 150, 378, 180, width=6, fill="black")

        elif self.hiba==9:
            self.canvas.create_line(290, 220, 290, 280, width=6, fill="black")

        elif self.hiba>=10:
            self.canvas.create_line(308, 220, 308, 280, width=6, fill="black")
            if messagebox.askyesno(title="Vesztettél!", message="Az akasztás végrehajtva! Te vesztettél."
                                                             "Szeretnéd megnézni a megfejtést?"):
                helyr=0
                helyc=-1
                for i in self.betük:
                    helyc += 1
                    if helyc==15:
                        helyc=0
                        helyr += 1
                    for j in self.all:
                        if i.lower() == j:
                            self.vonalak[helyr][helyc].config(text=i)

    def betü_megjelenítés(self):
        helyc=-1
        helyr=0
        nem=0
        megvolt=0
        for a in range(3):
            for i in self.betük:
                helyc+=1
                if helyc==15:
                    helyc=0
                    helyr+=1

                if helyr>= self.maxrow and helyc>self.maxcolumn:
                    break

                if input2.get().lower() in self.volt and nem==0 :
                    messagebox.showinfo(title="Volt már",message="Ez a betű már volt.")
                    nem+=1
                    megvolt+=1
                    break

                elif i.lower()==input2.get().lower() and megvolt==0:
                    self.vonalak[helyr][helyc].config(text=i)
                    self.volt.append(input2.get().lower())
                    self.veg+=1
                    nem+=1

                    if self.veg==self.karakter:
                        messagebox.showinfo(title="Nyertél!", message="Nyertél!")
                        break

            if helyr >= self.maxrow and helyc > self.maxcolumn:
                break

        if nem==0 and i!=" ":
            self.pluszhiba()
            self.volt.append(input2.get().lower())

window= Tk()

window.geometry("600x670-400-55")
window.title("Akasztófa")

Label(window, text="Akasztófa", font=("Arial", 40),).pack()
fel=Label(window, text="Itt add meg a szót:", font=("Arial", 30))
fel.pack()
input1= Entry(window, font=("Arial", 35),)
input1.pack()

game= Game()

submit_button= Button(window, text="Szó megadása", command=game.submit, font=("Arial", 20))
submit_button.place(x=100, y=180)

csillag_gomb=Button(window,text="Szó elrejtés", command=game.elrejtés, font=("Arial", 20))
csillag_gomb.place(x=350, y=180)

max = StringVar()
input2 = Entry(window, textvariable=max)

window.mainloop()
