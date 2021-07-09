string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
total_vowels = 0

for i in vowels:
    for j in string:
        if i == j:
            total_vowels += 1

print(total_vowels)