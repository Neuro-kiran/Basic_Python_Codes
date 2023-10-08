total = 0
for num in range(1, 101):
    if num % 5 == 0:
        continue
    total += num
print(total)
