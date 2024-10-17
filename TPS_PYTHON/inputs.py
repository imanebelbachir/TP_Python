import logging 

# Configuration du logging
logging.basicConfig(
    filename='programe.log',  # Nom du fichier de log
    level=logging.INFO,        # Niveau de gravité des messages à enregistrer
    format='%(asctime)s - %(levelname)s - %(message)s'  # Format des messages
)
def get_bet_amount():
    while True:
        try:
            amount = float(input("Entrez votre mise: "))
            if amount <= 0:
                print("La mise doit être positive.")
            else:
                return amount
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def choix_player():
    while True:
        try:
            number = int(input("Choisissez un nombre entre 0 et 49: "))
            if 0 <= number <= 49:
                return number
            else:
                print("Le nombre doit être entre 0 et 49.")
        except ValueError as e:
            print("Veuillez entrer un nombre valide.")
            logging.error(f"Erreur lors de l'entrée utilisateur : {e}")
