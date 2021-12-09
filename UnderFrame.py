from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from lib_gestionEtudiants import modificationEtudiant, suppressionEtudiant, ajoutEtudiant
from lib_gestionNotes import modificationNote, suppressionNote, ajoutNote
from lib_commun import ouverture_fichier_csv

def tab_update():
    for i in tree.get_children():
        tree.delete(i)
    tree_merge()


def etudiant_verif_ajout(prenom, nom, genre, email, groupe):
    data = ouverture_fichier_csv("etudiants.csv")
    for i in range(1, len(data)):
        if (str(data[i][4]) == str(email.get())) or \
                ((str(data[i][2]) == str(nom.get())) and (str(data[i][3]) == str(prenom.get()))):
            messagebox.showerror("Erreur", "L'etudiant existe deja")
            return
    if (prenom.get() == "") or (nom.get() == "") or (email.get() == "") or (groupe.get() == ""):
        messagebox.showerror("Erreur", "Informations manquantes")
        return
    else:
        ajoutEtudiant(prenom.get(), nom.get(), genre.get(), email.get(), groupe.get())
        return


def etudiant_verif_modif(prenom, nom, genre, email, id):
    if (prenom.get() == "") or (nom.get() == "") or (email.get() == ""):
        messagebox.showerror("Erreur", "Informations manquantes")
        return
    else:
        data = ouverture_fichier_csv("etudiants.csv")
        id_ = id.get()
        for i in range(1, len(data)):
            if data[i][0] == id_:
                modificationEtudiant(id_, prenom.get(), nom.get(), genre.get(), email.get())
                return
        messagebox.showerror("Erreur", "ID erronné")
        return


def etudiant_verif_supprime(id):
    data = ouverture_fichier_csv("etudiants.csv")
    id_ = int(id.get())
    for i in range(1, len(data)):
        if int(data[i][0]) == id_:
            suppressionEtudiant(id_)
            suppressionNote(str(id), str("2021/2022"), str("Informatique"))
            suppressionNote(str(id), str("2021/2022"), str("Aeronotique"))
            suppressionNote(str(id), str("2021/2022"), str("Electronique"))
            suppressionNote(str(id), str("2021/2022"), str("Grand Projet")) 

            return
    messagebox.showerror("Erreur", "ID erronné")
    return


def note_verif_ajout(id, annee, matiere, note):
    data = ouverture_fichier_csv("notes.csv")
    data1 = ouverture_fichier_csv("etudiants.csv")
    for j in range(1, len(data1)):
        if data1[j][0] == id.get():
            for i in range(1, len(data)):
                if str(data[i][2]) == str(id.get()) and str(data[i][3]) == str(matiere.get()):
                    messagebox.showerror("Erreur", "L'etudiant a deja ete evalue sur cette matiere")
                    return
            if (id.get() == "") or (annee.get() == "") or (matiere.get() == "") or (note.get() == ""):
                messagebox.showerror("Erreur", "Informations manquantes")
                return
            else:
                ajoutNote(id.get(), annee.get(), matiere.get(), note.get())
                return
    messagebox.showerror("Erreur", "L'etudiant n'existe pas")
    return


def note_verif_modif(id, annee, matiere, note):
    data = ouverture_fichier_csv("notes.csv")
    data1 = ouverture_fichier_csv("etudiants.csv")
    for i in range(1, len(data1)):
        if data1[i][0] == id.get():
            if (id.get() == "") or (annee.get() == "") or (matiere.get() == "") or (note.get() == ""):
                messagebox.showerror("Erreur", "Informations manquantes")
                return
            else:
                for j in range(1, len(data)):
                    if (data[j][1] == annee.get()) and (data[j][2] == id.get()) and (data[j][3] == matiere.get()):
                        modificationNote(id.get(), annee.get(), matiere.get(), note.get())
                        return
                messagebox.showerror("Erreur", "La note n'existe pas")
                return
    messagebox.showerror("Erreur", "L'etudiant n'existe pas")
    return


