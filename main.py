# Basic definitions
import random
from replit import clear
from Hangman_ascii import stages, logo
from Hangman_words import word_list

chosen_word = random.choice(word_list)
hidden_word = list(("_") * len(chosen_word))
display = " ".join(hidden_word)
lives = 6

#print(f"(CONTROL) The word is: {chosen_word}\n")
print(logo)
print(display)

#######  body ---------------------------------------------------------------
while "_" in hidden_word and lives > 0:
  print(stages[lives])
  
  #input
  guess = (input("Guess a letter\n\n")).lower()
  clear()
  if guess in display:
    print("You already guessed this letter")
  
  #wrong letter
  if guess not in chosen_word:
    print("Wrong!")
    print(display)
    lives -= 1

  #right letter
  else:
    cycle = - 1
    for letter in chosen_word:
      cycle += 1
      if letter == guess:
        hidden_word[cycle] = guess
        display = " ".join(hidden_word)
    print(display)


# victory conditions
if lives == 0:
  print(stages[lives])
  print("You lost")
if "_" not in hidden_word:
  print("Yay! You won!")