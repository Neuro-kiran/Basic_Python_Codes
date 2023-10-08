count = 0
for num in range(1, 31):
    if num == 9:
        continue
    if num % 3 == 0:
        print(num)
        count += 1
    if count == 10:
        break
