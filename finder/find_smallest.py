'''
Метод для нахождения наименьшего значения в списке.
Применяется для сортировок по возрастанию, например.
'''


def find_smallest(array):
    """
    Находит самое маленькое значение в списке
    :param array: принимает список.
    :return: Возвращает индекс значения в списке.
    """
    smallest_number = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest_number:
            smallest_number = array[i]
            smallest_index = i
    return smallest_index

if __name__ == '__main__':
    test_array = [15, 6, 46, 87, 63, 65, 4876, 343, 8, 7, 345, 37, 3, 567, 74, 44, 3, 85]
    print(find_smallest(test_array))