import os

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
    from main import directory
    files_names_president = list_of_files(directory,"txt")
    for boucle1_president in range(len(files_names_president)):
        files_names_president[boucle1_president]= files_names_president[boucle1_president].replace("Nomination_", "")
        files_names_president[boucle1_president] = files_names_president[boucle1_president].replace(".txt", "")
        files_names_president[boucle1_president] = files_names_president[boucle1_president].replace("1", "")
        files_names_president[boucle1_president] = files_names_president[boucle1_president].replace("2", "")
    print_list(files_names_president)