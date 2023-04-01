# python3 chapter-4/binarySearch.py
# pytest chapter-4/binarySearch.py

def binary_search(L, x):
    left, right = 0, len(L) - 1

    while left <= right:
        mid = int((left + right) / 2)

        if L[mid] == x:
            return mid
        
        if L[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return mid

if __name__ == "__main__":
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for x in range(1, 11):
        position = binary_search(L, x)

        if position == -1:
            if x in L:
                print(x, 'is in L, but function return -1')
            else:
                print(x, 'not in list')
        else:
            if L[position] == x:
                print(x, 'found in correct position.')
            else :
                print('binary search returned', position, 'for',  x, 'which is incorrect')
    print('program terminated')