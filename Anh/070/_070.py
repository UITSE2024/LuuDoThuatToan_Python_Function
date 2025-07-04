def tongluythuachan(xx,nn):
    s = 0
    t = 1
    i = 2
    while i <= 2*nn:
        t = t* xx * xx
        s += t
        i += 2
    return s


def main():
    x = float(input("Nhap x: "))
    n = int(input("Nhap n: "))
    print("Tong :", tongluythuachan(x,n))

if __name__ == "__main__":
    main()


