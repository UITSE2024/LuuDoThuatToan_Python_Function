
def Tinh(nn, xx):
    s = 0
    t = 1
    m = 0
    i = 1
    dau = -1
    while(i<=nn):
        t = t*xx
        m = m+i
        s = s + dau*t/m
        i = i+1
        dau = -dau
    return s

def main():
    n = int(input("Nhap n: "))
    x = float(input("Nhap x: "))
    print(Tinh(n, x))

if __name__=="__main__":
    main()