# Customer ID audit script (v1)
# Beginner-level implementation focused on understanding data cleaning logic



from collections import Counter

char_Occ = 0
neg_Occ = 0


raw_customer_ids = [101, "102", 101, "abc", 103, " 104 ", 102, 105, "101", -999]
str_convert = list(map(str, raw_customer_ids)) #Converted all itesm to string
for ch in str_convert:
    if ch.isalpha():
        char_Occ += 1

for id in str_convert:
    if id.isalpha():
        str_convert.remove(id)
        convertTo_int = list(map(int, str_convert))

        for negg in convertTo_int:
            if negg <= 0:
                neg_Occ += 1

                for negitive in convertTo_int:
                    if negitive <= 0:
                        convertTo_int.remove(negitive)
                        convertTo_int.sort()

                        copy_count = Counter(convertTo_int)
                        no_of_copy = len(copy_count)

                        dupli_removed_list = list(dict.fromkeys(convertTo_int))#removing duplicates
                        dupli_remove = list(dict.fromkeys(convertTo_int))

                        print(f'Cleaned list: {dupli_remove}')
                        print(f'Total Duplicate\'s occured: {no_of_copy}')
                        print(f'Total Bad Entries: {char_Occ + neg_Occ}')
