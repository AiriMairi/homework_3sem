import random

if __name__ == '__main__':
    a = 10
    arr = []
    for i in range(a):
        arr.append(random.randint(1, 99))
    print(arr)
    for i in range(a-1):
        for j in range(a-i-1):
            if arr[j] > arr[j+1]:
                arr[j] = arr[j+1]
                arr[j+1] = arr[j]
    print(arr)


