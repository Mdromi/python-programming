# python3 chapter-5/bubbleSort.py

def bubble_sort(L):
    n = len(L)
    count = 0

    for i in range(0, n):

        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                count += 1
        
        if count == 0:
            print('List already sorted')
            break
        print('Change List', L)
               

if __name__ == "__main__":
   
    L = [40, 80, 333, 5, 9, 111]
    L = [5, 9, 40, 80, 111, 333]
    print('Before sort', L)
    bubble_sort(L)
    print('After sort', L)

