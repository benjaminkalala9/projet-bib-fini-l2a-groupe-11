from livre import ajouterLivre, afficher_livres, rechercherLivre , suprimer_ou_archiver
from utilisateur import mange_users
from emprunt import emprunter_livre
from retour import retourner_livre




def menu_principal():
    print("1. ajouter un livre")
    print("2. Rechercher un livre")
    print("3. suprimer un livre")
    print("4. Afficher le livre")
    print("5. Emprunter un livre")
    print("6. Retournez un livre")
    print("7. Ajouter un nouvel utilisateur:")
    print("8. Quiter \n")
    choix = int(input("selectionez une option : "))
    return choix

def main ():
    while True:
        choix = menu_principal()
        if choix == 1:
            ajouterLivre()
        elif choix == 2:
            rechercherLivre()
        elif choix == 3:
            suprimer_ou_archiver()
        elif choix == 4:
            afficher_livres()
        elif choix == 5:
            emprunter_livre()
        elif choix == 6:
            retourner_livre()
        elif choix == 7 :
            mange_users()
        elif choix == 8:
            break

if __name__== "__main__":
 main()