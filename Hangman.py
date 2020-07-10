from nltk.corpus import words as w
import nltk as n
import string

word_list = w.words()
candidates = []
letters_dict = {}
best_number = 0
times_appeared = 0
best_char = " "
previous_best_char = []
char_position = []
show_list = []

alphabet = string.ascii_lowercase

def alpha_dict():
    global letters_dict
    for i in alphabet:
        letters_dict.__setitem__(i, 0)
    letters_dict.__setitem__('`', -1)

alpha_dict()


number_of_letters = int(input("How many letters are in your word?: "))

for i in range(number_of_letters):
    show_list.append("_")

number_of_attempts = int(input("How many attempts do you give the computer?: "))

for i in word_list:
    if len(i) == number_of_letters:
        candidates.append(i)

def show_user():
    global show_list
    update_show_list()
    print("  ".join(show_list))

def check_for_best_char():
    global number_of_letters
    global candidates
    global best_char
    global best_number
    global alphabet
    global previous_best_char

    best_number = 0

    for j in candidates:
        for k in j:
            letters_dict[k.lower()] = letters_dict[k.lower()] + 1

    for i in alphabet:
        if letters_dict[i] > best_number and i not in previous_best_char:

            best_number = letters_dict[i]
            best_char = i

def update_show_list():
    global show_list
    global best_char
    global char_position

    for i in char_position:
        show_list[i - 1] = best_char

def delete_from_candidates():
    global letters_dict
    global alpha_dict
    global alphabet
    global best_char
    global times_appeared
    global char_position

    letters_dict = {}
    alpha_dict()
    correct_number = 0
    counter = 0

    list_of_removal = []

    for i in candidates:
        counter = counter + 1

        if times_appeared == 0 and best_char in i:
            list_of_removal.append(counter - 1)

        for j in char_position:
            try:
                if i[j - 1] == best_char:
                    correct_number = correct_number + 1
            except Exception as e:
                pass

        for k in range(len(i)):
            if i[k] == best_char and k + 1 not in char_position:
                correct_number = 30

        if correct_number != len(char_position):
            list_of_removal.append(counter - 1)

        correct_number = 0

        letters_dict = {}
        alpha_dict()

    for i in list_of_removal:
        candidates[i] = "`"

def raw_candidates():
    global candidates
    real_candidates = []

    for i in candidates:
        if i != "`":
            real_candidates.append(i)

    candidates = real_candidates

def check_if_won():
    global previous_best_char
    global best_char
    global show_list
    if len(candidates) == 1 or best_char in previous_best_char:
        try:
            print("This is your word: ", candidates[0])
            return True
        except Exception as e:
            pass
    elif "_" not in show_list and "".join(show_list) not in word_list:
        print("You cannot trick me, you fool. The word doesn't exist!")
        return True

for i in range(number_of_attempts):
    char_position = []
    check_for_best_char()
    if check_if_won(): break
    times_appeared = int(input("How many times does " + best_char + " appear?: "))

    for i in range(times_appeared):
        char_position.append(int(input("Where is it located (e.g. first letter is 1): ")))
    delete_from_candidates()
    raw_candidates()
    show_user()
    if check_if_won(): break
    previous_best_char.append(best_char)