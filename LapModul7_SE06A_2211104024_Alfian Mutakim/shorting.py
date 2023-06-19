import timeit
# Ascending

# print ("Ascending")
# print("")

# # insertion sort
# def insertion_sort(array):
#     start = timeit.default_timer()
#     for i in range (1, len(array)):
#         item = array [i]
#         j = i-1

#         while j >= 0 and array [j] <= item:
#             array[j + 1] = array[j]
#             j -= 1

#         array[j + 1]= item
       
#     stop = timeit.default_timer()
#     print(f"insertion sort successful! Elapsed time: + {stop - start} ")
#     return array

# list_1 = [2,9,5,99,65,4,22,90]
# print(f"Bifore : {list_1}")
# insertion_sort(list_1)
# print(f"After : {list_1}")


# bubble sort
def bubble_sort(array):
    start = timeit.default_timer()
    for i in range (len(array)):
        for j in range (len(array)-i-1):
            if array [j] < array[j+1]:
                array[j], array [j+1] = array [j+1], array[j]
       

    stop = timeit.default_timer()
    print(f"bubble sort successful! Elapsed time: + {stop - start} ")
    return array

list_1 = [2,9,5,99,65,4,22,90]
print(f"Bifore : {list_1}")
bubble_sort(list_1)
print(f"After : {list_1}")

# selection sort

def selection_sort(arr):
    start = timeit.default_timer()
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] > arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    stop = timeit.default_timer()
    print(f"Selection sort successful! Elapsed time: {stop - start} seconds")
    return arr

list_1 = [90, 34, 57, 32, 4, 1]
print(f"Before: {list_1}")
sorted_list = selection_sort(list_1.copy())
print(f"After: {sorted_list}")
