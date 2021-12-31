def main():
    user_input = input("Please enter your list separated by spaces: ")
    user_list = user_input.split()

    for m in range(0, len(user_list)):
        user_list[m] = int(user_list[m])

    multiply(user_list)


def multiply(user_list):
    duplicate = []
    removed_num = 0
    multiplication = 1

    for i in range(len(user_list)):
        duplicate.append(user_list[i])

    for j in range(0, len(user_list)):
        for k in range(0, len(duplicate)):
            if user_list[j] == duplicate[k]:
                removed_num = user_list[j]
                duplicate.remove(removed_num)
                for l in range(0, len(duplicate)):
                    multiplication *= duplicate[l]
                print("Multiplication without", j, "th", "index is:", multiplication)
                duplicate.insert(j, removed_num)
                multiplication = 1


main()