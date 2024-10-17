from TPS_PYTHON.game_logique import play_round

def main():
    balance = 100  # Montant de départ
    print("Bienvenue au ZCasino!")
    while True:
        print(f"Votre solde actuel est : {balance}")
        balance = play_round(balance)  # Jouer un tour
        
        if balance <= 0:
            print("Vous n'avez plus d'argent ! Merci d'avoir joué.")
            break
        
        again = input("Voulez-vous jouer à nouveau ? (o/n) : ")
        if again.lower() != 'o':
            print("Merci d'avoir joué ! À bientôt.")
            break

if __name__ == "__main__":
    main()
