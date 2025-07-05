def Tinhx13(xx):
    xx2 = xx * xx
    xx4 = xx2 * xx2
    xx5 = xx4 * xx
    xx8 = xx4 * xx4
    xx13 = xx8 * xx5
    return xx13

def main():
    x = float(input("Nhap x: "))
    print("x13: ", Tinhx13(x))

if __name__ == "__main__":
    main()