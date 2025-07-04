def Tinh(xx, nn):
    s = 0
    t = 1
    m = 1
    i = 1
    dau = -1
    while i <= nn:
        t = t * xx
        m = m * i
        s = s + dau*t / m
        i = i + 1
        dau = -dau
    return s

def main():
    x = float(input("Nhap x: "))
    n = int(input("Nhap n: "))
    print("S(x,n) =", Tinh(x,n))

if __name__ == "__main__":
    main()

