# python3 chapter-13/margeSort.py
# pytest chapter-13/margeSort.py

def marge(a, b):
    marge_list = []

    len_a, len_b = len(a), len(b)
    index_a, index_b = 0, 0

    while index_a < len_a and index_b < len_b:
        if a[index_a] < b[index_b]:
            marge_list.append(a[index_a])
            index_a += 1
        else:
            marge_list.append(b[index_b])
            index_b += 1

    if index_a < len_a:
        marge_list.extend(a[index_a:])
    elif index_b < len_b:
        marge_list.extend(b[index_b:])
    
    return marge_list

def marge_sort(L):
    if len(L) <= 1:
        return L
    
    mid = len(L) // 2
    left = marge_sort(L[:mid])
    right = marge_sort(L[mid:])

    return marge(left, right)

if __name__ == '__main__':
    scenarios = [
        {'a': [1], 'b': [2], 'expected': [1, 2]},
        {'a': [2], 'b': [1], 'expected': [1, 2]},
        {'a': [], 'b': [1, 2], 'expected': [1, 2]},
        {'a': [1, 2], 'b': [], 'expected': [1, 2]},
        {'a': [1, 3, 5, 6], 'b': [2, 4, 7, 8], 'expected': [1, 2, 3, 4, 5, 6, 7, 8]},
        {'a': [1], 'b': [2, 3, 4], 'expected': [1, 2, 3, 4]}
    ]

    for item in scenarios:
        marge_list = marge(item['a'], item['b'])

        try:
            assert item['expected'] == marge_list
        except AssertionError:
            print('Output didnt match expected output')
            print('expected', item['expected'])
            print('got', marge_list)


    L = [[4, 7, 2, 3], [10], [10, 9, 8, 7, 6], [2, 3, 1], [1, 2], [2, 1]]

    for li in L:
        sorted_list = marge_sort(li)
        print('Original list', li)
        print('Sorted list', sorted_list)
        print()