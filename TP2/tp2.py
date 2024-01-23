from tkinter import *
import webbrowser

def appuyer(selection):
    global entry
    if selection == "=":
        print(entry.get())
        calculer()
        return
    elif selection in {'+', '-', '*', '/'}:
        print(entry.get())
        # Vérifiez si l'opérateur est le premier caractère saisi
        if not entry.get() or entry.get()[-1] in {'+', '-', '*', '/'}:
            return  # Évitez de répéter les opérateurs
    entry.set(entry.get() + str(selection))
    equation.set(entry.get())


def calculer():
    try:
        result = str(eval(entry.get()))
        equation.set(result)
        entry.set(result)
    except:
        equation.set("Erreur")
        entry.set("")

def effacer():
    entry.set("")
    equation.set("")

def effacerLastEntry():
    newEntry = entry.get()
    newText = newEntry[0:-1]
    entry.set(newText)
    equation.set(newText)
    

def afficher_aide():
    webbrowser.open('https://fr.wikipedia.org/wiki/Calculatrice')


def mode_calculatrice_scientifique():

    nb_ligne = fenetre.grid_size()[1]
    if nb_ligne < 7:
        fenetre.grid_rowconfigure(nb_ligne,weight=1)
        boutonsSup = ('(',')')
        colonne = 0
        for bouton in boutonsSup:
            b = Label(fenetre, text=str(bouton), background="#101419", foreground="#FFF", height=4, width=12)
            # Dès qu'on appuie sur un bouton, on appelle la fonction appuyer
            b.bind("<Button-1>", lambda e, selection=bouton: appuyer(selection))
            b.grid(row=nb_ligne, column=colonne)
            colonne += 1


def mode_calculatrice_simple():
    nb_ligne = fenetre.grid_size()[1]
    nb_colonne = fenetre.grid_size()[0]
    if nb_ligne > 6:
        for col in range(nb_colonne):
            ligne_a_supprimer = fenetre.grid_slaves(row=nb_ligne-1, column=col)
            for widget in ligne_a_supprimer:
                widget.destroy()
        fenetre.grid_rowconfigure(nb_ligne-1,weight=0)


# Fenêtre générale
fenetre = Tk()
fenetre.title('Calculatrice')
fenetre.configure(background="#101419")

menu_principal = Menu(fenetre)
fenetre.config(menu=menu_principal)

menu_fichier = Menu(menu_principal, tearoff=0)# Menu "Aide"
menu_aide = Menu(menu_principal, tearoff=0)
menu_aide.add_command(label="Aide", command=afficher_aide)
menu_principal.add_cascade(label="Aide", menu=menu_aide)

# Menu "Mode Calculatrice"
menu_mode_calculatrice = Menu(menu_principal, tearoff=0)
menu_mode_calculatrice.add_command(label="Calculatrice Simple", command=mode_calculatrice_simple)
menu_mode_calculatrice.add_command(label="Calculatrice Scientifique", command=mode_calculatrice_scientifique)
menu_principal.add_cascade(label="Mode Calculatrice", menu=menu_mode_calculatrice)

#Affichage de la selection et equation pour el calcul
equation = StringVar()
entry = StringVar()

resultat = Label(fenetre, background="#101419", foreground="#FFF", textvariable=equation, height=2)
resultat.grid(columnspan=4)

# Boutons normaux
boutons = (7,8,9,"+",4,5,6,"-",1,2,3,"*",0,".","/","=")
ligne=1
colonne=0

for bouton in boutons:
    b = Label(fenetre, text=str(bouton), background="#101419", foreground="#FFF", height=4, width=12)
    # Dès qu'on appuie sur un bouton, on appelle la fonction appuyer
    b.bind("<Button-1>", lambda e, selection=bouton: appuyer(selection))
    b.grid(row=ligne, column=colonne)

    colonne += 1
    if colonne == 4:
        colonne = 0
        ligne += 1


b = Label(fenetre,text="AC",background="#900C3F",foreground="#FFF" ,height=4,width=12)
b.bind("<Button-1>",lambda e: effacer())
b.grid(row=5,column=0)

b = Label(fenetre,text="C",background="#900C3F",foreground="#FFF" ,height=4,width=12)
b.bind("<Button-1>",lambda e: effacerLastEntry())
b.grid(row=5,column=1)

fenetre.mainloop()