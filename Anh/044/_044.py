def tongnghichdao4(nn):
    s = 0
    i = 1
    while i <= nn:
        s += 1/(i*(i + 1)*(i + 2)*(i + 3))
        i += 1
    return s


def main():
    n= int(input("Nhap n: "))
    print("Tong :", tongnghichdao4(n))

if __name__ == "__main__":
    main()
