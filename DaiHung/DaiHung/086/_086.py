def Nhap():
    xx = int(input("Nhap x: "))
    nn = int(input("Nhap n: "))
    return xx, nn

def tinhTong(xx, nn):
    s = 0
    t = 1
    i = 2
    dau = -1

    while i <= 2 * nn:
        t = t * xx * xx
        s = s + dau * t
        i = i + 2
        dau = -dau

    return s

def Xuat(ss):
    print(f"Tong S = {ss}")

def main():
    x, n = Nhap()
    s = tinhTong(x, n)
    Xuat(s)

if __name__ == "__main__":
    main()
