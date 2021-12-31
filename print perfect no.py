def perfect(i):
    i=1
    while i<=1000:
        j=1
        sum=0
        while j<i:
            if i%j==0:
                sum=sum+j
            j=j+1
        if sum==i:
            print(i,"perfect no")
        else:
            print(i)
        i=i+1
perfect(1000)
