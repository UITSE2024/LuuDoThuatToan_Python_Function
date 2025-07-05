def Nhap():
    x = int(input())
    n = int(input())
    return x, n
def TichLienTiepX(nn, xx):
    t = xx
    i = 1
    while(i <= nn):
        t*=(xx+i)
        i+=1
    return t
def main():
    x, n = Nhap()
    print(TichLienTiepX(n, x))
if __name__ == "__main__":
    main()
