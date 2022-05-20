# LES COLLECTIONS : LISTES / TUPLES
# Append / Extend / += / Insert



def element_dans_liste(e, l):
    e = e.lower()
    l = [i.lower() for i in l]
    if e in l:
        return True
    else:
        return False
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

if element_dans_liste("JEAn", noms):
    print("Jean est là")
else:
    print("Jean n'est pas là")