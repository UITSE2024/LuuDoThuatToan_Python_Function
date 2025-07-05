def LietKe(xx, yy):
    n = xx
    while (n <= yy):
        dk1 = ((n % 4 == 0) and (n % 100 != 0))
        dk2 = (n % 400 == 0)
        if (dk1 or dk2):
            print(n, end = " ")
        n = n + 1

def main():
    x = int(input("Nhap x: "))
    y = int(input("Nhap y: "))
    LietKe(x, y)

if __name__ == "__main__":
    main()