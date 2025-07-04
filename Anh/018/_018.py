def tinhx12(xx):
    x2=xx * xx
    x4= x2 * x2
    x8= x4 * x4
    x12= x8 * x4
    return x12

def main():
    x= float(input("Nhap x: "))
    print("x^12 =", tinhx12(x))

if __name__ == "__main__":
    main()

