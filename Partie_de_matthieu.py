import os, math

directory = "speeches-20231119"  # séléction du dossier


def print_list(lists_printer):
    for list_printer in lists_printer:
        print(list_printer)


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def print_president():
    files_names_president = list_of_files(directory, "txt")
    for boucle1_president in range(len(files_names_president)):
        files_names_president[boucle1_president] = files_names_president[boucle1_president].replace("Nomination_", "")
        files_names_president[boucle1_president] = files_names_president[boucle1_president].replace(".txt", "")
        for boucle2_president in range(10):
            files_names_president[boucle1_president] = files_names_president[boucle1_president].replace(
                str(boucle2_president), "")
    boucle1_president = 0
    while boucle1_president < len(files_names_president):
        boucle2_president = 0
        while boucle2_president < len(files_names_president):
            if boucle1_president != boucle2_president and files_names_president[boucle1_president] == \
                    files_names_president[boucle2_president]:
                del files_names_president[boucle2_president]
            boucle2_president += 1
        boucle1_president += 1
    for boucle1_president in range(len(files_names_president)):
        if files_names_president[boucle1_president] == "Chirac":
            files_names_president[boucle1_president] = "Jaques " + files_names_president[boucle1_president]
        elif files_names_president[boucle1_president] == "Giscard dEstaing":
            files_names_president[boucle1_president] = "Valery " + files_names_president[boucle1_president]
        elif files_names_president[boucle1_president] == "Hollande" or files_names_president[
            boucle1_president] == "Mitterrand":
            files_names_president[boucle1_president] = "François " + files_names_president[boucle1_president]
        elif files_names_president[boucle1_president] == "Macron":
            files_names_president[boucle1_president] = "Emmanuel " + files_names_president[boucle1_president]
        elif files_names_president[boucle1_president] == "Sarkozy":
            files_names_president[boucle1_president] = "Nicolas " + files_names_president[boucle1_president]
    print_list(files_names_president)
    return files_names_president


def TF(directory):
    dico_TF = {}  # initialisation de la matrice TF
    files_names_clean = list_of_files(directory, "txt")  # recupération des noms des fichiers dans le dossier clean
    for nom_fichier_parcouru in range(len(files_names_clean)):  # parcour chaque fichier 1 à 1
        with open("cleaned/" + files_names_clean[nom_fichier_parcouru], "r", encoding="utf-8") as fichier_parcouru:
            texte = fichier_parcouru.readline()  # recupération du texte du fichier
            mot_a_tester = ""
            for caractere_fichier_parcouru in texte:  # parcourt chaque caractère de la ligne
                if caractere_fichier_parcouru != " ":  # si on a un caractère on le rajoute aux mots
                    mot_a_tester += caractere_fichier_parcouru
                elif mot_a_tester != "":  # sinon (c'est la fin du mot) on vérifie qu'on a bien un mot
                    if not (mot_a_tester in dico_TF):
                        dico_TF[mot_a_tester] = [0.0] * (len(files_names_clean))
                    valeur_temporaire = dico_TF[mot_a_tester]
                    valeur_temporaire[nom_fichier_parcouru] += 1.0  # ajoute une ocurence à la bonne case
                    dico_TF[mot_a_tester] = valeur_temporaire
                    mot_a_tester = ""  # réinitialise le mot
    return dico_TF


def IDF(directory):
    dico_TF = TF(directory)
    dico_IDF = {}
    for nom_ligne_matrice_parcouru in dico_TF.keys():
        idf_ligne = 0.0
        ligne_matrice_parcouru = dico_TF[nom_ligne_matrice_parcouru]
        for case_matrice_parcouru in range(len(ligne_matrice_parcouru)):
            if ligne_matrice_parcouru[case_matrice_parcouru] != 0:
                idf_ligne += 1.0
        dico_IDF[nom_ligne_matrice_parcouru] = math.log(len(ligne_matrice_parcouru) / idf_ligne)
    return dico_IDF


def TF_IDF(directory):
    dico_TF = TF(directory)
    dico_IDF = IDF(directory)
    dico_TF_IDF = {}
    for nom_ligne_matrice_parcouru in dico_TF.keys():
        idf_ligne = dico_IDF[nom_ligne_matrice_parcouru]
        ligne_matrice_parcouru = dico_TF[nom_ligne_matrice_parcouru]
        for case_matrice_parcouru in range(len(ligne_matrice_parcouru)):
            ligne_matrice_parcouru[case_matrice_parcouru] = ligne_matrice_parcouru[case_matrice_parcouru] * idf_ligne
        dico_TF_IDF[nom_ligne_matrice_parcouru] = ligne_matrice_parcouru
    return dico_TF_IDF


def clean_rep(reponse):
    for caractere_clean in range(len(reponse)):
        if 64 < ord(reponse[caractere_clean]) < 91:
            reponse = reponse[:caractere_clean] + chr(ord(reponse[caractere_clean]) + 32) + reponse[
                                                                                            caractere_clean + 1:]
        elif not (96 < ord(reponse[caractere_clean]) < 123):
            reponse = reponse[:caractere_clean] + " " + reponse[caractere_clean + 1:]

    caractere_clean = 0
    while caractere_clean < len(reponse) - 1:
        if reponse[caractere_clean] == reponse[caractere_clean + 1] and reponse[caractere_clean] == " ":
            reponse = reponse[:caractere_clean] + reponse[caractere_clean + 1:]
        else:
            caractere_clean += 1
    return reponse


def calcule_similarité(dico_TF_IDF_rep,
                       dico_TF_IDF, list_nom_doc=None):
    if list_nom_doc is None:
        list_nom_doc = list_of_files("speeches-20231119", "txt")
    norme_vec_rep = 0.0  # calcule de la norme du vecteur réponse:
    for mot_select in dico_TF_IDF_rep.values():
        norme_vec_rep += mot_select ** 2
    norme_vec_rep = math.sqrt(norme_vec_rep)
    similarité = [0.0] * 8
    for doc_parcouru in range(8):
        norme_vec_doc = 0.0
        for mot_select in dico_TF_IDF.values():  # calcule de la norme du vecteur du document
            norme_vec_doc += mot_select[doc_parcouru] ** 2
        norme_vec_doc = math.sqrt(norme_vec_rep)
        for mot_select in dico_TF_IDF_rep.keys():  # calcule produit scalaire
            if mot_select in dico_TF_IDF.keys():
                similarité[doc_parcouru] += dico_TF_IDF_rep[mot_select]*dico_TF_IDF[mot_select][doc_parcouru]
        similarité[doc_parcouru] = similarité[doc_parcouru]/(norme_vec_rep*norme_vec_doc) #calcule similarité
    doc_sim = 0 # recherche du nom du doc similaire
    for doc_parcouru in range(1, 8):
        if similarité[doc_sim] > similarité[doc_parcouru]:
            doc_sim = doc_parcouru
    doc_sim = list_nom_doc[doc_sim]
    return doc_sim