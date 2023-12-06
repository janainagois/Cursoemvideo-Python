import math
print(f'The value of pi is aproximately {math.pi:.3f}.')
table = {'Sjoerd': 4127, 'Jack': 4098 , 'Dcab': 76780}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))

animal = 'égua'
print(f'Meu celeiro tem {animal}')
print(f'Meu celeiro tem{animal!r}.')

bugs = 'roaches'
count = 13
area = 'living room'
print(f'debugging {bugs=} {count=} {area=}')

print('We are the {} my {}'.format('champion', 'friend'))

print('This {food} is {adjective}'.format(food='beans', adjective='great'))

print('The story of {0}, {1}, and {other}'.format('ian', 'amora', other = 'tie'))

for x in range (1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x , x*x, x*x*x))

print('The value of pi is approximaely %5.3f.'%math.pi)