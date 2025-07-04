from math import sqrt

def tinhBieuThuc(nn):
    s = 0
    for i in range(1, nn + 1):
        s += 1 / ((i + 1) * sqrt(i) + i * sqrt(i + 1))

    return s

def main():
    n = int(input("Nhap vao gia tri cua n: "))
    s = tinhBieuThuc(n)

    print("Gia tri cua bieu thuc s: {:.2f}".format(s))

if __name__ == "__main__":
    main()

