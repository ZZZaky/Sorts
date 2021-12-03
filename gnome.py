from output import Output

def Gnome_sort(array):
    count_if = 0
    count_change_main = 0
    count_change_temp = 0

    i, j, size = 1, 2, len(array)

    while i < size:
        count_if += 1
        if array[i - 1] <= array[i]:
            i, j = j, j + 1
            count_if += 1
        else:
            array[i], array[i - 1] = array[i - 1], array[i]
            count_change_main += 2
            i -= 1

            if i == 0:
                count_if += 1
                i, j = j, j + 1
    
    Output(count_if, count_change_main, count_change_temp)
