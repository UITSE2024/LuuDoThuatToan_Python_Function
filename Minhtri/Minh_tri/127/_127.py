def Nhap():
    a=int(input("Nhap a: "))
    b=int(input("Nhap b: "))
    return a,b
def Min(a,b):
    lc=a
    if(lc>b):
        lc=b
    return lc
def main():
    a,b=Nhap()
    print("Min: ", Min(a,b))
if __name__ == "__main__":
    main()

