if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    max = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] < max:
            print( arr[i])
            break
