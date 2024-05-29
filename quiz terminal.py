import random

# Liste des mots à deviner
word_list = ["ordinateur", "python", "programmation", "algorithme", "machine"]

# Choisir un mot au hasard dans la liste
chosen_word = random.choice(word_list)

# Créer une liste pour stocker les lettres devinées correctement
display = ["_" for _ in chosen_word]

# Nombre total d'essais autorisés
total_tries = 6

# Garder une trace des essais restants
tries_left = total_tries

print("Bienvenue dans le jeu de pendu!")
print("Le mot à deviner a", len(chosen_word), "lettres.")

while tries_left > 0 and "_" in display:
    print("\nEssais restants:", tries_left)
    print("Mot à deviner:", " ".join(display))
    
    # Demander une lettre au joueur
    guess = input("Devinez une lettre: ").lower()

    if len(guess) != 1:
        print("Veuillez entrer une seule lettre.")
        continue

    # Si la lettre devinée est dans le mot
    if guess in chosen_word:
        # Mettre à jour le mot à afficher
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print("Bien joué! La lettre", guess, "est correcte.")
    else:
        # Réduire le nombre d'essais restants
        tries_left -= 1
        print("Oups! La lettre", guess, "n'est pas dans le mot.")

if "_" not in display:
    print("\nFélicitations! Vous avez deviné le mot:", "".join(display))
else:
    print("\nDésolé, vous avez perdu. Le mot était:", chosen_word)
