raw_ids = ["TX101", "TX102", "TX101", "TX103", "TEST_99", "TX102", "TEST_00"]

set_ids = set(raw_ids)
list_ids = list(set_ids)


final_ids = []
for ids in list_ids:
    if not ids.startswith('TEST'):
        final_ids.append(ids)
        
print(final_ids)

tuple_ids = tuple(final_ids)
tuple_ids[0] = 'Appple'
print(tuple_ids)


