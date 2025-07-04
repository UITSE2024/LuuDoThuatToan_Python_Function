 
def UCLN(a, b):
    m = abs(a)
    n = abs(b)

    while m * n != 0:
        if m > n:
            m -= n
        else: 
            n -= m

    return m + n 


def BCNN(a, b):
    gcd = UCLN(a, b)
    return abs(a * b) / gcd 


def main():
    a = int(input("Nhap vao a: "))
    b = int(input("Nhap vao b: "))

    LCM = BCNN(a, b)

    print("Boi chung nho nhat {} va {}: {}".format(a, b, LCM))

if __name__ == "__main__":
    main()

