def Nhap():
    xx = int(input("Nhap x: "))
    nn = int(input("Nhap n: "))
    return xx, nn

def tinhTong(xx, nn):
    s = 0
    t = 1
    m = 0
    i = 1

    while i <= nn:
        t = t * xx
        m = m + i
        s = s + (t / m)
        i = i + 1

    return s

def Xuat(ss):
    print(f"Tong S = {ss:.2f}")

def main():
    x, n = Nhap()
    s = tinhTong(x, n)
    Xuat(s)

if __name__ == "__main__":
    main()
