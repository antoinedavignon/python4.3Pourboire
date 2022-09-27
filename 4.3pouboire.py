# Auteur : Antoine

# CONSTANTES


# VARIABLES
prix_pourboire: float
prix_facture: float


# LOGIQUE
print("Quelle est le montant de votre facture?")
prix_facture = float(input("Montant de la facture:"))

if prix_facture < 0:
    print("Pas besoin de pourboire, il vous doit de l'argent!")
elif prix_facture < 10:
    print("Un pourboire de 1,50$ est recommandé.")
elif prix_facture < 100: