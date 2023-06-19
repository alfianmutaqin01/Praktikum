print("indeks prestasi Semester (IPS)")
# bubble sort
def bubble_sort(array):
    for i in range (len(array)):
        for j in range (len(array)-i-1):
            if array [j] < array[j+1]:
                array[j], array [j+1] = array [j+1], array[j]
       
    return array

list_1 = [3.8,2.9,3.3,4.0,2.7]
print(f"list sebelum diurutkan : {list_1}")
bubble_sort(list_1)
print(f"list setelah diurutkan : {list_1}")