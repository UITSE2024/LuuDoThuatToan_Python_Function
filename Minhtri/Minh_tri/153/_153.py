def Kiemtra(n):
    flag=1
    t=n
    while (t>1):
        du=t%5
        if(du!=0):
            flag=0
        t=t/5
    if (flag==1):
        print("La dang")
    else:
        print("Khong la dang")
def main():
    n=int(input("Nhap n: "))
    Kiemtra(n)
if __name__=="__main__":
    main()