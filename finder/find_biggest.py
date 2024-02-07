'''
Метод для нахождения наибольшего значения в списке.
Применяется для сортировок по убыванию, например.
'''


def find_biggest(array):
    """
    Находит самое большое значение в списке
    :param array: принимает список.
    :return: Возвращает индекс значения в списке.
    """
    biggest_number = array[0]
    biggest_index = 0
    for i in range(1, len(array)):
        if array[i] > biggest_number:
            biggest_number = array[i]
            biggest_index = i
    return biggest_index
