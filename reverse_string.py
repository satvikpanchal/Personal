def main():
    user_input = input("Enter a string you want to reverse: ")
    reverse_str(user_input)


def reverse_str(user_input):
    user_len = len(user_input) - 1
    new_string = ""
    while user_len != 0:
        new_string += user_input[user_len]
        user_len -= 1
    new_string += user_input[0]

    print(new_string)


main()
