def rearrange(array):
    a=array
    pos=[]
    neg=[]
    
    for i in range(1,len(a)):
        if a[i]>=0:
            pos.append(a[i])
        else:
            neg.append(a[i])
    for i in range(1,len(pos)):
        a[2*i]=pos[i]
    for i in range(len(neg)):
        a[2*i+1]=neg[i]
    
    return a
a = [1, 2, -4, -5]
ans = rearrange(array)

for i in range(len(ans)):
    print(ans[i], end=" ")