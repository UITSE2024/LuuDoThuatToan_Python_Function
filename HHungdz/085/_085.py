from math import sqrt

def tinhBieuThuc(xx, nn):
    s = 0
    t = 1
    dau = 1
    for i in range(1, nn + 1):
        t *= xx
        s += dau * t
        dau = -dau 

    return s

def main():
    x = int(input("Nhap vao gia tri cua x: "))
    n = int(input("Nhap vao gia tri cua n: "))
    s = tinhBieuThuc(x, n)

    print("Gia tri cua bieu thuc s: {:.2f}".format(s))

if __name__ == "__main__":
    main()