def note_verif_suppr(id, annee, matiere):
    data = ouverture_fichier_csv("notes.csv")
    data1 = ouverture_fichier_csv("etudiants.csv")
    for i in range(1, len(data1)):
        if data1[i][0] == id.get():
            if (id.get() == "") or (annee.get() == "") or (matiere.get() == ""):
                messagebox.showerror("Erreur", "Informations manquantes")
                return
            else:
                for j in range(1, len(data)):
                    if (data[j][1] == annee.get()) and (data[j][2] == id.get()) and (data[j][3] == matiere.get()):
                        suppressionNote(id.get(), annee.get(), matiere.get())
                        return
                messagebox.showerror("Erreur", "La note n'existe pas")
    messagebox.showerror("Erreur", "L'etudiant n'existe pas")
    return


def Etudiant_Supprimer():
    nouveau = Toplevel(bg='#FF0101')
    nouveau.geometry("720x480")
    nouveau.title("Supprimer un etudiant")

    Lab = Label(nouveau, text="Saisissez l'identifiant de l'etudiant a supprimer", font=100)
    Lab.pack(pady=10)
    entree = Entry(nouveau)
    entree.pack()

    Btn0 = Button(nouveau, text="Annuler", bg='#FF8501', command=nouveau.destroy)
    Btn0.place(relx=0.575, rely=0.8, relwidth=0.15, relheight=0.1)

    Btn1 = Button(nouveau, text="Confirmer", bg='#FF8501', command=lambda: [
        etudiant_verif_supprime(entree), tab_update(), nouveau.destroy()])
    Btn1.place(relx=0.275, rely=0.8, relwidth=0.15, relheight=0.1)


def Etudiant_Modifier(prenom, nom, genre, email):
    nouveau1 = Toplevel(bg='#2c75ff')
    nouveau1.geometry("720x480")
    nouveau1.title("Modifier un etudiant")

    Lab = Label(nouveau1, text="Saisissez l'identifiant de l'etudiant a modifier", font=100)
    Lab.pack(pady=10)
    entree = Entry(nouveau1)
    entree.pack()

    Btn0 = Button(nouveau1, text="Annuler", bg='#7B01AD', command=nouveau1.destroy)
    Btn0.place(relx=0.575, rely=0.8, relwidth=0.15, relheight=0.1)

    Btn1 = Button(nouveau1, text="Confirmer", bg='#7B01AD', command=lambda: [
        etudiant_verif_modif(prenom, nom, genre, email, entree), tab_update(), nouveau1.destroy()])
    Btn1.place(relx=0.275, rely=0.8, relwidth=0.15, relheight=0.1)


def Note_Ajouter():
    add = Toplevel(bg='#01FF0C')
    add.geometry("720x480")
    add.title("Ajouter une note")

    Lab = Label(add, text="Saisissez pour ajouter une note", font=100)
    Lab.pack()

    Lab1 = Label(add, text="ID Etudiant")
    Lab1.place(relx=0.1, rely=0.15)
    Txt1 = Entry(add)
    Txt1.place(relx=0.3, rely=0.15)

    Lab2 = Label(add, text="Annee scolaire")
    Lab2.place(relx=0.1, rely=0.25)
    Txt2 = Entry(add)
    Txt2.place(relx=0.3, rely=0.25)

    Lab3 = Label(add, text="Matiere")
    Lab3.place(relx=0.1, rely=0.35)
    Txt3 = ttk.Combobox(add, state="readonly")
    Txt3["values"] = ('Informatique', 'Electronique', 'Aeronotique', 'Grand Projet')
    Txt3.place(relx=0.3, rely=0.35)

    Lab4 = Label(add, text="Note")
    Lab4.place(relx=0.1, rely=0.45)
    Txt4 = Entry(add)
    Txt4.place(relx=0.3, rely=0.45)

    Btn1 = Button(add, text="Confirmer", bg='#088F36', command=lambda: [
        note_verif_ajout(Txt1, Txt2, Txt3, Txt4), tab_update(), add.destroy()])
    Btn1.place(relx=0.25, rely=0.85, relwidth=0.2, relheight=0.075)

    Btn2 = Button(add, text="Annuler", bg='#088F36', command=add.destroy)
    Btn2.place(relx=0.55, rely=0.85, relwidth=0.2, relheight=0.075)


