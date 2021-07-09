# put your python code here

first_num = int(input())
second_num = int(input())
list_num = []
for i in range(first_num, second_num + 1):
    if i % 3 == 0:
        list_num.append(i)

total_val = 0
for i in list_num:
    total_val += i

final_meanval = total_val / len(list_num)
print(final_meanval)