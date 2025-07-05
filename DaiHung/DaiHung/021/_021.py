def Nhap():
    xx = int(input("Nhap x: "))
    return xx

def tinhX15(xx):
    xx2 = xx * xx
    xx4 = xx2 * xx2
    xx8 = xx4 * xx4
    xx16 = xx8 * xx8
    xx15 = xx16 // xx  
    return xx15

def main():
    x = Nhap()
    x15 = tinhX15(x)
    print(f"x^15 = {x15}")

if __name__ == "__main__":
    main()
