def Nhap():
    nn = int(input("Nhap n: "))
    return nn

def tinhTong(nn):
    s = 0
    i = 1

    while i <= 2 * nn + 1:
        s = s + (i / (i + 1))
        i = i + 2
    return s

def Xuat(ss):
    print(f"Tong S = {ss:.2f}")

def main():
    n = Nhap()
    s = tinhTong(n)
    Xuat(s)

if __name__ == "__main__":
    main()
