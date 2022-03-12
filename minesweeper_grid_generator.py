import random


def main():
    row = int(input("How many rows do you want to be in the grid? "))
    col = int(input("How many columns do you want to be in the grid? "))
    mines = int(input("How many mines do you want to be in the grid? "))
    grid(row, col, mines)


def grid(row, col, mine_number):

    mine = 0
    mines = []
    for i in range(mine_number):
        mines.append(mine)

    rand_index_list = []
    for l in range(mine_number):
        num = random.randint(0, (row * col) - 1)
        if num in rand_index_list:
            num2 = random.choice([o for o in range(0, (row * col) - 1) if o not in rand_index_list])
            rand_index_list.append(num2)
        else:
            rand_index_list.append(num)

    row_col = []
    for g in range(0, (row * col)):
        row_col.append(1)

    for a in range(0, len(rand_index_list)):
        row_col[rand_index_list[a]] = 0

    final_grid_list = []
    for s in range(0, len(row_col), col):
        final_grid_list.append(row_col[s:s + col])

    for q in range(len(final_grid_list)):
        print(final_grid_list[q], end='\n')

main()
