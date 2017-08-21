def multiply(x,y):
    if len(str(x))==1 or len(str(y))==1:
        return x*y

    n=max(len(str(x)),len(str(y)))
    mid=n//2
 
    a = x//(10**mid)
    b = x%(10**mid)
    c = y//(10**mid)
    d = y%(10**mid)
    ac=multiply(a,c)
    bd=multiply(b,d)
    sum_ab_cd=multiply((a+b),(c+d))
    return (10**(2*mid)*ac+10**(mid)*(sum_ab_cd-ac-bd)+bd)

res=multiply(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627)
print(int(res))

 