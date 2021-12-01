from output import Output

def Insertion_sort(array):
    count_if = 0
    count_change_main = 0
    count_change_temp = 0

    for i in range(1, len(array)):
        cursor = array[i]
        position = i

        while position > 0 and array[position - 1] > cursor:
            count_if += 2
            array[position] = array[position - 1]
            count_change_main += 1
            position -= 1
        array[position] = cursor
        count_change_main += 1

    Output(count_if, count_change_main, count_change_temp)