def Note_Modifier():
    mod = Toplevel(bg='#FCAAF3')
    mod.geometry("720x480")
    mod.title("Modifier une note")

    Lab = Label(mod, text="Saisissez pour modifier une note", font=100)
    Lab.pack()

    Lab1 = Label(mod, text="ID Etudiant")
    Lab1.place(relx=0.1, rely=0.15)
    Txt1 = Entry(mod)
    Txt1.place(relx=0.3, rely=0.15)

    Lab2 = Label(mod, text="Annee scolaire")
    Lab2.place(relx=0.1, rely=0.25)
    Txt2 = Entry(mod)
    Txt2.place(relx=0.3, rely=0.25)

    Lab3 = Label(mod, text="Matiere")
    Lab3.place(relx=0.1, rely=0.35)
    Txt3 = ttk.Combobox(mod, state="readonly")
    Txt3["values"] = ('Informatique', 'Electronique', 'Aeronotique', 'Grand Projet')
    Txt3.place(relx=0.3, rely=0.35)

    Lab4 = Label(mod, text="Note")
    Lab4.place(relx=0.1, rely=0.45)
    Txt4 = Entry(mod)
    Txt4.place(relx=0.3, rely=0.45)

    Btn1 = Button(mod, text="Confirmer", bg='#FF01E3', command=lambda: [
        note_verif_modif(Txt1, Txt2, Txt3, Txt4), tab_update(), mod.destroy()])
    Btn1.place(relx=0.25, rely=0.85, relwidth=0.2, relheight=0.075)

    Btn2 = Button(mod, text="Annuler", bg='#FF01E3', command=mod.destroy)
    Btn2.place(relx=0.55, rely=0.85, relwidth=0.2, relheight=0.075)


def Note_Supprimer():
    suppr = Toplevel(bg='#5D430D')
    suppr.geometry("720x480")
    suppr.title("Supprimer une note")

    Lab = Label(suppr, text="Saisissez pour supprimer une note", font=100)
    Lab.pack()

    Lab1 = Label(suppr, text="ID Etudiant")
    Lab1.place(relx=0.1, rely=0.15)
    Txt1 = Entry(suppr)
    Txt1.place(relx=0.3, rely=0.15)

    Lab2 = Label(suppr, text="Annee scolaire")
    Lab2.place(relx=0.1, rely=0.25)
    Txt2 = Entry(suppr)
    Txt2.place(relx=0.3, rely=0.25)

    Lab3 = Label(suppr, text="Matiere")
    Lab3.place(relx=0.1, rely=0.35)
    Txt3 = ttk.Combobox(suppr, state="readonly")
    Txt3["values"] = ('Informatique', 'Electronique', 'Aeronotique', 'Grand Projet')
    Txt3.place(relx=0.3, rely=0.35)

    Btn1 = Button(suppr, text="Confirmer", bg='#89713E', command=lambda: [
        note_verif_suppr(Txt1, Txt2, Txt3), tab_update(), suppr.destroy()])
    Btn1.place(relx=0.25, rely=0.85, relwidth=0.2, relheight=0.075)

    Btn2 = Button(suppr, text="Annuler", bg='#89713E', command=suppr.destroy)
    Btn2.place(relx=0.55, rely=0.85, relwidth=0.2, relheight=0.075)


def Evaluer():
    eval = Toplevel(bg='#51EBD6')
    eval.geometry("720x480")
    eval.title("Evaluer un etudiant")

    Lab = Label(eval, text="Gestionnaire des notes de l'etudiant", font=100)
    Lab.pack()

    Btn_n = Button(eval, text="Ajouter note", bg='#9AD7CF', command=Note_Ajouter)
    Btn_n.place(relx=0.375, rely=0.1, relwidth=0.25, relheight=0.15)

    Btn_m = Button(eval, text="Modifier note", bg='#9AD7CF', command=Note_Modifier)
    Btn_m.place(relx=0.375, rely=0.3, relwidth=0.25, relheight=0.15)

    Btn_d = Button(eval, text="Supprimer note", bg='#9AD7CF', command=Note_Supprimer)
    Btn_d.place(relx=0.375, rely=0.5, relwidth=0.25, relheight=0.15)

    Btn_r = Button(eval, text="Retour gestion scolaire", bg='#9AD7CF', command=eval.destroy)
    Btn_r.place(relx=0.375, rely=0.7, relwidth=0.25, relheight=0.15)


