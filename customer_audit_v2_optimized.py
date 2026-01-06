# Refactored and optimized version of the previous audit script.
# Improved logic to remove nested loops and used math to find duplicates.

from collections import Counter


char_occurance = 0
negative_occurance = 0


raw_customer_ids = [101, "102", 101, "abc", 103, " 104 ", 102, 105, "101", -999]
str_conversion = list(map(str, raw_customer_ids))

for alpha in str_conversion:
    if alpha.isalpha():
        char_occurance += 1
        str_conversion.remove(alpha)

int_conversion = list(map(int, str_conversion))
for digit in int_conversion:
    if digit <= 0:
        negative_occurance += 1
        int_conversion.remove(digit)

int_conversion.sort()
sorted_id = list(dict.fromkeys(int_conversion))
total_id = len(int_conversion)
duplicate_id = len(sorted_id)
total_duplicates = total_id - duplicate_id
Bad_entries = char_occurance + negative_occurance

print(f'Cleaned id : {sorted_id}')        
print(f'The total no of duplicates in the list are: {total_duplicates}')
print(f'The total no of bad Entries are: {Bad_entries}')