from Partie_de_matthieu import *  # ajout du travail de Matthieu


def cleaner():
    directory = "speeches-20231119"  # séléction du dossier
    files_names = list_of_files(directory, "txt")  # récupération des noms de fichiers

    for fichier in files_names:
        with open(directory+"/"+fichier, "r", encoding="utf-8") as fichier_ouvert, open("cleaned/"+fichier, "w", encoding="utf-8") as fichier_ouvert2:
            textenonclean = fichier_ouvert.readlines()
            for ligne_parcouru in range(len(textenonclean)):
                textenonclean[ligne_parcouru] = textenonclean[ligne_parcouru].replace("\n", " ")
                for caractere_ligne in range(len(textenonclean[ligne_parcouru])):
                    if 65 <= ord(textenonclean[ligne_parcouru][caractere_ligne]) <= 90 :
                        textenonclean[ligne_parcouru]=textenonclean[ligne_parcouru][:caractere_ligne]+chr(ord(textenonclean[ligne_parcouru][caractere_ligne])+32)+textenonclean[ligne_parcouru][caractere_ligne+1:]

                    elif 0<=ord(textenonclean[ligne_parcouru][caractere_ligne])<=64:
                        textenonclean[ligne_parcouru]=textenonclean[ligne_parcouru][:caractere_ligne]+" "+textenonclean[ligne_parcouru][caractere_ligne+1:]

                    elif 91<=ord(textenonclean[ligne_parcouru][caractere_ligne])<=96 :
                        textenonclean[ligne_parcouru]=textenonclean[ligne_parcouru][:caractere_ligne]+" "+textenonclean[ligne_parcouru][caractere_ligne+1:]

                    elif 123<=ord(textenonclean[ligne_parcouru][caractere_ligne])<=126:
                        textenonclean[ligne_parcouru]=textenonclean[ligne_parcouru][:caractere_ligne]+" "+textenonclean[ligne_parcouru][caractere_ligne+1:]
            for ligne_parcouru in textenonclean:
                fichier_ouvert2.write(ligne_parcouru)



