from math import sin
def tongsinluythua(xx,nn):
    s = 0
    t = 1
    i = 1
    while i <= nn:
        t = t* xx
        s += sin(t)
        i += 1
    return s


def main():
    x = float(input("Nhap x: "))
    n = int(input("Nhap n: "))
    print("Tong :", tongsinluythua(x,n))

if __name__ == "__main__":
    main()