fenetre = Tk()
fenetre.title("Gestion scolaire")
fenetre.geometry("1440x720")
fenetre.configure(bg='#2c75ff')
l = LabelFrame(fenetre, text="Etudiant", bg='#2c75ff', labelanchor="n")
lbl1 = Label(l, text="Prenom")
lbl1.grid(row=0, column=0, padx=25)
txt1 = Entry(l)
txt1.grid(row=0, column=1, pady=10, padx=15)

lbl2 = Label(l, text="Nom")
lbl2.grid(row=1, column=0)
txt2 = Entry(l)
txt2.grid(row=1, column=1, pady=10)

var_genre = StringVar()
lbl3 = Label(l, text="Genre")
lbl3.grid(row=2, column=0)
radio = Radiobutton(l, text="F", value="F", variable=var_genre)
radio.grid(row=2, column=1)
radio1 = Radiobutton(l, text="M", value="M", variable=var_genre)
radio1.grid(row=2, column=2, pady=10)
radio.deselect()
radio1.deselect()

lbl4 = Label(l, text="Email")
lbl4.grid(row=3, column=0)
txt4 = Entry(l)
txt4.grid(row=3, column=1, pady=10)

lbl5 = Label(l, text="Groupe")
lbl5.grid(row=4, column=0)
combo = ttk.Combobox(l, state="readonly")
combo.grid(row=4, column=1, pady=10)
combo['values'] = ('2PD2', 'ANG1', 'ANG2')

btn = Button(l, text="Ajouter", bg='#B0C4DE', command=lambda: [
    etudiant_verif_ajout(txt1, txt2, var_genre, txt4, combo), tab_update()])
btn.grid(row=5, column=0, pady=20, padx=10)

btn1 = Button(l, text="Modifier", bg='#B0C4DE', command=lambda: Etudiant_Modifier(txt1, txt2, var_genre, txt4))
btn1.grid(row=5, column=2, padx=10)

l.pack(side="left", fill="y")

Title = Label(fenetre, text="Gestion de scolarite", font=100)
Title.pack()

TableMargin = Frame(fenetre, width=100)
TableMargin.pack()
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=(
    "ID", "Genre", "Nom", "Prenom", "Email", "Informatique", "Aeronautique", "Electronique", "Grand Projet"
    ), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading("ID", text="ID", anchor=W)
tree.heading("Genre", text="Genre", anchor=W)
tree.heading("Nom", text="Nom", anchor=W)
tree.heading("Prenom", text="Prenom", anchor=W)
tree.heading("Email", text="Email", anchor=W)
tree.heading("Informatique", text="Informatique", anchor=W)
tree.heading("Aeronautique", text="Aeronautique", anchor=W)
tree.heading("Electronique", text="Electronique", anchor=W)
tree.heading("Grand Projet", text="Grand Projet", anchor=W)
tree.column("#0", stretch=NO, minwidth=0, width=1)
tree.column("#1", stretch=NO, minwidth=0, width=50)
tree.column("#2", stretch=NO, minwidth=0, width=75)
tree.column("#3", stretch=NO, minwidth=0, width=175)
tree.column("#4", stretch=NO, minwidth=0, width=176)
tree.column("#5", stretch=NO, minwidth=0, width=250)
tree.column("#6", stretch=NO, minwidth=0, width=200)
tree.column("#7", stretch=NO, minwidth=0, width=200)
tree.column("#8", stretch=NO, minwidth=0, width=200)
tree.pack()


