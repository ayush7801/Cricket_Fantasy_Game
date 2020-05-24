#calculate points
def calc_points(a):
    print("in points")
    if a[1]!=0:
        p=(a[1])/2
        sr=(a[1]/a[2])*100
        if sr<100:
            if sr>=80:
                p=p+2
        else:
            p=p+4

        p=p+(a[3]*1)
        p=p+(a[4]*2)
        i=1
        b=a[1]
        while b>=50:
            p=p+(i*5)
            b=b-50
            i=i+1
    else:
        p=0
   
    p=p+(a[9]*10)
    p=p+(a[10]*10)
    p=p+(a[11]*10)

    p=p+(a[8]*10)
    if a[8]<5:
        if a[8]>=3:
            p=p+5
    else:
        p=p+10

    if a[7]==0:
        eco=0
    else:
        eco=a[7]/(a[5]/6)
        if eco>3.5 and eco<=4.5:
            p=p+4
        elif eco>2 and eco<=3.5:
            p=p+7
        elif eco<=2:
            p=p+10
    print(p)
    print(type(p))
    return p
    
    
