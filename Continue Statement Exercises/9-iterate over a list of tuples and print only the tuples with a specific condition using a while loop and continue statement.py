tuple_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
i = 0
while i < len(tuple_list):
    if sum(tuple_list[i]) % 4 == 0:
        print(tuple_list[i])
    i += 1
