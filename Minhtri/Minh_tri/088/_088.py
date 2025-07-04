def Tinhtong(n):
    s=0
    m=0
    i=1
    dau=1
    while (i<=n):
        m+=i
        s=s+dau/m
        i+=1
        dau=-dau
    return s
def main():
    n=int(input("Nhap n: "))
    print("Tong: ", Tinhtong(n))
if __name__=="__main__":
    main()