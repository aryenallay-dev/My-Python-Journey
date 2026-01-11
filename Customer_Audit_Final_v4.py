#Replaced mutable list removal with the New List Pattern…


raw_customer_ids = [101, "102", 101,  "abc", 103, " 104 ", 102, 105, "101", -999]
str_ids = list(map(str, raw_customer_ids))

#REMOVING DUPLICATES BY CONVERTING TO SET
set_ids = set(str_ids)
list_ids = list(set_ids)

clean_ids = []
for id in list_ids:
    if not id.isalpha():
        clean_ids.append(id)


int_ids = list(map(int, clean_ids))

extra_cleaned_ids = []
for neg in int_ids:
    if not neg <= 0:
        extra_cleaned_ids.append(neg)
        
neg_occ = len(clean_ids) - len(extra_cleaned_ids)
bad_occ = len(list_ids) - len(clean_ids)
bad_entries = neg_occ + bad_occ
sorted_ids = sorted(extra_cleaned_ids)
duplicate = len(raw_customer_ids) - len(set_ids)

print(sorted_ids)
print(f'There were: {bad_entries} bad entries')
print(f'Total duplicates were: {duplicate}')

