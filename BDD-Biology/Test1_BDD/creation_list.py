especes = [
    {"id": 1, "nom": "Alice", "famille": "Data Scientist", "population": 50000},
    {"id": 2, "nom": "Bob", "famille": "Développeur Python", "population": 45000}
]  # Liste pour stocker les espèces

def add_species():
    esp_id = input("Entrez l'ID de l'espèce (chiffres uniquement) : ")
    while not esp_id.isdigit():
        print("Erreur : l'ID doit être composé uniquement de chiffres.")
        esp_id = input("Entrez l'ID de l'espèce (chiffres uniquement) : ")

    esp_id = int(esp_id)  # Conversion en entier
    name = input("Entrez le nom vernaculaire de l'espèce : ")
    while not all(c.isalpha() or c.isspace() or c == "'" for c in name):
        print("Erreur : présence de caractères non supportés.")
        name = input("Entrez le nom vernaculaire de l'espèce : ")

    species = input("Entrez le nom latin de l'espèce : ")
    while not all(c.isalpha() or c.isspace() or c == "'" for c in name):
        print("Erreur : présence de caractères non supportés.")
        species = input("Entrez le nom latin de l'espèce : ")

    family = input("Entrez la famille de l'espèce : ")
    while not all(c.isalpha() or c.isspace() or c == "'" for c in family):
        print("Erreur : présence de caractères non supportés.")
        family = input("Entrez la famille de l'espèce : ")

    genra = input("Entrez le genre de l'espèce : ")
    while not all(c.isalpha() or c.isspace() or c == "'" for c in family):
        print("Erreur : présence de caractères non supportés.")
        genra = input("Entrez le genre de l'espèce : ")
    
    population = input("Entrez la population de l'espèce : ")
    while True:
        try:
            population = float(population)  # Conversion en float
            break
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide pour le population.")
            population = input("Entrez le population de l'espèce (nombre décimal autorisé) : ")

    # Ajout à la liste sous forme de dictionnaire
    especes.append({
        "id": esp_id,  # Correspond aux autres entrées
        "nom": name,
        "famille": family,
        "genre": genra,
        "population": population
    })
    
    print("espèce ajoutée avec succès !")

# Exemple d'utilisation
add_species()
print(especes)

#espece.pop()
#print(espece)

