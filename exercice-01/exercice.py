produit="clavier"

prix_ht= 19.90

quantité= 3

taux_tva= 0.20

total_ht= prix_ht * quantité
print("total_ht", total_ht)

total_ttc= total_ht * (1 + taux_tva)
print("total_ttc", total_ttc)

f"le total arrondi à 2 décimales est : {round(total_ttc, 2)}"
print(f"le total arrondi à 2 décimales est : {round(total_ttc, 2)}")

prix_texte= "19.90"


