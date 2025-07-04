from math import sqrt

def Tong(xx, nn):
    s = 0
    t = 1
    i = 1
    while (i <= nn):
        t = t * xx
        s = sqrt(t + s)
        i = i + 1
    return s

def main():
    x = float(input("Nhap x: "))
    n = int(input("Nhap n: "))
    print("Tong la: ", Tong(x, n))

if __name__ == "__main__":
    main()