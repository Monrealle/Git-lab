def quik_sort(array):
    
    if len(array) <= 1:
        return array # массив уже отсортирован
    
    else:
        pivot = array[len(array) // 2] # Середина в качестве опорного элемента
        left = [x for x in array if x < pivot]
        right = [x for x in array if x > pivot]
        middle = [x for x in array if x == pivot]

        return quik_sort(left) + middle + quik_sort(right)

# Проверка     
arr = [15, 6, 7, 9, 14, 1, 8] 
sorted_arr = quik_sort(arr)
print("Отсортированный массив: ", sorted_arr)  