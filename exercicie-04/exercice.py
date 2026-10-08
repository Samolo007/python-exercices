ventes = [
    {"produits": "café", "prix": 2.5, "quantité": 120},
    {"produits": "thé", "prix": 2.0, "quantité": 80},
    {"produits": "jus", "prix": 3.5, "quantité": 45},
]

ca_par_produit = {vente["produits"]: vente["prix"] * vente["quantité"] for vente in ventes}
print("Chiffre d'affaires par produit :", ca_par_produit)

ca_total = sum(ca_par_produit.values())
print("Total :", ca_total)

maximum= max(ca_par_produit, key=ca_par_produit.get)
print("Meilleur produit :", maximum)