# python3 chapter-8/exr.py

def print_number(n):
    if n == 0:
        return 
    
    # print(n)
    print_number(n-1)
    print(n)

if __name__ == '__main__':
    print_number(5)