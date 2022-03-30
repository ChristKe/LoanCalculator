# put your python code here
f_number = float(input())
s_number = float(input())
operation = ['+', '-', '*', '/', 'mod', 'pow', 'div']
operator = input()

if operator == operation[0]:
    print(f_number + s_number)
elif operator == operation[1]:
    print(f_number - s_number)
elif operator == operation[2]:
    print(f_number * s_number)
elif operator == operation[5]:
    print(f_number ** s_number)
else:
    if s_number != 0:
        if operator == operation[3]:
            print(f_number / s_number)
        elif operator == operation[6]:
            print(f_number // s_number)
        elif operator == operation[4]:
            print(f_number % s_number)
    else:
        print('Division by 0!')
