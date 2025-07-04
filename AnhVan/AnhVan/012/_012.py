def Tinh(xx):
    x2 = xx * xx
    x4 = x2 * x2
    return x4 * x2

def main():
    x = float(input("Nhap x: "))
    print("x^6 =", Tinh(x))

if __name__ == "__main__":
    main()

