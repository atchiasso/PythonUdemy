def questionnaire(question):
    global score
    print("QUESTION")
    print(" " + question[0])
    for choix in question[1]:
        print("  " + choix)
    reponse = input("Votre réponse : ")
    if reponse.lower() == question[2].lower():
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")
    print()


# questionnaire("Quelle est la capitale de la France", "Marseille", "Nice", "Paris", "Nantes", "c")

'''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"
'''

score = 0
question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
question2 = ("Quelle est la capitale de la France ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")
questionnaire(question1)
questionnaire(question2)
print("Score final : ", score)