# linear_search

def linear_search (keyword, data):
    for i in range(len(data)):
        if str(data[i]).lower() == keyword.lower ():
            print(f"keyword {keyword} has found at index {i}")
            return i
    print(f"keyword {keyword} not found ")
    return -1

data = [23, 4, 5, 90, 18, 45]
keyword = input("input keyword: ")
linear_search(keyword, data)


# binary_search

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