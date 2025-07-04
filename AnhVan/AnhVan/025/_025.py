def main():
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    print("Truoc hoan vi:")
    print("a =", a)
    print("b =", b)

    print("Sau hoan vi:")
    a, b = b, a
    print("a =", a)
    print("b =", b)

if __name__ == "__main__":
    main()

