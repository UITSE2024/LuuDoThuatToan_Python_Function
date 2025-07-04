def Nhap():
    nn = int(input("Nhap n: "))
    return nn

def tinhTong(nn):
    s = 0
    i = 1

    while i <= nn:
        s = (i + s) ** (1 / (i + 1))
        i = i + 1

    return s

def Xuat(ss):
    print(f"Tong S = {ss:.2f}")

def main():
    n = Nhap()
    s = tinhTong(n)
    Xuat(s)

if __name__ == "__main__":
    main()
