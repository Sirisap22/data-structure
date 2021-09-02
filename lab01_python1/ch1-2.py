print(" *** Wind classification ***")
speed = float(input('Enter wind speed (km/h) : '))
rank = None
if (speed < 52):
    rank = 'Breeze'
elif (speed >= 52 and speed < 56):
    rank = 'Depression'
elif (speed >= 56 and speed < 102):
    rank = 'Tropical Storm'
elif (speed >= 102 and speed < 209):
    rank = 'Typhoon'
else:
    rank = 'Super Typhoon'
print(f'Wind classification is {rank}.')