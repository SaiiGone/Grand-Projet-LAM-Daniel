# -*- coding: utf-8 -*-
from lib_commun import ouverture_fichier_csv, ecriture_fichier_csv

def ajoutEtudiant(prenom,nom,genre,email,groupe) :
    """
    Cette fonction a pour objectif d'ajouter un etudiant
    IN : [prenom, nom, genre, email, groupe], nom_fichier
    OUT : retour nouvelle ligne + affectation ID
    """
    nv_data = []
    id_data = []
    data = ouverture_fichier_csv("etudiants.csv")
    id_etudiant = 1
    for j in range(1, len(data)):
        id_data.append(int(data[j][0]))
    for k in id_data:
        while id_etudiant == k:
                id_etudiant += 1
    for i in range(1, len(data)):
        if data[i][4] == email:
            print("Cet étudiant existe déjà")
            id_data.clear()
            return
    nv_data.insert(0, str(id_etudiant))
    nv_data.insert(1, str(genre))
    nv_data.insert(2, str(nom))
    nv_data.insert(3, str(prenom))
    nv_data.insert(4, str(email))
    nv_data.insert(5, str(groupe))
    data.insert(id_etudiant, nv_data)
    ecriture_fichier_csv(data, "etudiants.csv")
    nv_data.clear()
    id_data.clear()
    return
    
def modificationEtudiant(id_,prenom,nom,genre,email) :
    """
    Cette fonction a pour objectif de modifier les donnees etudiant
    IN : ID
    OUT : prenom, nom, genre, email, groupe
    """
    data = ouverture_fichier_csv("etudiants.csv")
    for i in range(1, len(data)):
        if data[i][0] == id_:
            del data[i][1:5]
            in_data = data[i]
            in_data.insert(1, genre)
            in_data.insert(2, nom)
            in_data.insert(3, prenom)
            in_data.insert(4, email)
            ecriture_fichier_csv(data, "etudiants.csv")
            return
    print("Cet étudiant n'existe pas")
    return
    
def suppressionEtudiant(id_) :
    """
    Cette fonction a pour objectif de supprimer l'etudiant (de la liste)
    IN : id_
    OUT : supprime ligne etudiant
    """
    data = ouverture_fichier_csv("etudiants.csv")
    for i in range(1, len(data)):
        if data[i][0] == id_:
            del data[i]
            ecriture_fichier_csv(data, "etudiants.csv")
            return
    print("Cet étudiant n'existe pas")
    return

def affichageEtudiant() :
    """
    Cette procédure a pour objectif d'afficher l'ensemble des informations administratives des etudiants.
    Soit : ID, prenom, nom, genre, email, groupe
    IN : aucun paramètre en entrée
    OUT : aucun retour
    """
    ##################################################
    #ouverture et recuperation du contenu du fichier
    ##################################################
    nomfichier = "etudiants.csv"
    data = ouverture_fichier_csv(nomfichier)



    print("***********************************************************************************************************")
    print("*                                          Gestion Scolaire                                               *")
    print("***********************************************************************************************************")
    print("*  ID   *   Genre      *     Prenom          *   Nom              * Email adresse          *   Groupe      ")
    print("***********************************************************************************************************")

    for i in range(1,len(data)) :
        print("* {:<8}  * {:<8}  * {:<15}  *  {:<15}  *  {:<25} * {:>5} *" . format(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))

    print("***********************************************************************************************************\n")