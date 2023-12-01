from Partie_de_loic import *  # ajout du travail de Matthieu et Loic
print_president()  # afficher la liste des présidents
dico_TF = TF("cleaned")
dico_IDF = IDF("cleaned")
dico_TF_IDF = TF_IDF("cleaned")


cleaner()

x = 0

while x != 7:
    x = int(input("Si vous voulez afficher la liste des mots les moins importants dans le corpus de documents entrez 1. \n "
              "Si vous voulez afficher le(s) mot(s) ayant le score TD-IDF le plus élevé entrez 2. \n "
              "Si vous voulez indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac entrez 3. \n "
              "Si vouq voulez indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois entrez 4. \n "
              "Si vous voulez indiquer le premier président à parler du climat et/ou de l’écologie entrez 5. \n "
              "Hormis les mots dits « non importants », Si vous voulez le(s) mot(s) que tous les présidents ont évoqués entrez 6. \n "
              "Si vous n'avez plus de demandes entrez 7."))

    if x == 1:
        list_mots_faibles=[]
        for key in dico_TF_IDF.keys():
            list_ref = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            if dico_TF_IDF[key]==list_ref:
                list_mots_faibles.append(key)
        print(list_mots_faibles)

    if x ==2:
        list_mots_forts=[]
        max=0
        for key in dico_TF_IDF.keys():
            list_test=dico_TF_IDF[key]
            for i in range(len(list_test)):
                if list_test[i]>=max:
                    max=list_test[i]
                    list_mots_forts.append(key)
                    list_mots_fort=[]
                else:
                    max=max
        print(list_mots_forts)

    if x == 3:
        list_mots_occurence = []
        max2 = 0
        for key in dico_TF.keys():
            list_test2 = dico_TF[key]
            for i in range(2):
                if list_test2[i] >= max2:
                    max = list_test2[i]
                    list_mots_occurence.append(key)
                    list_mots_occurence = []
                else:
                    max2 = max2
        print(list_mots_occurence)
