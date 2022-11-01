def fib(n):
    i,j,tmp=0,1,0
    while(i<=n):
        print(i)
        tmp=j
        j=i+j
        i=tmp
fib(10)
