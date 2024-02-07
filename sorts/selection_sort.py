from finder.find_smallest import *
from finder.find_biggest import *

'''
Метод для сортировки выбором
'''


# Пример сортировки от меньшего к большему.
def selection_sort_min_max(array):
    new_array = []
    for i in range(len(array)):
        smallest_index = find_smallest(array)
        new_array.append(array.pop(smallest_index))
    return new_array


# Пример сортировки от большего к меньшему
def selection_sort_max_min(array):
    new_array = []
    for i in range(len(array)):
        biggest_index = find_biggest(array)
        new_array.append(array.pop(biggest_index))
    return new_array


if __name__ == '__main__':
    test_array = [15, 6, 46, 87, 63, 65, 4876, 343, 8, 7, 345, 37, 3, 567, 74, 44, 3, 85]
    print(selection_sort_min_max(test_array))
    test_array = [15, 6, 46, 87, 63, 65, 4876, 343, 8, 7, 345, 37, 3, 567, 74, 44, 3, 85]
    print(selection_sort_max_min(test_array))
