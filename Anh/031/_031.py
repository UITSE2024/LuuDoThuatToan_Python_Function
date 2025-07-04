def tongnghichdaole(nn):
    s = 0
    i = 1
    while i <= nn:
        s += 1/i
        i += 2
    return s


def main():
    n= int(input("Nhap n: "))
    print("Tong :", tongnghichdaole(n))

if __name__ == "__main__":
    main()
