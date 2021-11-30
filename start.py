from random import randint


def Bauble(array):
    from bauble import Bauble_sort
    return Bauble_sort(array)

def Tree(array):
    from tree import Tree_sort
    return Tree_sort(array)

def Slow(array):
    from slow import Slow_sort
    return Slow_sort(array)


sorts = {'1': 'Bauble', '2': 'Tree', '3': 'Slow'}
sorts_import = {'Bauble': Bauble, 'Tree': Tree, 'Slow': Slow}

while True:
    print('Select the number of sort method you want to use or type q to quit: ', sorts)
    method = input()
    if method == 'q': break
    else: method = sorts[method]

    size = int(input('Set the size of array: '))

    print('Initializing %s method on array...\n' % (method))

    arr = []

    for i in range(size):
        arr.append(randint(0, size*10))


    print(sorts_import[method](arr), '\n')