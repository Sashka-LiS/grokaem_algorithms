# Каждая рекурсивная функция состоит из двух частей: БАЗОВЫЙ СЛУЧАЙ и РЕКУРСИВНЫЙ СЛУЧАЙ
# Когда вызывается функция из другой функции, вызывающая функция приостанавливается частично завершенном состоянии. Все значения переменных отсаются в памяти. Все вызовы функции остаются в стеке.
# Стек поддерживает две операции: ЗАНЕСЕНИЕ и ИЗВЛЕЧЕНИЕ элементов

def countdown(start: int):
    print(start)
    if start <= 1:
        print("End!")
    else:
        countdown(start - 1)
    

def sum(numbers: list):
    if len(numbers) <= 1:
        return numbers[0]
    else:
        return numbers[0] + sum(numbers[1:])
    

def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

print(count([1,3,2,5]))