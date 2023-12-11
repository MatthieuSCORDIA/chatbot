from Partie_de_matthieu import *  # ajout du travail de Matthieu


def cleaner():
    directory = "speeches-20231119"  # séléction du dossier
    files_names = list_of_files(directory, "txt")  # récupération des noms de fichiers

    for fichier in files_names:
        with open(directory+"/"+fichier, "r") as fichier_ouvert, open("cleaned/"+fichier, "w") as fichier_ouvert2:
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


def TF_rep(reponse):
    dico_TF_rep= {} #initialisation du dictionnaire TF de la réponse
    mot_a_tester_2="" #init de la variable mot a tester 2 de la reponse
    for caractere_reponse in range(len(reponse)): #Parcourt de chaques caractères de la reponse
        if caractere_reponse != " ": #On prend que les mots
            mot_a_tester_2 += aractere_reponse #On attribu a mot a tester 2 le mot de la reponse
        elif mot_a_tester_2 != "" : #Si c'est la fin du mot faire :
            mot_a_tester_2 = mot_a_tester_2.replace("Ã©", "é") #on modifit les caractères qui n'ont pas été clean a 100%
            mot_a_tester_2 = mot_a_tester_2.replace("oÃ¹", "à") #on modifit les caractères qui n'ont pas été clean a 100%
            if not (mot_a_tester_2 in dico_TF_rep): #Si le mot n'est pas présent on lui donne pas de score
                dico_TF_rep[mot_a_tester_2] = [0.0] * (len(reponse))
            val_t = dico_TF_rep[mot_a_tester_2]
            val_t [caractere_reponse] += 1.0
            dico_TF[mot_a_tester_2] = val_t
            mot_a_tester_2 = ""
    return dico_TF_rep


