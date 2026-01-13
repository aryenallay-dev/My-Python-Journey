#Initial warehouse script: calculated electronics total using total_price * total_quantity
#Fixed logic bug: switched to per-item price * quantity for correct total

warehouse_data = [
    ["Laptop", "Electronics", 1200, 5],
    ["Chair", "Furniture", 150, 0],
    ["Phone", "Electronics", 800, 10],
    ["Table", "Furniture", 300, 2]]

for items in warehouse_data:
    print(items)


electronics = []
for lists in warehouse_data:
    if lists[1] == 'Electronics':
        electronics.append(lists)


for quantity in warehouse_data:
    if  quantity[3] == 0:
        print(f'The quantity of the list, {quantity}, should be refilled')


total_amount = sum(item[2] * item[3] for item in electronics)
print(f'The total is: {total_amount}')
