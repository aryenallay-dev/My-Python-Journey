# Beginner practice: checking if a number is even or odd
# Focused on understanding input validation and control flow


while True:
    num = input('Enter the number: ')
    digit = num.isdigit()
    if digit == True:
        conversion = int(num)
        if conversion % 2 == 0:
            print('Even')
            print('IT is a number')
        else:
            print('Odd')
            print('IT is a number')
        break
    else:
        print('Error: Invalid Data Type')
        
