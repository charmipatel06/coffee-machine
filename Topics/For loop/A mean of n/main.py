take_num = int(input())
take_num2 = []

for _ in range(1, take_num + 1):
    take_num2.append(int(input()))

sum_val = 0
for i in take_num2:
    sum_val += i

print(sum_val / take_num)
