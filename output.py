from colorama import init, Fore, Back
init()

def Output(comparisons, change_in_main_array, change_in_temp_array):
    print(f"{Fore.BLUE}Comparsion: {Fore.RED}%s{Fore.BLUE}\nChange in main array: {Fore.RED}%s{Fore.BLUE}\nChange in temporary array: {Fore.RED}%s{Fore.WHITE}" % (comparisons, change_in_main_array, change_in_temp_array))