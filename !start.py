from random import randint
from colorama import init, Fore, Back
from colorama.initialise import reset_all
init()

def Bauble(array):
    from bauble import Bauble_sort
    Bauble_sort(array)

def Tree(array):
    from tree import Tree_sort
    Tree_sort(array)

def Slow(array):
    from slow import Slow_sort
    Slow_sort(array)

def Selection_min(array):
    from selection_min import Selection_min_sort
    Selection_min_sort(array)

def Selection_max(array):
    from selection_max import Selection_max_sort
    Selection_max_sort(array)

def Insertion(array):
    from insertion import Insertion_sort
    Insertion_sort(array)

def Gnome(array):
    from gnome import Gnome_sort
    Gnome_sort(array)


sorts = {'1': 'Bauble', '2': 'Tree', '3': 'Selection on minimum', '4': 'Selection on maximum' , '5': 'Slow', '6': 'Insertion', '7': 'Gnome'}
sorts_import = {'Bauble': Bauble, 'Tree': Tree, 'Slow': Slow, 'Selection on minimum': Selection_min, 'Selection on maximum' : Selection_max, 'Insertion': Insertion, 'Gnome': Gnome}



while True:
    print(f"{Back.WHITE}{Fore.BLACK}Select the number of sort method you want to use or 'q' to quit:{Back.BLACK}{Fore.WHITE}\n", sorts)
    method = input()

    if method in sorts: method = sorts[method]
    elif method in sorts_import: pass
    elif method == 'q': break
    else: method = False

    if method:
        size = int(input(f'{Fore.WHITE}Set the size of array: '))

        print(f'Initializing {Fore.RED}%s{Fore.WHITE} method on array with a size of {Fore.RED}%s{Fore.WHITE}...' % (method, size))

        arr = []

        for i in range(size):
            arr.append(randint(0, size*10))


        sorts_import[method](arr)
        # print(arr)
        print('\n')