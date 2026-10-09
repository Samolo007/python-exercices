from outils import convertir_note, moyenne, mention

notes_brutes = ["12,5", "15", "abc", "9", "18,25"]

notes_ignorees = 0
notes_valides = []
for note in notes_brutes:
    note_convertie = convertir_note(note)
    if note_convertie is None:
        notes_ignorees += 1
    else:
        notes_valides.append(note_convertie)

print(f"Notes ignorées : {notes_ignorees}")

if notes_valides:
    moyenne_notes = moyenne(notes_valides)
    mention_obtenue = mention(moyenne_notes)
    print(f"Moyenne : {round(moyenne_notes, 2)}")
    print(f"Mention : {mention_obtenue}")
else:
    print("Aucune note valide : impossible de calculer la moyenne.")
