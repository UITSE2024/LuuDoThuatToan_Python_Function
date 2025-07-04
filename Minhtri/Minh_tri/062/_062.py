def Tinhtong(n):
    s=0
    t=n
    while(t!=0):
        dv=t%10
        if(dv%2==0):
            s+=dv
        t=t//10
    return s
def main():
    n=int(input("Nhap n: "))
    print("Tong: ", Tinhtong(n))
if __name__=="__main__":
    main()