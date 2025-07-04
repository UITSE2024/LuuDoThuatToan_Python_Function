def tinhBieuThuc(xx):
    f = 0
    if xx >= 5:
        f = 2 * xx * xx + 5 * xx + 9
    else: 
        f = -2 * xx * xx + 4 * xx - 9

    return f

def main():
    x = int(input("Nhap vao gia tri cua x: "))

    f = tinhBieuThuc(x)

    print("Gia tri cua bieu thuc: {}".format(f))

if __name__ == "__main__":
    main()

