def Tong(xx, nn):
    s = xx
    t = xx
    i = 3
    while (i <= 2 * nn + 1):
        t = t * xx * xx
        s = s + t
        i = i + 2
    return s

def main():
    x = float(input("Nhap x: "))
    n = int(input("Nhap n: "))
    print("Tong la: ", Tong(x, n))

if __name__ == "__main__":
    main()