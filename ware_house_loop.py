warehouse_data = [
    ["Laptop", "Electronics", 1200, 5],
    ["Chair", "Furniture", 150, 0],
    ["Phone", "Electronics", 800, 10],
    ["Table", "Furniture", 300, 2]]

items = []
for item in warehouse_data:
    items.append(item[1])

set_items = set(items)
tuple_items = tuple(set_items)

while True:
    user_choice = input(f'Which of the items would u like see list & total of: {tuple_items}')
    correction = user_choice.capitalize()
    if correction not in tuple_items:
        print('Wrong input try again')
    else:
        break

choice = []
for want in warehouse_data:
    if correction == want[1]:
        choice.append(want)
    
print(f'items in \'{correction}\':')

for c in choice:
    print(f'{c[0]} = (Price: {c[2]}, Quantity: {c[3]})')

total = sum(amount[2] * amount[3] for amount in choice)
print(f'The total is {total}')  



