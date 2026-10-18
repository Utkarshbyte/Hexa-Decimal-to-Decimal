b=eval(input("Input a Hexa-Decimal Integer: "))
if "." in str(b):
    a=str(b).split(".")
    d=a[0][::-1]
    f=a[1][::-1]
    s1=0
    s2=0
    for i in range(len(d)):
        s1=s1+(int(d[i])*(16**i))
    for j in range(-1,-len(f)-1,-1):
        s2=s2+(int(f[j])*(16**j))
        print(s1+s2)
else:
    d=(str(b))[::-1]
    s=0
    for i in range(len(d)):
        s=s+(int(d[i])*(16**i))
    print(s)
