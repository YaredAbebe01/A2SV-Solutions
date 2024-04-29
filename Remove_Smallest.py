t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    if len(li)==1:
        ans.append("YES")
    sor=sorted(li)
    for i in range(1,len(sor)):
        D=sor[1]-sor[0]
        if D<=1:
            sor.remove(sor[0])
            if len(sor)==1:
                ans.append("YES")
                break
        else:
            ans.append("NO")
            break
for i in ans:
    print(i)
