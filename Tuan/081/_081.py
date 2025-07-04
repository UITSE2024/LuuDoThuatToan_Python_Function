def Nhap():
    xx = int(input("Nhap x = "))
    nn = int(input("Nhap n = "))
    return xx, nn

def Tinh(xx, nn):
    s = 0
    m = 1
    i = 0
    while i <= nn:
        m = m * (xx + i)
        s = s + 1 / m
        i = i + 1
    return s

def main():
    x, n = Nhap()
    print("Ket qua:", Tinh(x, n))

if __name__ == "__main__":
    main()