def Nhap():
    xx = float(input("Nhap x: "))
    return xx

def tinhGiaTri(xx):
    if (xx >= 0):
        if (xx <= 1):
            return 5 * xx - 7
        else:
            return 2 * xx ** 3 + 5 * xx ** 2 - 8 * xx + 3
    else:
        return -2 * xx ** 3 + 6 * xx + 9

def Xuat(xx, ff):
    print(f"Gia tri f({xx}) = {ff}")

def main():
    x = Nhap()
    f = tinhGiaTri(x)
    Xuat(x, f)

if __name__ == "__main__":
    main()
