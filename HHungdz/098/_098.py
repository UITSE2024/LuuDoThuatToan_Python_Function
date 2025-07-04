

def tinhBieuThuc(nn):
    s = 0
    for i in range(2, nn + 1):
        s  = (i + s) ** (1/i)

    return s

def main():
    n = int(input("Nhap vao gia tri cua n: "))
    s = tinhBieuThuc(n)

    print("Gia tri cua bieu thuc s: {:.2f}".format(s))

if __name__ == "__main__":
    main()



