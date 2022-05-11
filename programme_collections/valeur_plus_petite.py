nom_chauffeur = ["Patrick", "Paul", "Marc", "Jean", "Pierre", "Marie", "Maxime"]
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]

distance_min = distance_chauffeur_km[0]
index_min = 0
for distance in range (len(distance_chauffeur_km)):
    if distance_chauffeur_km[distance] < distance_min:
        distance_min = distance_chauffeur_km[distance]
        index_min = distance
print("Distance min :", distance_min)
print("Index :", index_min)
print("Chauffeur :", nom_chauffeur[index_min])