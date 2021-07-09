def convert_camel_snake_case(name):
    new_string = ''
    for i in name:
        if i.isupper():
            new_string += ('_' if len(new_string) != 0 else '') + i.lower()
        else:
            new_string += i

    print(new_string)


string_input = input()
convert_camel_snake_case(string_input)
