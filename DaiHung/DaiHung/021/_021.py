def Nhap():
    x = int(input("Nhap x: "))
    return x

def tinhX15(x):
    x2 = x * x
    x4 = x2 * x2
    x8 = x4 * x4
    x16 = x8 * x8
    x15 = x16 // x  
    return x15

def main():
    x = Nhap()
    x15 = tinhX15(x)
    print(f"x^15 = {x15}")

if __name__ == "__main__":
    main()
