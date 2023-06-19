def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

list_1 = ["Zhafira", "Nirmala", "Aksara", "Nalendra", "Cakra", "Sastra", "Agni", "Bagas", "Jerome", "Kiara"]
print(f"Before: {list_1}")
sorted_list = selection_sort(list_1.copy())
print(f"After: {sorted_list}")