
odd = []
even = []

for i in range(10):
    if (i%2) == 0:
        even.append(i)
    else:
        odd.append(i)

merged_list = odd + even
merged_list = [i * 2 for i in merged_list]

for j in range(len(merged_list)):
    print(type(merged_list[j]))



print(merged_list)


