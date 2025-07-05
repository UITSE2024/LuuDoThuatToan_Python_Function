def Nhap():
    nn = int(input("Nhap n: "))
    return nn

def tinhTichCacChuSo(nn):
    tich = 1
    t = nn

    while t != 0:
        dv = t % 10
        tich = tich * dv
        t = t // 10
    
    return tich

def Xuat(nn, tich):
    print(f"Tich cac chu so cua {nn} la {tich}")

def main():
    n = Nhap()
    tich = tinhTichCacChuSo(n)
    Xuat(n, tich)

if __name__ == "__main__":
    main()