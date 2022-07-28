from random import choice

print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*Welcome to the nine lives game-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
print('')
print('Description below.')
print('')
print('This game is all about luck, you should guess a random word. You only have 9 lives so choose them wisely. ')
print('')

lives = 9
secret_word_list = ['pizza', 'car', 'banana', 'apple', 'orange', 'pineapple']
secret_word = choice(secret_word_list)

found_letters_location = []
hidden_letters = []
word_letters = list(secret_word)

for i in range(0, len(word_letters)):
    hidden_letters.append('?')


def update_letter(word_list: list, hidden_list: list, guessed_letter: str):
    for x in range(0, len(word_list)):
        if guessed_letter == word_list[x]:
            hidden_list[x] = guessed_letter


while lives > 0:
    guess = input('Enter a random letter: ').lstrip().rstrip().lower()

    if guess in secret_word:
        update_letter(word_list=word_letters, hidden_list=hidden_letters, guessed_letter=guess)
    else:
        lives = lives - 1
        print('Wrong choice.')
        print(f'You have {lives} left.')

    print(hidden_letters)
    print('')

    if '?' not in hidden_letters:
        print('You are a winner!!!')
        break

if lives == 0:
    print('Loser....')
