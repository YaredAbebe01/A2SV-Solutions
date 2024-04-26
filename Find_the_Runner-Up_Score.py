if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    u = []
    for l in arr:
        if l not in u:
            u.append(l)
u.sort()
print(u[len(u)-2]) 
