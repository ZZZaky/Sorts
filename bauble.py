from output import Output

def Bauble_sort(array):
    count_if = 0
    count_change_main = 0
    count_change_temp = 0

    changes = True
    count = 0

    while(changes):
        changes = False
        count += 1
        for i in range(len(array) - count):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                count_change_main += 2
                changes = True
            count_if += 1

    Output(count_if, count_change_main, count_change_temp)