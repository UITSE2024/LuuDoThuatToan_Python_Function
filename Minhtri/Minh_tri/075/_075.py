def Nhap():
    x=int(input("Nhap x: "))
    n=int(input("Nhap n: "))
    return x, n
def Tinhtong(x,n):
    s=1
    t=1
    m=1
    i=2
    while(i<=2*n):
        t=t*x*x
        m=m*i*(i-1)
        s=s+t/m
        i+=2
    return s
def main():
    x,n=Nhap()
    print("Tong: ", Tinhtong(x,n))

if __name__=="__main__":
    main()