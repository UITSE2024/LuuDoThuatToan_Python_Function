def tonguocbe(nn):
    s = 0
    i = 1
    while i < nn:
        if nn % i == 0:
            s += i
        i += 1
    return s


def main():
    n= int(input("Nhap n: "))
    print("Tong :", tonguocbe(n))

if __name__ == "__main__":
    main()

