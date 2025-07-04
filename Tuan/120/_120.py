from math import sqrt

def Nhap():
    nn = int(input("Nhap n = "))
    return nn

def TinhAhh(nn):
    at = 2
    i = 2
    while i <= nn:
        ahh = 5 * at + sqrt(24 * at * at - 8)
        i = i + 1
        at = ahh
    return ahh

def main():
    n = Nhap()
    print("Ket qua:", TinhAhh(n))

if __name__ == "__main__":
    main()