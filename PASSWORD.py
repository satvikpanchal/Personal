import random


def main():
    menu()


def menu():
    string = "A) 'A' for creating a random numbered password \n" \
             "B) 'B' for creating a random alphabet password \n" \
             "C) 'C' for converting a numerical password to a alphabets password \n" \
             "D) 'D' for converting a alphabets password to a numerical password \n" \
             "E) 'E' to quit"
    print(string)

    user_input = input("Please select from the menu: ")
    menu_option(user_input)


def menu_option(u_input):
    if u_input == "A":
        random_password_num()
    elif u_input == "B":
        random_password_alphabet()
    elif u_input == "C":
        num_to_alphabet()
    elif u_input == "D":
        alphabet_to_num()
    elif u_input == "E":
        exit()
    else:
        print('')
        main()


def lower_alphabets():
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
             "t", "u", "v", "w", "x", "y", "z"]
    return lower


def upper_alphabets():
    upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
             "T", "U", "V", "W", "X", "Y", "Z"]
    return upper


def what_length():
    length = int(input("How long should be the password? "))
    return length


def lower_or_upper():
    l_or_u = input("Do you want the alphabets be upper or lower case? \nL for lower and U for upper: ")
    if l_or_u == "L":
        return_type = lower_alphabets()
    elif l_or_u == "U":
        return_type = upper_alphabets()
    return return_type


def random_password_num():
    length = what_length()
    start = pow(10, length - 1)
    end = pow(10, length) - 1
    random_pass_num = random.randint(start, end)

    print("The random password number generated of", length, "is:", random_pass_num)
    # DONE


def random_password_alphabet():
    choice = lower_or_upper()
    length = what_length()

    random_alph = ""

    for i in range(0, length):
        random_alph += random.choice(choice)

    print("The random password number generated of", length, "is:", random_alph)

    # DONE


def num_to_alphabet():
    choice = lower_or_upper()
    usr_inp = input("Please enter a series of number separated by a hyphen(-) in pairs with A/a being 0 and Z/z being "
                    "25 : ")
    usr = usr_inp.split('-')
    new_list = []
    new_str = ''

    for i in range(0, len(usr)):
        if int(usr[i]) < 26:
            new_list.append(int(usr[i]))
            pass
        else:
            first_num = int(int(usr[i]) / 10)
            last_num = int(usr[i]) % 10
            new_list.append(first_num)
            new_list.append(last_num)

    for j in range(0, len(new_list)):
        for k in range(0, len(choice)):
            if new_list[j] == k:
                new_str += choice[k]

    print("The password converted from numbers to alphabets is:", new_str)
    # DONE


def alphabet_to_num():
    usr_inp = input("Please enter a series of alphabets with A/a being 0 and Z/z being 25 : ")
    int_to_str = ''
    upper = upper_alphabets()
    upper_list = []

    for k in range(0, len(usr_inp)):
        upper_list.append(usr_inp[k].upper())

    for i in range(0, len(upper_list)):
        for j in range(0, len(upper)):
            if upper_list[i] == upper[j]:
                int_to_str += str(j) + '-'

    final_num = int_to_str.rstrip(int_to_str[-1])

    print("The password converted from alphabets to numbers is:", final_num)
    # DONE


main()