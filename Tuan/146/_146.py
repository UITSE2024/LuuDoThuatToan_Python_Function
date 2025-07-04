def Nhap():
    nn = int(input("Nhap n = "))
    return nn

def TimDaoNguoc(nn):
    dn = 0
    t = nn
    while t != 0:
        dv = t % 10
        dn = dn * 10 + dv
        t = t // 10
    return dn

def main():
    n = Nhap()
    dn = TimDaoNguoc(n)
    if dn == n:
        print("La DX")
    else:
        print("Ko DX")

if __name__ == "__main__":
    main()