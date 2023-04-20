# Бинарный поиск работает только с отсортированным массивом.
# Бинарный поиск работает намного быстрее простого



def binary_search(list, item):
    low = 0 # нижняя граница массива для поиска 
    high = len(list) - 1 # верхняя граница списка для поиска
    while low <= high: # пока эта не сократиться до одного элемента...
        mid = int((low + high) / 2) # ...проверяем средний элемент
        guess = list[mid]
        if guess == item: # значение найдено
            return mid
        if guess > item: # много
            high = mid - 1
        else: # мало
            low = mid + 1
    return None # значение не существует


my_list = [4, 6, 7, 26, 54, 67, 100, 139, 202, 376]

print(binary_search(my_list, 67))
print(binary_search(my_list, 533))