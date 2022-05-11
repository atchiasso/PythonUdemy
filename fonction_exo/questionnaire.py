def questionnaire(question, r1, r2, r3, r4, choix_bonne_reponse):
    global score
    print("QUESTION")
    print(" " + question)
    print("  (a)", r1)
    print("  (b)", r2)
    print("  (c)", r3)
    print("  (d)", r4)
    print()
    reponse = input("Votre réponse : ")
    if reponse == choix_bonne_reponse:
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")
    print()

score = 0
questionnaire("Quelle est la capitale de la France", "Marseille", "Nice", "Paris", "Nantes", "c")

print("Score final : ", score)