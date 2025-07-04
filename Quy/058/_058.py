def TongChuSo(n):
    s = 0
    t = n
    while (t != 0):
        dv = t % 10
        s = s + dv
        t = t // 10
    return s

def main():
    n = int(input("Nhap n: "))
    print("Tong chu so la: ", TongChuSo(n))

if __name__ == "__main__":
    main()