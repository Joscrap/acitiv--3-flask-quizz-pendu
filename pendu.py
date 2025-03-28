from unidecode import unidecode


class Pendu :
    vies = 0
    mot_a_deviner = ""
    mot_a_afficher =""
    lettres_proposees = []


    def initialisation(mot_a_deviner , vies):
        mot_a_deviner = unidecode(mot_a_deviner).upper()
        print("le mot pour cette partie est :", mot_a_deviner)

        data_etat_du_jeu = {
            "vies" : vies,
            "mot_a_deviner" : mot_a_deviner,
            "mot_a_afficher" : "-" * len(mot_a_deviner),
            "defaite" : False,
            "victoire" : False,
            "entree" : "",
            "lettres_proposees" : []
        }

        return data_etat_du_jeu


    def deviner(etat_du_jeu, entree):
        global vies
        global mot_a_deviner
        global mot_a_afficher
        global lettres_proposees

        vies = etat_du_jeu["vies"]
        mot_a_deviner = etat_du_jeu["mot_a_deviner"]
        mot_a_afficher = etat_du_jeu["mot_a_afficher"]
        lettres_proposees = etat_du_jeu["lettres_proposees"]

        data_retour = {
            "defaite" : False,
            "victoire" : False,
            "derniere_entree" : ""
        }

        entree = unidecode(entree)

        if len(entree) == 0 :
            message = "Propose quelque chose !"
        elif len(entree) == 1 :
            message = Pendu.deviner_lettre(entree)
        else:
            message = Pendu.deviner_mot(entree)

        data_retour["vies"] = vies
        data_retour["mot_a_deviner"] = mot_a_deviner
        data_retour["mot_a_afficher"] = mot_a_afficher
        data_retour["lettres_proposees"] = lettres_proposees
        data_retour["message"] = message

        data_retour["victoire"] = not "-" in mot_a_afficher
        if vies == 0:
            data_retour["defaite"] = True
            
        return data_retour

    
    def deviner_lettre(entree):
        global lettres_proposees
        global mot_a_afficher
        global vies

        if entree in lettres_proposees:
            return "Tu a déjà deviner cette lettre !!!"
        else:
            lettres_proposees.append(entree)
            if entree in mot_a_deviner:
                Pendu.actualisation_mot_a_afficher(entree)
                return "Bonne piche, le mot contient cette lettre !!!"
            else:
                vies -= 1
                return "Oups, cette lettre n'est pas dans le mot !!!"


    def deviner_mot(mot):
        global mot_a_deviner
        global vies
        global mot_a_afficher

        if mot == mot_a_deviner:
            mot_a_afficher = mot
            return "Bravo, tu a trouver le mot !"
        else :
            vies -= 1
            return "Dommage, tu n'a pas trouver le bon mot !"


    def actualisation_mot_a_afficher(lettre):
        global mot_a_deviner
        global mot_a_afficher

        for i in range(len(mot_a_deviner)):
            if lettre == mot_a_deviner[i]:
                mot_tmp = list(mot_a_afficher)
                mot_tmp [i] = lettre
                mot_a_afficher = "".join(mot_tmp)




    





