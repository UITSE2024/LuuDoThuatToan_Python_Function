
def Nhap():
    xx = int(input("Nhap x = "))
    return xx

def Tinh(xx):
    x2 = xx * xx
    x4 = x2 * x2
    x8 = x4 * x4
    x9 = x8 * xx
    return x9

def main():
    x = Nhap()
    print("Ket qua: ", Tinh(x))

if __name__ == "__main__":
    main()
