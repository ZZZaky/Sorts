from random import randint
from output import Output

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
                rand = randint(i, len(array) - 1)
                array[i], array[rand] = array[rand], array[i]
                count_change_main += 2
    
    Output(count_if, count_change_main, count_change_temp)
