from math import sqrt
def tongluythuacan(nn):
    s = 0
    t = 1
    i = 1
    while i <= nn:
        t = t*i
        s = sqrt(s + t)
        i += 1
    return s


def main():
    n = int(input("Nhap n: "))
    print("Tong :", tongluythuacan(n))

if __name__ == "__main__":
    main()



