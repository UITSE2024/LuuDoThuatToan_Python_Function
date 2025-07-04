def tinhX14(xx):
    x2 = xx * xx
    x4 = x2 * x2
    x6 = x4 * x2
    x8 = x4 * x4
    x14 = x6 * x8
    return x14

def main():
    x = int(input("Nhap vao gia tri x: "))
    x14 = tinhX14(x)

    print("Gia tri cua x14 = {}".format(x14))

if __name__ == "__main__":
    main()
