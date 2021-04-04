import string
import time
try:
    from nltk.corpus import words as w
except Exception as e:
    import nltk as n
    n.download()

word_list_pre = []
word_list = []
candidates = []
letters_dict = {}
best_number = 0
times_appeared = 0
best_char = " "
save_candidates = 0
previous_best_char = []
prev_best_char = ''
char_position = []
show_list = []
common_word_list = []
first_failed = True   #500
second_failed = True  #250
third_failed = True   #100
fourth_failed = True   #50
fifth_failed = True   #2


alphabet = string.ascii_lowercase

def make_common_list():
    global common_word_list
    temp_list = []
    f = open("20k.txt", 'r')
    for i in f.read():
        if i in alphabet:
            temp_list.append(i)
        else:
            common_word_list.append("".join(temp_list))
            temp_list = []

make_common_list()


def make_word_list():
    global word_list_pre
    temp_list = []
    f = open("words.txt", 'r')
    for i in f.read():
        if i in alphabet:
            temp_list.append(i)
        else:
            word_list_pre.append("".join(temp_list))
            temp_list = []
make_word_list()
def check_word_list():
    global word_list
    global world_list_pre

    for i in word_list_pre:
        try:
            if i[0] != " ":
                word_list.append(i.lower())
        except Exception as e:
            pass


check_word_list()


def alpha_dict():
    global letters_dicts
    for i in alphabet:
        letters_dict.__setitem__(i, 0)
    letters_dict.__setitem__('`', -1)

alpha_dict()


number_of_letters = int(input("How many letters are in your word?: "))


for i in range(number_of_letters):
    show_list.append("_")

number_of_attempts = int(input("How many attempts do you give the computer?: "))
word_list = word_list + w.words()
for i in word_list:
    if len(i) == number_of_letters:
        candidates.append(i)

def show_user():
    global show_list
    update_show_list()
    print("  ".join(show_list))

def check_for_best_word():
    global candidates
    global common_word_list
    for i in range(len(common_word_list)):
        for j in range(len(candidates)):
            if common_word_list[i] == candidates[j]:
                if str(input("Is this your word: " + candidates[j] + "? ")) == "No":
                    candidates[j] = "`"
                    return "No"
                else:
                    return "Yes"


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
            try:
                letters_dict[k.lower()] = letters_dict[k.lower()] + 1
            except Exception as e:
                pass

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
    global save_candidates

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
    save_candidates = []
    temp_save = []
    for i in list_of_removal:
        if candidates[i] != "`":
            save_candidates.append(candidates[i])
        candidates[i] = "`"
    if len(list_of_removal) < 500:
        [temp_save.append(x) for x in save_candidates if x not in temp_save]
        save_candidates = temp_save



def raw_candidates():
    global candidates
    global save_candidates
    real_candidates = []

    for i in candidates:
        if i != "`":
            real_candidates.append(i)
    if len(real_candidates) > 0:
        save_candidates = real_candidates
    candidates = real_candidates

def check_if_won():
    global previous_best_char
    global best_char
    global show_list
    global prev_best_char

    if len(candidates) == 1 or "_" not in show_list:
        try:
            print("This is your word: ", candidates[0])
            time.sleep(10)
            return True
        except Exception as e:
            pass

    if prev_best_char == best_char:
        print("You cannot trick me, you fool. The word doesn't exist!")
        print("Here were some closest words: ", save_candidates)
        time.sleep(10)
        return True



for i in range(number_of_attempts):
    char_position = []
    if (5 >= len(candidates) and first_failed) or ():
        if (check_for_best_word()) == "Yes":
            break
        else:
            first_failed = True

    else:
        check_for_best_char()
    check_for_best_char()
    if check_if_won():
        break
    times_appeared = int(input("How many times does " + best_char + " appear?: "))
    prev_best_char = best_char

    for i in range(times_appeared):
        char_position.append(int(input("Where is it located (e.g. first letter is 1): ")))
    delete_from_candidates()
    raw_candidates()
    show_user()
    previous_best_char.append(best_char)
else:
    print("Welp, I lost. Probably you should give more attempts")
    time.sleep(10)