def tree_merge():
    data = ouverture_fichier_csv("etudiants.csv")
    data_notes = ouverture_fichier_csv("notes.csv")

    liste = [["" for i in range(4)] for j in range(1, len(data))]

    for n in range(1, len(data)):
        liste[n - 1].insert(0, data[n][0])
        liste[n - 1].insert(1, data[n][1])
        liste[n - 1].insert(2, data[n][2])
        liste[n - 1].insert(3, data[n][3])
        liste[n - 1].insert(4, data[n][4])

    for k in range(1, len(data)):
        id_e = k
        for m in range(1, len(data_notes)):
            if str(data_notes[m][3]) == 'Informatique':
                if int(data_notes[m][2]) == int(id_e):
                    liste[id_e - 1].pop(5)
                    liste[id_e - 1].insert(5, data_notes[m][4])
            if str(data_notes[m][3]) == 'Aeronotique':
                if int(data_notes[m][2]) == int(id_e):
                    liste[id_e - 1].pop(6)
                    liste[id_e - 1].insert(6, data_notes[m][4])
            if str(data_notes[m][3]) == 'Electronique':
                if int(data_notes[m][2]) == int(id_e):
                    liste[id_e - 1].pop(7)
                    liste[id_e - 1].insert(7, data_notes[m][4])
            if str(data_notes[m][3]) == 'Grand Projet':
                if int(data_notes[m][2]) == int(id_e):
                    liste[id_e - 1].pop(8)
                    liste[id_e - 1].insert(8, data_notes[m][4])

    for i in range(1, len(liste)+1):
        ID = liste[-i][0]
        GENRE = liste[-i][1]
        NOM = liste[-i][2]
        PRENOM = liste[-i][3]
        EMAIL = liste[-i][4]
        INFORMATIQUE = liste[-i][5]
        AERONAUTIQUE = liste[-i][6]
        ELECTRONIQUE = liste[-i][7]
        GRAND_PROJET = liste[-i][8]
        tree.insert("", 0, values=(ID, GENRE, NOM, PRENOM, EMAIL, INFORMATIQUE, AERONAUTIQUE,
                                   ELECTRONIQUE, GRAND_PROJET))

    liste.clear()


tree_merge()

df = Frame(fenetre)
df.pack()

btn2 = Button(l, text="Supprimer", bg='#B0C4DE', command=Etudiant_Supprimer)
btn2.grid(row=5, column=1)

btn3 = Button(l, text="Evaluer", bg='#B0C4DE', command=Evaluer)
btn3.grid(row=6, column=1)

def TextContent(id):
    data = ouverture_fichier_csv("etudiants.csv")
    data_notes = ouverture_fichier_csv("notes.csv")
    L = []
    for i in range(1, len(data)):
        if data[i][0] == str(id):
            id_t = str("Identifiant" + ": " + data[i][0])
            L.append(id_t)
            gender = str("Genre" + ": " + data[i][1])
            L.append(gender)
            name = str("Nom" + ": " + data[i][2])
            L.append(name)
            surname = str("Prenom" + ": " + data[i][3])
            L.append(surname)
            e_mail = str("Adresse mail" + ": " + data[i][4])
            L.append(e_mail)
            group = str("Groupe" + ": " + data[i][5])
            L.append(group)
    for j in range(1, len(data_notes)):
        if data_notes[j][2] == str(id):
            noted = str(data_notes[j][-2] + ": " + data_notes[j][-1] + "/20")
            L.append(noted)
    return L

def TextConvert(nom, prenom):
    data = ouverture_fichier_csv("etudiants.csv")
    filename = str(nom) + "_" + str(prenom) + ".txt"
    for i in range(1, len(data)):
        if data[i][3] == str(prenom) and data[i][2] == str(nom):
            id_e = int(data[i][0])
            with open(filename, 'w') as f:
                lines = TextContent(id_e)
                for z in range(len(lines)):
                    f.write(lines[z])
                    f.write("\n")
            return
    messagebox.showerror("Erreur", "Les informations saisies sont incorrectes")
    return

def Report():
    rapport = Toplevel()
    rapport.title('Telecharger le bulletin')
    rapport.geometry('720x480')

    titre = Label(rapport, text="Telecharger le bulletin de l'etudiant")
    titre.place(relx=0.4, rely=0.005)

    surname = Label(rapport, text="Nom")
    surname.place(relx=0.1, rely=0.1)
    name = Label(rapport, text="Prenom")
    name.place(relx=0.1, rely=0.2)

    entry1 = Entry(rapport)
    entry1.place(relx=0.25, rely=0.1)
    entry2 = Entry(rapport)
    entry2.place(relx=0.25, rely=0.2)

    bouton = Button(rapport, text="Confirmer", command=lambda: [
        TextConvert(entry1.get(), entry2.get()), rapport.destroy()])
    bouton.place(relx=0.8, rely=0.45)


btn4 = Button(l, text="Rapport", command=Report)
btn4.grid(row=6, column=0)

fenetre.mainloop()
