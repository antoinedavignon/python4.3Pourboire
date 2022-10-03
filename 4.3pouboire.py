# Auteur : Fait par Antoine
# Date de création : 27 septembre 2022

# Algorithme :
# Ce programme servira à déterminer s'il y a un pourboire à donner et
# quel serait le montant recommandé tout donnant le montant total de la facture.

import math

# VARIABLES
prix_pourboire: float  # valeur du pourboire recommandé
prix_facture: float  # prix de la facture demandé en input

# LOGIQUE
while True:
    try:
        # PMC : j'ai enlevé le print()
        prix_facture = float(input("Quel est le montant de la facture:"))
        if prix_facture < math.inf:
            break
    except ValueError:
        print("Pas de lettres dans le montant!")
        # PMC : pas besoin de quitter, juste à recommencer

if prix_facture <= 10:
    prix_pourboire = 1.50

elif prix_facture < 100:
    prix_pourboire = prix_facture * 0.15

elif prix_facture < 200 or prix_facture == 100:
    prix_pourboire = (prix_facture * 0.05) + 15

else:
    prix_pourboire = 0

if 200 > prix_facture > 0:
    print(f"Votre montant total de votre facture est de {(prix_facture + prix_pourboire) :.2f} $ \n"
          f"et la valeur du pourboire est de {prix_pourboire:.2f} $.")

if prix_facture >= 200:
    print("La valeur du pourboire est de 0$ car celui-ci est inclu.")
elif prix_facture < 0:
    print("Impossible, la facture ne peut pas être négative.")
