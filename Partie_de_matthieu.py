import os

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
        files_names_president[boucle1_president] = files_names_president[boucle1_president].replace("1", "")
        files_names_president[boucle1_president] = files_names_president[boucle1_president].replace("2", "")
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


def TF():
    matrice = []
    files_names_clean = list_of_files(directory, "txt")
    for nom_fichier_parcouru in range(len(files_names_clean)):
        with open(directory+"/" + files_names_clean[nom_fichier_parcouru], "r") as fichier_parcouru:
            texte = fichier_parcouru.readlines()
            for ligne_fichier_parcouru in texte:
                mot_a_tester = ""
                for caractere_fichier_parcouru in ligne_fichier_parcouru:
                    if caractere_fichier_parcouru != " ":
                        mot_a_tester += caractere_fichier_parcouru
                    elif mot_a_tester != "":
                        verif_present = False
                        selection_case = 0
                        while selection_case < len(matrice) and not verif_present:
                            if matrice[selection_case][0] == mot_a_tester:
                                verif_present=True
                            else:
                                selection_case+=1
                        if not verif_present:
                            matrice.append([0]*(len(files_names_clean)+1))
                            matrice[selection_case][0]=mot_a_tester
                        matrice[selection_case][nom_fichier_parcouru+1]+=1
                        mot_a_tester=""
    return matrice