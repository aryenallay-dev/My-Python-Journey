warehouse_data = [
    ["Laptop", "Electronics", 1200, 5],
    ["Chair", "Furniture", 150, 0],
    ["Phone", "Electronics", 800, 10],
    ["Table", "Furniture", 300, 2]]

for items in warehouse_data:
    print(items)


electronics = []
for lists in warehouse_data:
    if 'Electronics' in lists:
        electronics.append(lists)


for quantity in warehouse_data:
    if 0 in quantity:
        print(f'The quantity of the list, {quantity}, should be refilled')
  

amount = electronics[0][2] + electronics[1][3]
quantity = electronics[1][2]  + electronics [1][3]
total = amount * quantity
print(f'Total is {total}')

