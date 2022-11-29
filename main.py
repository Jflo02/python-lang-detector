from tkinter import *
from langdetect import detect
from langcodes import *

fenetre = Tk()


class DetectLanguage:

    def __init__(self, fenetre):

        fenetre.title("Quelle langue parles tu ?")
        fenetre.configure(bg='grey')

        text = Label(fenetre, text="Texte :")
        text.place(x=20, y=20)
        text.configure(bg='grey')

        self.text_unkown_language = StringVar()
        entree = Entry(
            fenetre, textvariable=self.text_unkown_language, width=100)
        entree.place(x=20, y=60, width=560, height=80)

        bouton = Button(fenetre, text="Detecter", command=self.set_language)
        bouton.pack()
        bouton.place(x=260, y=150)

        detection = Label(fenetre, text="Detection :")
        detection.configure(bg='grey')
        detection.place(x=20, y=200)

        self.language = StringVar()
        self.show_language = Label(fenetre, textvariable=self.language)
        self.show_language.pack()
        self.show_language.place(x=20, y=250, width=560, height=20)

    def set_language(self):
        self.language.set(Language.make(self.find_language()).autonym())
        print(self.find_language())
        print(Language.make(self.find_language()).autonym())

    def find_language(self):
        return detect(self.text_unkown_language.get())


DetectLanguage(fenetre)

fenetre.geometry("600x300")
fenetre.mainloop()
