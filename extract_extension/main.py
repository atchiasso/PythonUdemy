import time
fichiers = ["notepad.exe", "mon_fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat"]

def extraire_extension(nom_fichier):
    nom_fichier_split = nom_fichier.split(".")
    if len(nom_fichier_split) > 1:
        return nom_fichier_split[-1]
    return None

def obtenir_definition_extension(extension, definitions):
    for d in definitions:
        if d[0].lower() == extension.lower():
            return d[1]
    return None

definition_extensions = (("exe", "Executable"),
                         ("doc", "Document Word"),
                         ("txt", "Document texte"),
                         ("jpeg", "Image JPEG"))

definition_extensions_dict = {"exe": "Executable",
                         "doc": "Document Word",
                         "txt": "Document texte",
                         "jpeg": "Image JPEG"}

for fichier in fichiers:
    ext = extraire_extension(fichier)
    if ext:
        # definition = obtenir_definition_extension(ext, definition_extensions)
        definition = definition_extensions_dict.get(ext.lower())
        if definition == None:
            definition = "Extension non connue"
    else:
        definition = "Aucune extension"
    print(fichier + " (" + definition + ")")