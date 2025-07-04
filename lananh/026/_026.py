def main():
    a = float(input("Nhap a: "))
    b = float (input("Nhap b: "))
    a = a + b
    b = a - b
    a = a - b
    print("a = ", a)
    print("b = ", b)
    return 0

if __name__ == "__main__":
    main()
