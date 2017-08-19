def merge_sort_and_count(arr):
    n=len(arr)
    if n==1:
        return 0,arr
    mid=n//2
    l_cn, left=merge_sort_and_count(arr[0:mid])
    r_cn, right=merge_sort_and_count(arr[mid:n])
    mas=list()
    cn=0
    while left and right:
        if left[0]<right[0]:
            mas.append(left.pop(0))
        else:
            mas.append(right.pop(0))
            cn=cn+len(left)
    mas.extend(right or left)
    return cn+l_cn+r_cn, mas
     
if __name__=='__main__':  
    f=open('C:\\Study\\Algorithms\\PA02\\IntegerArray.txt')
    arr=list(map(int,f.read().splitlines()))
    print(len(lst))
    cn, arr=merge_sort_and_count(arr)    
    print(cn)
