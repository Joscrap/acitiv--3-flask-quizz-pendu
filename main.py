from flask import Flask, render_template, session, redirect, request
import os
import random
from pendu import Pendu

# Création de l'application
app = Flask("Jeu du pandu")
#création d"une clée secrete
app.secret_key = os.urandom(24)

# route de l'accueil
@app.route('/')
def index():
    liste_de_mot = ["ordinateur", "valorant", "manger", "micro", "téléphone", "liste", "ordinateur", "classe", "papier", "arbre"]
    mot_a_deviner = random.choice(liste_de_mot)
    vies = 6
    session["etat_du_jeu"] = Pendu.initialisation(mot_a_deviner , vies)

    return redirect("/jeu")

#affiche le jeu
@app.route('/jeu')
def jeu():
    return render_template("index.html", etat_du_jeu = session["etat_du_jeu"])

@app.route("/deviner", methods=["POST"])
def deviner():
    entree = request.form["entree"]
    session["etat_du_jeu"] = Pendu.deviner(session["etat_du_jeu"], entree)
    return redirect("/jeu")

# Exécution du code
app.run(host='0.0.0.0', port=81)