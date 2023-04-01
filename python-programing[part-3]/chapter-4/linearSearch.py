# python3 chapter-4/linearSearch.py

def linear_search(L, X):
    n = len(L)
    i = 0

    while i < n:
        if L[i] == x:
            return i
        i += 1
    i = -1
    return i

def linear_search(L, x):
    n = len(L)

    for i in range(n):
        if L[i] == x:
            return i
    
    return -1