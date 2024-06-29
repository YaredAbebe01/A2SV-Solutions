if __name__ == '__main__':
    N = int(input())
    li = []
    for _ in range(N):
        com = input().split()
        if com[0] == 'insert':
            i = int(com[1])
            e = int(com[2])
            li.insert(i, e)
        elif com[0] == 'print':
            print(li)
        elif com[0] == 'remove':
            e = int(com[1])
            li.remove(e)
        elif com[0] == 'append':
            e = int(com[1])
            li.append(e)
        elif com[0] == 'sort':
            li.sort()
        elif com[0] == 'pop':
            li.pop()
        elif com[0] == 'reverse':
            li.reverse()
