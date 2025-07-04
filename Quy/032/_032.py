def Tong(n):
    s = 0
    i = 1
    while (i <= n):
        s = s + 1 / (i * (i + 1))
        i = i + 1
    return s

def main():
    n = int(input("Nhap n: "))
    print("Tong la: ", Tong(n))

if __name__ == "__main__":
    main()