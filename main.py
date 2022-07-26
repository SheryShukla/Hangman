import random
from word import word_list
from h import stages, logo

print(logo)

game_is_finished = False
chosen_word = random.choice(word_list)
word_len = len(chosen_word)
lives = 6


# def playAg
x = input("\nDo you want to play?(y/n):  ").lower()

display = []
for _ in range(word_len):
    display += "_"

while x == 'y':
    while not game_is_finished:
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"You guessed the correct word {guess}")

        for position in range(word_len):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                game_is_finished = True
                print("You lose.")
                print(f"The correct word is {chosen_word}")

        print(f"{' '.join(display)}")

        if not "_" in display:
            game_is_finished = True
            print("You win.")

        print(stages[lives])

