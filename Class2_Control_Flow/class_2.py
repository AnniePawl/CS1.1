# LISTS
clothes = ['shoes', 'belt', 'shirt']
# switch belt to necklace
clothes[1] = 'necklace'
print(clothes)
# replace shirt with pants
clothes[-1] = 'pants'
print(clothes)
clothes.append('hat')
print(clothes)


# IF-ELSE
# is hat in our list?
if 'hat' in clothes:
    print('wearing a hat')
# is the first item pants?
if clothes[0] is 'socks':
    print('socks are first')
elif clothes[0] == 'shoes':
    print('shoes are first')

# LOOPS
# For loops interate over a list
clothes = []
for item in clothes:
    print('shoes')
# While loops run forever as long as a condition is true
while len(clothes) >=0:
    print(clothes[0])
