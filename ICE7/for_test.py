int_list = [1, 2, 3, 4, 5, 6]
i = 1
sum = 0

for iter in int_list:
    sum += iter

print("Average is: " + str(sum / len(int_list)))