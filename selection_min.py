from output import Output

def Selection_min_sort(array):
    count_if = 0
    count_change_main = 0
    count_change_temp = 0

    for i in range(len(array) - 1):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                count_if += 1
                min = j
        
        array[i], array[min] = array[min], array[i]
        count_change_main += 2
    
    Output(count_if, count_change_main, count_change_temp)