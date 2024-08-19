import random

words = "abuser crottes fleches continental babiole etoile bougie coup coeur malade"

# convertir la chaine de catactères "words" en liste
word_list = words.split()

#Génère un index aléatoire pour séléctionner un mot aléatoirement dans la liste.
secret = random.randint(0, len(word_list) -1)

#Récupère le mot aléatoire en utilisant l'index généré aléatoirement
secret_word = word_list[secret]

#Le dictionnaire game contient les informations requis pendant la partie: le mot à deviner, l'affichage des tirest et des lettres devinées et les vies
game = {
    "secret_word" : secret_word,
    "guess_word": "_" * len(secret_word),
    "life" : 9
}

#afficher les tirest et le nombe de vie
print(f"{game['guess_word']} | vies : {game['life']}")

while True:
    letter = input('Entrez une lettre : ')
    if letter in game['secret_word'] and letter not in game['guess_word']:
        #transformer la chaîne de caractères en liste pour modidifer 'guess_word' car une chaine de caractère n'est pas modifiable
        guess_word_list = list(game['guess_word'])

        #Parcourir la chaîne de caratères du mot à deviner car une chaîne de caractères est itérable, enumerate() permet de recuperer l'index
        for index, current_letter in enumerate(game['secret_word']):
            if current_letter == letter:
                #remplaçer le tiret dans guess_word_list par la lettre à la bonne position grâce à l'index
                guess_word_list[index] = letter

        #une fois parcouru le mot à deviner, recéer une chaîne de caractères à partir de guess_word_list        
        game['guess_word'] = "".join(guess_word_list)        
    elif letter not in game['secret_word']: 
        game['life'] -= 1
    print(f"{game['guess_word']} | vies : {game['life']}")
    if "_" not in game['guess_word']:
        print('WIN ! ')
        break
    elif game['life'] < 1:
        print('game over !')
        break





# import random

# words = "abuser crottes fleches continental babiole etoile bougie coup coeur malade"
# words_list = words.split()
# secret = random.randint(0, len(words_list) - 1)
# secret_word = words_list[secret]
# game = {
#     'secret_word': secret_word,
#     'guess_word': '_' * len(secret_word),
#     'life': 9
# }

# print(f"{game['guess_word']} | vies : {game['life']}")

# while True:
#     letter = input('Entrez une lettre : ')