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