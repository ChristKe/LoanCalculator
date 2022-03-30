x = input()
y = input()
Zero = 0
if float(x) == Zero and float(y) == Zero:
    print("It's the origin!")
elif float(x) == Zero or float(y) == Zero:
    print('One of the coordinates is equal to zero!')

if float(x) > Zero and (float(y) > Zero):
    print('I')
elif float(x) > Zero and float(y) < Zero:
    print('IV')
elif float(x) < Zero and (float(y) > Zero):
    print('II')
elif float(x) < Zero and (float(y) < Zero):
    print('III')
