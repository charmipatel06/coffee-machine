# Write your code here
# print('Write how many cups of coffee you will need:')
# coffee_cup_no = int(input())
#
# total_water = 200 * coffee_cup_no
# total_milk = 50 * coffee_cup_no
# total_coffee = 15 * coffee_cup_no
#
# print('For', coffee_cup_no,'cups of coffee you will need:')
# print(total_water, 'ml of water')
# print(total_milk, 'ml of milk')
# print(total_coffee, 'g of coffee beans')

print('Write how many ml of water the coffee machine has:')
total_water = int(input())
print('Write how many ml of milk the coffee machine has:')
total_milk = int(input())
print('Write how many grams of coffee beans the coffee machine has:')
total_coffee = int(input())
print('Write how many cups of coffee you will need:')
coffee_cup_no = int(input())

machine_coffee_made = 0
while True:
    total_water -= 200
    total_milk -= 50
    total_coffee -= 15
    if total_water < 0 or total_milk < 0 or total_coffee < 0:
        break
    machine_coffee_made += 1


if coffee_cup_no > machine_coffee_made:
    print('No, I can make only',machine_coffee_made,'cups of coffee')
elif coffee_cup_no == machine_coffee_made:
    print('Yes, I can make that amount of coffee')
elif coffee_cup_no < machine_coffee_made:
    extra_coffee_cup = machine_coffee_made - coffee_cup_no
    print('Yes, I can make that amount of coffee (and even ', extra_coffee_cup,' more than that)')




