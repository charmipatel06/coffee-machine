take_num = int(input())
take_num2 = []
for _ in range(1, take_num + 1):
    take_num2.append(int(input()))

for i in take_num2:
    if i % 7 == 0:
        print(i ** 2)
