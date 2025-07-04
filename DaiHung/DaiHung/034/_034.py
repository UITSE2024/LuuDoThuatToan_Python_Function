def Nhap():
    n = int(input("Nhap n: "))
    return n

def tinhTong(n):
    s = 0
    i = 1

    while i <= 2 * n + 1:
        s = s + (i / (i + 1))
        i = i + 2
    return s

def Xuat(s):
    print(f"Tong S = {s:.2f}")

def main():
    n = Nhap()
    s = tinhTong(n)
    Xuat(s)

if __name__ == "__main__":
    main()
