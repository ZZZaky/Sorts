from output import Output

def Selection_max_sort(array):
    count_if = 0
    count_change_main = 0
    count_change_temp = 0

    for i in reversed(range(1, len(array))):
        max = i
        
        for j in range(0, i):
            if array[j] > array[max]:
                count_if += 1
                max = j

        array[i], array[max] = array[max], array[i]
        count_change_main += 2
    
    Output(count_if, count_change_main, count_change_temp)