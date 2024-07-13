import json

def validerTitre(titre):
    if not titre.startswith(("#", "@", "$", "%", "&", "_ ")) or len(titre) > 2 and len(titre) < 30:
        return True
    else:
        return False

def validerAuteur(auteur):
    if len(auteur) > 3 and len(auteur) < 20:
        return True
    else:
        return False

def validerGenre(genre):
    return True

def ajouterLivre():
    try:
        with open("livres.json", "r") as f:
            livres = json.load(f)
    except FileNotFoundError:
        livres = []

    if len(livres) == 0:
        idLivre = 1
    else:
        idLivre = livres[-1]["id"] + 1

    titreLivre = input("Entrer le titre du livre : ")
    auteurLivre = input("Entrer le nom de l'auteur : ")
    genrelivre = input("Entrer le genre du livre : ")
    
    livre_existe = False
    for livre in livres:
        if livre["Titre"] == titreLivre and livre["Auteur"] == auteurLivre and livre["Genre"] == genrelivre:
            livre_existe = True
            break
    
    if not livre_existe:

        
        if validerTitre(titreLivre) and validerAuteur(auteurLivre) and validerGenre(genrelivre):
            livres.append(livre)
            with open("livres.json", "w") as f:
                json.dump(livres, f, indent=2)
            print("Livre ajouté avec succès.")
        else:
            print("Impossible d'ajouter le livre car il ne remplit pas tous les critères de la bibliothèque.")
    else:
        print("Le livre existe déjà dans notre bibliothèque.")

    
        
def afficher_livres(): 
    try:
        with open("livres.json", "r") as f:
            livres = json.load(f)
            if len(livres) == 0:
                print("Le fichier JSON est vide.")
            else:
                for livre in livres:
                    print(f"Livre ID: {livre['id']}")
                    print(f"Titre: {livre['Titre']}")
                    print(f"Auteur: {livre['Auteur']}")
                    print(f"Genre: {livre['Genre']}")
                    print("--------------------")
    except FileNotFoundError:
        print("Le fichier JSON n'existe pas.")
    except json.JSONDecodeError:
        print("Le fichier JSON est mal formaté.")


# partie  recherche de livre   
def rechercherLivre():
            try:
                with open("livres.json", "r") as f:
                    livres = json.load(f)
                    if len(livres) == 0:
                        print("La bibliothèque est vide.")
                    else:
                        recherche = input("Entrez le critère de recherche (auteur, titre, genre, disponibilité): ")
                        if recherche == "auteur":
                            rechercherParAuteur(livres)
                        elif recherche == "titre":
                            rechercherParTitre(livres)
                        elif recherche == "genre":
                            rechercherParGenre(livres)
                        elif recherche == "disponibilité":
                            rechercherParDisponibilite(livres)
                        else:
                            print("Critère de recherche invalide.")
            except FileNotFoundError:
                print("Le fichier JSON n'existe pas.")
            except json.JSONDecodeError:
                print("Le fichier JSON est mal formaté.")

def rechercherParAuteur(livres):
            auteur = input("Entrez le nom de l'auteur: ")
            found_livres = [livre for livre in livres if livre["Auteur"] == auteur]
            afficherLivresTrouves(found_livres)

def rechercherParTitre(livres):
            titre = input("Entrez le titre du livre: ")
            found_livres = [livre for livre in livres if livre["Titre"] == titre]
            afficherLivresTrouves(found_livres)

def rechercherParGenre(livres):
            genre = input("Entrez le genre du livre: ")
            found_livres = [livre for livre in livres if livre["Genre"] == genre]
            afficherLivresTrouves(found_livres)

def rechercherParDisponibilite(livres):
            disponibilite = input("Entrez la disponibilité du livre (True/False): ")
            if disponibilite.lower() == "true":
                disponibilite = True
            elif disponibilite.lower() == "false":
                disponibilite = False
            else:
                print("Valeur de disponibilité invalide.")
                return
            found_livres = [livre for livre in livres if livre["Disponible"] == disponibilite]
            afficherLivresTrouves(found_livres)

def afficherLivresTrouves(livres):
            if len(livres) == 0:
                print("Aucun livre trouvé.")
            else:
                for livre in livres:
                    print(f"Livre ID: {livre['id']}")
                    print(f"Titre: {livre['Titre']}")
                    print(f"Auteur: {livre['Auteur']}")
                    print(f"Genre: {livre['Genre']}")
                    print("--------------------")


def suprimerLivre():
    livre = input("saisir l'ID du livre à supprimer: ")
    with open("livres.json", "r") as f:
        livres = json.load(f)
    index = -1
    for i in range(len(livres)):
        if livres[i]["id"] == int(livre):
            index = i
            break
    if index != -1:
        del livres[index]
        with open("livres.json", "w") as f:
            json.dump(livres, f)
        print("Livre supprimé.")
    else:
        print("Livre non trouvé.")

def archiverLivre():
    livre = input("Entrez l'ID du livre à archiver: ")
    with open("livres.json", "r") as f:
        livres = json.load(f)
    index = -1
    for i in range(len(livres)):
        if livres[i]["id"] == int(livre):
            index = i
            break
    if index != -1:
        livres[index]["Disponible"] = False
        with open("livres.json", "w") as f:
            json.dump(livres, f)
        print("Livre archivé.")
    else:
        print("Livre non trouvé.")

def suprimer_ou_archiver():
    choix = input("Entrez votre choix (1: Supprimer un livre, 2: Archiver un livre): ")
    if choix == "1":
        suprimerLivre()
    elif choix == "2":
        archiverLivre()
    else:
        print("Choix invalide.")

