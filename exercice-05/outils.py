def convertir_note(texte):
    try:
        return float(texte.replace(",", "."))
    except ValueError:
        return None

def moyenne(valeurs):
    return sum(valeurs) / len(valeurs) 

def mention(note):
    if note >= 15:
        return "Très bien"
    elif note >= 10:
        return "Assez bien"
    elif note < 10:
        return "Tu cherches quoi ici"
    
