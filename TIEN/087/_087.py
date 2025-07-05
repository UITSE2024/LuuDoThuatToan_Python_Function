
from re import X

def Nhap():
    x = int(input())
    n = int(input())
    return x, n
def TichPhanSo(xx, nn):
    s = 0
    t = 1
    m = 1
    i = 1
    while(i <= nn):
        t *= xx
        m = m*i
        s+=t/m
        i+=1
    return s
def main():
    x, n = Nhap()
    print(TichPhanSo(x, n))
if __name__ == "__main__":
    main()


