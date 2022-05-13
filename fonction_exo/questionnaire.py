
'''
REFLEXION :
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"
'''

def questionnaire(question):
    rep = 1
    print("QUESTION")
    print(" " + question[0])
    for choix in question[1]:
        print(f" {rep} - " + choix)
        rep += 1
    resultat_reponse_correcte = False
    reponse_int = demander_reponse_numerique_utilisateur(1, len(question[1]))
    if question[1][reponse_int-1].lower() == question[2].lower():
        print("Bonne réponse")
        resultat_reponse_correcte = True
    else:
        print("Mauvaise réponse")
    print()
    return resultat_reponse_correcte

def demander_reponse_numerique_utilisateur(min, max):
    reponse = input(f"Votre réponse (entre {min} et {max}) : ")
    try:
        reponse_int = int(reponse)
        if min <= reponse_int <= max:
            return reponse_int
        print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
    except:
        print("ERREUR : Veuillez rentre uniquement des chiffres")
    return demander_reponse_numerique_utilisateur(min, max)

def lancer_questionnaire(qcm):
    score = 0
    for question in qcm:
        if questionnaire(question):
            score += 1
    print("Score final : " + str(score) + "/" + str(len(qcm)))

question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
question2 = ("Quelle est la capitale de la France ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")
question3 = ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")

qcm = (question1, question2, question3)
lancer_questionnaire(qcm)