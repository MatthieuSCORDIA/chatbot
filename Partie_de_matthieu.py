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
        elif files_names_president[boucle1_president] == "Hollande" or files_names_president[boucle1_president] == "Mitterrand":
            files_names_president[boucle1_president] = "François " + files_names_president[boucle1_president]
        elif files_names_president[boucle1_president] == "Macron":
            files_names_president[boucle1_president] = "Emmanuel " + files_names_president[boucle1_president]
        elif files_names_president[boucle1_president] == "Sarkozy":
            files_names_president[boucle1_president] = "Nicolas " + files_names_president[boucle1_president]
    print_list(files_names_president)
