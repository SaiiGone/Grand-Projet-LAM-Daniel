# -*- coding: utf-8 -*-
from lib_commun import ouverture_fichier_csv, ecriture_fichier_csv

def ajoutNote(id_,annee,matiere,note) :
    """
    Cette fonction a pour objectif d'ajouter une nouvelle note
    IN : ID, Annee, Matiere, Note
    OUT : ajout de ligne note
    """
    data = ouverture_fichier_csv("notes.csv")
    nv_data = []
    idn_data =[]
    id_n = 1
    for i in range(1, len(data)):
        idn_data.append(int(data[i][0]))
    for j in idn_data:
        while id_n == j:
            id_n += 1
    for k in range(1, len(data)):
        if data[i][2] == id_ and data[i][3] == matiere:
            print("L'etudiant a deja ete evalue sur cette matiere")
            idn_data.clear()
            return
    nv_data.insert(0, str(id_n))
    nv_data.insert(1, str(annee))
    nv_data.insert(2, str(id_))
    nv_data.insert(3, str(matiere))
    nv_data.insert(4, str(note))
    data.insert(id_n + 1, nv_data)
    ecriture_fichier_csv(data, "notes.csv")
    nv_data.clear()
    idn_data.clear()
    return
    
def modificationNote(id_,annee,matiere,note) :
    """
    Cette fonction a pour objectif de modifier une note deja existante
    IN : ID, Annee, Matiere, Note
    OUT : change la note
    """
    data = ouverture_fichier_csv("notes.csv")
    for i in range(1, len(data)):
        if data[i][1] == annee and data[i][2] == id_ and data[i][3] == matiere :
            del data[i][4]
            in_data = data[i]
            in_data.insert(4, note)
            ecriture_fichier_csv(data, "notes.csv")
            return
    print("Cette note n'existe pas")
    return
    
def suppressionNote(id_,annee,matiere) :
    """
    Cette fonction a pour objectif de supprimer une note
    IN : ID, Annee, Matiere
    OUT : retire une ligne de note
    """
    data = ouverture_fichier_csv("notes.csv")
    for i in range(1, len(data)):
        if data[i][1] == annee and data[i][2] == id_ and data[i][3] == matiere :
            del data[i]
            ecriture_fichier_csv(data, "notes.csv")
            return
    print("Cette note n'existe pas")
    return
