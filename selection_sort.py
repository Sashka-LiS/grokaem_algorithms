def find_smallest(arr):
    "функция для поиска наименьшего элемента массива"
    smallest = arr[0] # для хранения наименьшего значения
    smallest_index = 0 # для хранения индекса наименьшего значения
    for _ in range(1, len(arr)):
        if arr[_] < smallest:
            smallest = arr[_]
            smallest_index = _
    return smallest_index


def selection_sort(arr):
    "функция сортировки выбором"
    new_arr = []
    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

my_arr = [9, 6, 1, 4, 7, 2, 8]

print(selection_sort(my_arr))