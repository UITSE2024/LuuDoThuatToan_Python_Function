def Tinhsohang():
    at=-2
    tt=3
    pp=7
    i=2
    while(i<=n):
        tt*=3
        pp*=7
        ahh=5*at+2*tt-6*pp+12
        i+=1
        at=ahh
    return ahh
def main():
    n=int(input("Nhap n: "))
    print("So hang thu n")
if __name__=="__main__":
    main()
