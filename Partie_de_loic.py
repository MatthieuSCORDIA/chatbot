from Partie_de_matthieu import *  # ajout du travail de Matthieu


def cleaner():
    directory = "speeches-20231119"  # séléction du dossier
    files_names = list_of_files(directory, "txt")  # récupération des noms de fichiers

    for fichier in files_names:
        with open(directory+"/"+fichier, "r") as fichier_ouvert:
            textenonclean = fichier_ouvert.readline()
            if fichier
            print(textenonclean)
