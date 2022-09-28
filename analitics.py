nums = list()
for i in range(10, 100):
    if i % 8 == 0:
        nums.append(i)
    if i % 7 == 0:
        nums.append(i)
print(*nums, sep='\n')

