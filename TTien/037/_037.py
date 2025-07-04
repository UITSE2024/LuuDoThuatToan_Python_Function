
def Nhap():
    n = int(input("Nhap n: "))
    return n

def Tinh(n):
    s = 0
    i = 1
    while(i<=n):
        s = s + i**3
        i+=1
    return s

def main():
    n = Nhap();
    print(Tinh(n))

if __name__=="__main__":
    main()


