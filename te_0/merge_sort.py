ls = [5,2,4,4,8]
def merge_sort(ls1,p,q):
    if p<q:
        k = int((p + q) / 2)
        merge_sort(ls1,p,k)
        merge_sort(ls1,k+1,q)
        merge_ls(ls1,p,k,q)
def merge_ls(ls1,p,k,q):
    i,j = 0,0
    L = ls1[p:k+1].copy()  #这里就是列表与数组的不同之处，列表的区间右端点是不引用的
    R = ls1[k+1:q+1].copy()
    print("p:{} k:{} q:{}".format(p,k,q))
    for g in range(p, q+1):
        if len(L) > i and len(R) > j:
            if L[i] >= R[j]:
                ls1[g] = R[j]
                j = j+1
            else:
                ls1[g] = L[i]
                i = i+1
        elif i == len(L):
            print("g:{} j:{}".format(g,j))
            ls1[g] = R[j]
            j = j+1
        else:
            ls1[g] = L[i]
            i = i+1
print(ls)
merge_sort(ls,0,len(ls)-1)
print(ls)