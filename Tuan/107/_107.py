from math import pi

def Nhap():
    xx = int(input("Nhap x = "))
    return xx

def Tinh(xx):
    s = 1
    t = 1
    m = 1
    dau = -1
    e = 1
    i = 2
    epsilon = 1e-6
    while e >= epsilon:
        t = t * xx * xx
        m = m * (i - 1) * i
        e = t / m
        s = s + dau * e
        dau = -dau
        i = i + 2
    return s

def main():
    x = Nhap()
    print("Ket qua:", Tinh(x * pi / 180))

if __name__ == "__main__":
    main()