def commas(a_list):
    my_sentence =''
    for i in range(len(a_list)):
        if i == len(a_list) - 1:
            my_sentence += ', and ' + a_list[i]
        elif i == 0:
            my_sentence = a_list[i]
        else:
            my_sentence += ', ' + a_list[i]
    return my_sentence


# print(commas(['apples', 'bananas', 'tofu', 'cats', 'dogs']))

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j], end='')
    print()
