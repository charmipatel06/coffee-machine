# put your code here
num_list = []
while True:
    take_val = int(input())
    if take_val == 55:
        break
    else:
        num_list.append(take_val)

print(len(num_list))
print(sum(num_list))
print(round(sum(num_list) / len(num_list)))
