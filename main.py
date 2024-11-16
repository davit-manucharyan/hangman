from images import images_list
from words_and_lists import words, alphabet
import defs


while True:
    riddle_word = defs.word_choice(words)
    list_of_spaces = defs.count_of_space(riddle_word)
    letters_list = defs.section_of_words(riddle_word)

    tries = 0

    game_start = input("start the game? (y/n): ")
    if game_start == "n":
        break

    elif game_start == "y":
        print("welcome to my game :D\n")
        while tries < 5:


            print(list_of_spaces)
            letter = defs.enter_letter()
            while letter not in alphabet:
                print("unclear answer, try agen")
                print()
                letter = defs.enter_letter()

            if letter not in letters_list:
                print(defs.error_404(letter))
                print()
                print(images_list[tries])
                print()
                print()

                if tries == 4:
                    print("you lost(\n")
                    break

                tries += 1

            else:
                defs.correct_letter_def(letters_list, letter, list_of_spaces)
                print()
                print()
                if "_" not in list_of_spaces:
                    print("YOU WON!! :D")
                    print()
                    print()
                    break

    else:
        print("unclear answer, try agen")
        print()
