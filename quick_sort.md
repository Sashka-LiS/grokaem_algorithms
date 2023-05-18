# Сортировка выбором
- работает __быстрее__ сортировки выбором

```python
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        support_element = array[0]
        less = [i for i in array[1:] if i < support_element]
        greater = [i for i in array[1:] if i > support_element]
        return quicksort(less) + [support_element] + quicksort(greater)
```