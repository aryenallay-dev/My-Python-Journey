#Improved it a little more, or so i think ^_^

alpha_occ = 0
neg_occ = 0


raw_customer_ids = [101, "102", 101, "abc", 103, " 104 ", 102, 105, "101", -999]
str_conversion = list(map(str, raw_customer_ids))

for id_no in str_conversion:
    if id_no.isalpha():
        alpha_occ += 1 
        str_conversion.remove(id_no)

int_conversion = list(map(int, str_conversion))
for neg in int_conversion:
    if neg <= 0:
        neg_occ += 1
        int_conversion.remove(neg)

clear_duplicate = list(dict.fromkeys(int_conversion))
sorting = sorted(clear_duplicate)
total_dup = len(int_conversion) - len(clear_duplicate)
Bad_entries = alpha_occ + neg_occ

print(clear_duplicate)
print(f'Duplicates: {total_dup}')
print(f'Bad entries: {Bad_entries}')


