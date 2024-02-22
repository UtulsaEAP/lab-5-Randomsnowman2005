# Mohamad Ali Fakhoury Thurs @2pm
def fibonacci(n):
    if n == 0:
       return (0)
    elif n ==1:
       return (1)
    elif n < 0:
        return(-1)
    else:
       


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')