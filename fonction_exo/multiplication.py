def afficher_table_multiplication(n):
    cpt = 0
    while(cpt == 0):
        min = input("Commencer par : ")
        max = input("Finir par : ")
        min_int = int(min)
        max_int = int(max)
        cpt += 1
        if(min_int > max_int):
            cpt = 0
            print("La valeur min est supérieure à la valeur max, réessaye !")


    for i in range(min_int, max_int+1):
        print(i," * ", n," = ",i*n)

afficher_table_multiplication(10)
