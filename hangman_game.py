import os
import random

def refresh_screen():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def read():
    names = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            names.append(line)
    return random.choice(names)


def run():
    word = read()
    
    print(word)
    dicc = {"á": "a", "é":"e", "í": "i", "ó": "o", "ú": "u"}

    for lett in word:
        if lett in dicc:
            new_letter = dicc[lett]
            word = word.replace(lett, new_letter)

    list_convert = list(word)
    print(list_convert)
    

    new_list = list(list_convert)

    new_list = ["-" for i in range(len(new_list))]

    intentos = 5

    while intentos != 0:
        print("Bienvenido al hangman game, tienes " + str(intentos) + " vidas!.")
        print(new_list)
        new_list = list(new_list)

        if new_list == list_convert:
            print("Ganaste el juego. Felicitaciones!")
            break

        letter = input("Choice a letter: ")

        acumulado = 0

        for i in range(len(new_list)):
            if list_convert[i] == letter and new_list[i] == "-":
                print(new_list[i])
                new_list[i] = letter
                acumulado =+ 1
        
        if acumulado == 0:
            intentos = intentos - 1

        new_list = "".join(new_list)
        refresh_screen()
        

if __name__ == "__main__":
    run()



# """ Game class with methods to help play Hangman """

# # random to select random word
# import random

# class Game:

#     def __init__(self):
#         """ open file with words """
#         self.words = []
#         with open('data.txt', mode='r', encoding='utf-8') as file:
#             for word in file:
#                 self.words.append(word)


#     def get_random_word(self):
#         """ choose and return a random word """
#         words_with_accents = {'á': 'a','é': 'e','í': 'i','ó': 'o','ú': 'u'}
#         word = lambda words: random.choice(self.words)
#         random_word = word(self.words)

#         for letter in random_word:
#             if letter in words_with_accents:
#                 new_letter = words_with_accents[letter]
#                 random_word = random_word.replace(letter, new_letter)

#         return random_word


#     @staticmethod
#     def is_correct(user_letter, word):
#         """ return indices where user_letter is in word """
#         indices = [index for index, value in enumerate(word) if value == user_letter]

#         if indices:
#             return indices

#         return '_'
