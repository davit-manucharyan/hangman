import random


def count_of_space(word:str):
    space = "_"
    list_of_spaces = []

    for i in range(len(word)):
        list_of_spaces.append(space)

    return list_of_spaces

def word_choice(word_list: list):
    return random.choice(word_list)

def section_of_words(main_world: str):
    letters_list_in_def = []

    for letter_for_section in main_world:
        letters_list_in_def.append(letter_for_section)

    return letters_list_in_def

def enter_letter():
    letter_in_def = input("enter the letter: ")

    return letter_in_def


def error_404(letter_in_error: str):
    return f"there is no letter {letter_in_error} in the word"

def correct_letter_def(word_in_list_in_def: list, letter_in_correct_def: str,
                       spaces_in_list: list):
    for letter_id_for in range(len(word_in_list_in_def)):
        if letter_in_correct_def == word_in_list_in_def[letter_id_for]:
            for i in range(len(spaces_in_list)):
                if i == letter_id_for:
                    spaces_in_list.pop(i)
                    spaces_in_list.insert(i, word_in_list_in_def[letter_id_for])

    return spaces_in_list
