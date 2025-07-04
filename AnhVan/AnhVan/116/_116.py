def TinhSoHang(nn):
    att = 1
    at = 2
    i = 2
    while i <= nn:
        ahh = 4*at + att
        i = i + 1
        att = at
        at = ahh
    return ahh

def main():
    n = int(input("Nhap n: "))
    print("So hang thu n cua day: ", TinhSoHang(n))

if __name__ == "__main__":
    main()

