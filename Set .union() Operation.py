# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    s1 = set(map(int, input().split()))
    m = int(input())
    s2 = set(map(int, input().split()))
    tot = s1 | s2
    print(len(tot))
