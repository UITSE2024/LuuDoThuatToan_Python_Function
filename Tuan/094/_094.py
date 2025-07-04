from math import sqrt

def Nhap():
    nn = int(input("Nhap n = "))
    return nn

def Tinh(nn):
    s = 0
    i = 1
    while i <= nn:
        s = sqrt(i + s)
        i = i + 1
    return s

def main():
    n = Nhap()
    print("Ket qua:", Tinh(n))

if __name__ == "__main__":
    main()