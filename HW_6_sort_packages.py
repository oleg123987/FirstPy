width = 100
height = 100
length = 100
mass = 19

# if width * height * length > 1000000:
#     print('pakage is bulky')
#     bulky = True
#
# elif mass > 20:
#     print('pakage is heavy')
#     heavy = True

if width * height * length <= 1000000 and mass <= 20:
    print('STANDART')

elif width * height * length >= 1000000 and mass >= 20:
    print('REJECTED')

elif width * height * length >= 1000000 or mass >= 20:
    print('SPECIAL')