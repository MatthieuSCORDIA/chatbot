from Partie_de_loic import *  # ajout du travail de Matthieu et Loic
print_president()  # afficher la liste des présidents
print_list(TF_IDF())
dico_TF = TF("cleaned")
dico_IDF = IDF("cleaned")
dico_TF_IDF = TF_IDF("cleaned")