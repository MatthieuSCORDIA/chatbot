import os

directory = "speeches-20231119.zip"
files_names = list_of_files(directory, ".txt")
print_list(files_names)


def print_list(lists_printer):
    for list_printer in lists_printer:
        print(list_printer)


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
