

list = [[1] * 21];
print(list)
for i in range(1, 21):
    new_list = [0] * 21

    for j in range(0, 21):
        if ( 0 == j):
            new_list[j] = 1
        else:
            new_list[j] = new_list[j-1] + list[i-1][j]

    list.append(new_list)

print(list)

