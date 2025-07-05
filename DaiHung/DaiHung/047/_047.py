from math import sqrt

def Nhap():
    nn = int(input("Nhap n: "))
    return nn

def tinhTong(nn):
    s = 0
    i = 1

    while i <= nn:
        s = s + sqrt(1 + 1 / (i ** 2) + 1 / ((i + 1) ** 2))
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
