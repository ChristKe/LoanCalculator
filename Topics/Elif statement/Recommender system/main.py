age = input()
limit = [16, 25, 40, 60]
if int(age) <= limit[0]:
    print('Lion King')
elif int(age) <= limit[1]:
    print('Trainspotting')
elif int(age) <= limit[2]:
    print('Matrix')
elif int(age) <= limit[3]:
    print('Pulp Fiction')
else:
    print("Breakfast at Tiffany's")