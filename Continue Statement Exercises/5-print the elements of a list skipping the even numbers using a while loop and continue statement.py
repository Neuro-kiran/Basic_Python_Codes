my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
while i < len(my_list):
    if my_list[i] % 2 == 0:
        i += 1
        continue
    print(my_list[i])
    i += 1
