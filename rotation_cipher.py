user_input = input("Enter a line: ")
rotate_user_input = int(input("By how much should I rotate the line by? "))
final_list = []


def separate(user, rotate):
    number_list = []
    number_index_list = []
    for i in range(0, len(user)):
        if user[i].islower() or user[i].isupper():
            pass
        elif (not user[i].islower()) or (not user[i].isupper()):
            number_list.append(user[i])
            number_index_list.append(i)

    for j in range(0, len(number_list)):
        number_list[j] = int(number_list[j])

    for k in range(0, len(number_list)):
        number_list[k] += rotate

    new_num = []
    for l in number_list:
        new_num.append(str(l))

    dict_number = {}
    for key1 in new_num:
        for value1 in number_index_list:
            dict_number[key1] = value1
            number_index_list.remove(value1)
            break

    for key2, value2 in dict_number.items():
        final_list.insert(value2, key2)

    upper_alphabet_list = []
    lower_alphabet_list = []
    lower_alphabet_list_index = []
    upper_alphabet_list_index = []
    for m in range(0, len(user)):
        if user[m].islower():
            lower_alphabet_list.append(user[m])
            lower_alphabet_list_index.append(m)
        elif user[m].isupper():
            upper_alphabet_list.append(user[m])
            upper_alphabet_list_index.append(m)

    upper_alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                       "T", "U", "V", "W", "X", "Y", "Z"]

    lower_alphabets = ['a', "b", 'c', "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                       "t", "u", "v", "w", "x", "y", "z"]

    lower_new_new_index = 0
    lower_new_j = 0
    new_lower_list = []
    for n in range(0, len(lower_alphabets)):
        for o in range(0, len(lower_alphabet_list)):
            if lower_alphabets[n] == lower_alphabet_list[o]:
                lower_new_j = n + rotate
                lower_new_new_index = lower_new_j
                if lower_new_new_index >= 25:
                    while lower_new_new_index >= 25:
                        lower_new_new_index = lower_new_j - 26
                new_lower_list.append(lower_alphabets[lower_new_new_index])

    dict_lower = {}
    for key3 in new_lower_list:
        for value3 in lower_alphabet_list_index:
            dict_lower[key3] = value3
            lower_alphabet_list_index.remove(value3)
            break

    for keys4, values4 in dict_lower.items():
        final_list.insert(values4, keys4)

    upper_new_new_index = 0
    upper_new_j = 0
    new_upper_list = []
    for p in range(0, len(upper_alphabets)):
        for q in range(0, len(upper_alphabet_list)):
            if upper_alphabets[p] == upper_alphabet_list[q]:
                upper_new_j = p + rotate
                upper_new_new_index = upper_new_j
                if upper_new_new_index >= 25:
                    while upper_new_new_index >= 25:
                        upper_new_new_index = upper_new_j - 26
                new_upper_list.append(lower_alphabets[upper_new_new_index])

    dict_upper = {}
    for key5 in new_upper_list:
        for value5 in upper_alphabet_list_index:
            dict_upper[key5.upper()] = value5
            upper_alphabet_list_index.remove(value5)
            break

    for keys6, values6 in dict_upper.items():
        final_list.insert(values6, keys6)


separate(user_input, rotate_user_input)


print("Final String: " + ''.join(final_list))