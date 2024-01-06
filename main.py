from Partie_de_loic import *  # ajout du travail de Matthieu et Loic

files_names_president = print_president()  # afficher la liste des présidents
dico_TF = TF("cleaned")
dico_IDF = IDF("cleaned")
dico_TF_IDF = TF_IDF("cleaned")

print("")
print("Posez votre question :")
question2 = str(input())
print(reponse_2(question2))
cleaner()

x = 0

while x != 7:
    x = int(
        input("Si vous voulez afficher la liste des mots les moins importants dans le corpus de documents entrez 1. \n "
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
        print("Les mots les moins importants sont :", list_mots_faibles)

    if x ==2:
        list_mots_forts=[]
        max=0
        for key in dico_TF_IDF.keys():
            list_test=dico_TF_IDF[key]
            maxi=list_test[0]
            for i in range(1, len(list_test)):
                if maxi<list_test[i]:
                    maxi=list_test[i]
            if maxi==max:
                list_mots_forts.append(key)
            elif maxi>max:
                list_mots_forts = []
                max=maxi
                list_mots_forts.append(key)

        print("Les mots les plus forts sont :", list_mots_forts)

    if x == 3:
        list_mots_occurence = []
        max2 = 0
        for key in dico_TF.keys():
            list_test2 = dico_TF[key]
            maxi = list_test2[0]
            if maxi < list_test2[1]:
                maxi = list_test2[1]
            if maxi == max2:
                list_mots_occurence.append(key)
            elif maxi > max2:
                list_mots_occurence = []
                max2 = maxi
                list_mots_occurence.append(key)

        print(list_mots_occurence)

    if x == 4:
        list_mot_nation = dico_TF["nation"]
        chronologie_president = [2, 5, 6, 0, 1, 7, 3, 5]
        i = 0
        president_patriot = None
        while president_patriot is None:
            if list_mot_nation[chronologie_president[i]] != 0:
                president_patriot = chronologie_president[i]
            else:
                i += 1
            nombre_nation=int(list_mot_nation[chronologie_president[i]])
        if president_patriot >= 6:
            president_patriot -= 1
        if president_patriot >= 1:
            president_patriot -= 1
        print("le premier président à parler de la Nation est ", files_names_president[president_patriot], "et il en parle", nombre_nation," fois.")

    if x == 5:
        list_mot_ecolo = dico_TF["écologique"]
        list_mot_climat = dico_TF["climat"]
        chronologie_president = [2, 5, 6, 0, 1, 7, 3, 5]
        i = 0
        president_écolo = None
        while president_écolo is None:
            if list_mot_ecolo[chronologie_president[i]] != 0 or list_mot_climat[chronologie_president[i]] != 0:
                president_écolo = chronologie_president[i]
            else:
                i += 1
        if president_écolo >= 6:
            president_écolo -= 1
        if president_écolo >= 1:
            president_écolo -= 1
        president_écolo=files_names_president[president_écolo]
        print("le premier président à parler du climat et/ou de l’écologie est ", president_écolo)
    if x==6:
        list_mots_simple = []
        for key in dico_TF_IDF.keys():
            list_ref2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            if dico_TF_IDF[key] != list_ref2:
                list_mots_simple.append(key)
        print("Les mots les mots, hormis ceux non importants, des présidents sont :", list_mots_simple)

