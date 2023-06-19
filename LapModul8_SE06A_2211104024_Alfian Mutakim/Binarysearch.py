# def bubble_sort(data):
#     for i in range(len(data)):
#         for j in range(len(data) -i -1):
#             if data[j] > data [j+1]:
#                 data[j], data[j+1] = data[j], data[j+1]
#     return data

# def binary_search(keywoard, data):
#             sorted_data = bubble_sort(data)
#             print(f"Data (sorted) = {sorted_data}")
#             left = 0
#             right = len(sorted_data)-1
#             while left <= right:
#                 mid = (left + right) // 2
#                 str_data = str(sorted_data[mid]).lower()
#                 if str_data > keyword.lower():
#                     right = mid - 1
#                 elif str_data < keyword.lower():
#                     left = mid + 1
#                 else:
#                     print(f"Keyword '{keyword}' has found at index {mid}")
#                     return mid
                
#             print(f"keyword {keyword} not found")
#             return -1
           
# data = [23,3,4,78,9,10,32]
# keyword = input("input keyword: ")
# binary_search(keyword, data)

def bubble_sort(keyword,data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return binary_search(keyword, data)

def binary_search(keyword, data):

    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if str(data[mid]).lower() > keyword.lower():
            right = mid - 1           
        elif str(data[mid]).lower() < keyword.lower():
            left = mid + 1
        else:
            print(data)
            print(f"Keyword '{keyword}' has been found at index {mid}")
            return mid
        
    print(f"Keyword '{keyword}' not found")
    return -1

data = [23, 3, 4, 78, 9, 10, 32]
keyword = input("Input keyword: ")
bubble_sort(keyword, data)

