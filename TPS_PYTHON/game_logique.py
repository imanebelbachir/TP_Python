import random
from TPS_PYTHON.inputs import choix_player, get_bet_amount

def spin_roulette():
    return random.randint(0, 49)

def calculate_payout(bet_amount, player_number, roulette_number):
    if player_number == roulette_number:
        return bet_amount * 3
    elif (player_number % 2) == (roulette_number % 2):  # Même couleur
        return bet_amount * 0.5
    return 0

def play_round(balance):
    player_number = choix_player()
    bet_amount = get_bet_amount()
    
    if bet_amount > balance:
        print("Vous n'avez pas assez d'argent pour miser cette somme.")
        return balance

    roulette_number = spin_roulette()
    print(f"Le numéro de la roulette est : {roulette_number}")

    payout = calculate_payout(bet_amount, player_number, roulette_number)
    balance += payout - bet_amount
    if payout > 0:
        print(f"Vous avez gagné : {payout} (solde restant : {balance})")
    else:
        print(f"Désolé, vous avez perdu votre mise. (solde restant : {balance})")

    return balance
