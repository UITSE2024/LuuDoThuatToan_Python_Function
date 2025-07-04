from math import sin

def Tong(xx, nn):
    s = 0
    t = xx
    i = 1
    while (i <= nn):
        t = sin(t)
        s = s + t
        i = i + 1
    return s

def main():
    x = float(input("Nhap x: "))
    n = int(input("Nhap n: "))
    print("Tong la: ", Tong(x, n))

if __name__ == "__main__":
    main()