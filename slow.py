from random import randint


def Slow_sort(array):
    count_if = 0
    count_change_main = 0
    count_change_temp = 0

    while True:
        done = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                count_if += 1
                done = False
        
        if done: 
            count_if += 1
            break
        else: 
            for i in range(len(array) - 1):
                rand = randint(0, len(array) - 1)
                array[i], array[rand] = array[rand], array[i]
                count_change_main += 2
    
    return {'comparsion': int(count_if), 'change in main array': int(count_change_main), 'change in temporary array': int(count_change_temp)}
