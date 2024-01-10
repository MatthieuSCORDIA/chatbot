from Partie_de_matthieu import *  # ajout du travail de Matthieu


def cleaner():
    directory = "speeches-20231119"  # séléction du dossier
    files_names = list_of_files(directory, "txt")  # récupération des noms de fichiers

    for fichier in files_names:
        with open(directory + "/" + fichier, "r", encoding="utf-8") as fichier_ouvert, open("cleaned/" + fichier, "w",
                                                                                            encoding="utf-8") as fichier_ouvert2:
            textenonclean = fichier_ouvert.readlines()
            for ligne_parcouru in range(len(textenonclean)):
                textenonclean[ligne_parcouru] = textenonclean[ligne_parcouru].replace("\n", " ")
                for caractere_ligne in range(len(textenonclean[ligne_parcouru])):
                    if 65 <= ord(textenonclean[ligne_parcouru][caractere_ligne]) <= 90:
                        textenonclean[ligne_parcouru] = textenonclean[ligne_parcouru][:caractere_ligne] + chr(
                            ord(textenonclean[ligne_parcouru][caractere_ligne]) + 32) + textenonclean[ligne_parcouru][
                                                                                        caractere_ligne + 1:]

                    elif 0 <= ord(textenonclean[ligne_parcouru][caractere_ligne]) <= 64:
                        textenonclean[ligne_parcouru] = textenonclean[ligne_parcouru][:caractere_ligne] + " " + \
                                                        textenonclean[ligne_parcouru][caractere_ligne + 1:]

                    elif 91 <= ord(textenonclean[ligne_parcouru][caractere_ligne]) <= 96:
                        textenonclean[ligne_parcouru] = textenonclean[ligne_parcouru][:caractere_ligne] + " " + \
                                                        textenonclean[ligne_parcouru][caractere_ligne + 1:]

                    elif 123 <= ord(textenonclean[ligne_parcouru][caractere_ligne]) <= 126:
                        textenonclean[ligne_parcouru] = textenonclean[ligne_parcouru][:caractere_ligne] + " " + \
                                                        textenonclean[ligne_parcouru][caractere_ligne + 1:]
            for ligne_parcouru in textenonclean:
                fichier_ouvert2.write(ligne_parcouru)


def TF_rep(reponse):
    dico_TF_rep = {}  # initialisation du dictionnaire TF de la réponse
    mot_a_tester_2 = ""  # init de la variable mot a tester 2 de la reponse
    for caractere_reponse in range(len(reponse)):  # Parcourt de chaques caractères de la reponse
        if reponse[caractere_reponse] != " ":  # On prend que les mots
            mot_a_tester_2 += reponse[caractere_reponse]  # On attribu a mot a tester 2 le mot de la reponse
        elif mot_a_tester_2 != "":  # Si c'est la fin du mot faire :
            if not (mot_a_tester_2 in dico_TF_rep):  # Si le mot n'est pas présent on lui donne pas de score
                dico_TF_rep[mot_a_tester_2] = 0.0
            dico_TF_rep[mot_a_tester_2] += 1.0
            mot_a_tester_2 = ""
    if mot_a_tester_2 != "":  # Si c'est la fin du mot faire :
        if not (mot_a_tester_2 in dico_TF_rep):  # Si le mot n'est pas présent on lui donne pas de score
            dico_TF_rep[mot_a_tester_2] = 0.0
        dico_TF_rep[mot_a_tester_2] += 1.0
    return dico_TF_rep

liste_mot_ban = ["comment","pourquoi","qui","qaund"]

def Idem(reponse):
    dico_TF_rep = TF_rep(reponse)
    dico_IDF = IDF("cleaned")
    for mot in dico_TF_rep.keys():
        if not (mot in dico_IDF.keys()) or (mot in liste_mot_ban) :
            dico_TF_rep[mot] = 0.0
        else:
            dico_TF_rep[mot] = dico_TF_rep[mot] * dico_IDF[mot]
    return dico_TF_rep


question_ref = {  # génération d'une liste pour incrémeneter le texte correspondant a la question
    "comment": "Après analyse, ",
    "pourquoi": "Car, ",
    "peux": "Oui, bien sûr! "
}

def reponse_2(question2, dico_TF_IDF_rep, doc_parcourir):
    mot_1 = question2.split()[0]  # Cette ligne divise la question2 en mots,sélectionne le premier mot.
    reponse2 = ""
    if mot_1 in question_ref.keys():
        reponse2 = question_ref[mot_1]  # Trouver la réponse correspondante au premier mot
    reponse2 = str(reponse2)
    reponse_generer = generation_reponse(dico_TF_IDF_rep, doc_parcourir)
    if reponse_generer is None:
        reponse_generer = "Malheureusement, nous n'avons pas trouvé de réponse à votre question"
    reponse2 += reponse_generer
    reponse2 = reponse2.capitalize() + "."  # Mettre une majuscule en début de phrase et un point à la fin
    return reponse2


def generation_reponse(dico_TF_IDF_rep, doc_parcourir):
    mot_important = max(dico_TF_IDF_rep, key=dico_TF_IDF_rep.get)  # creation variable mot important
    if not (doc_parcourir is None):
        with open(directory + "/" + doc_parcourir, "r", encoding="utf-8") as fichier_ouvert:  # ouvrir le dossier texte
            doc_lecture = fichier_ouvert.read()
            liste1 = doc_lecture.split('.')  # fonction split pour faire un liste avec chaques phrases en point
            liste_clone = []
            for y in range(len(liste1)):
                liste_clone.append(liste1[y])
                liste_clone[y] = clean_rep(liste_clone[y])
            for y in range(len(liste_clone)):
                if mot_important in liste_clone[y]:
                    return str(liste1[y])