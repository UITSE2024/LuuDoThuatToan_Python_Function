def Nhap():
    x=int(input("Nhap x: "))
    n=int(input("Nhap n: "))
    return x, n
def Luythua(x,n):
    t=1
    i=1
    while (i<=n):
        t*=x
        i+=1
    return t
def main():
    x, n = Nhap()
    print("Luy thua: ", Luythua(x,n))
if __name__ == "__main__":
    main()