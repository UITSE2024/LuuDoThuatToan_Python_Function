def Nhap():
    nn = int(input("Nhap n = "))
    return nn

def Tinh(nn):
    t = 1
    i = 1
    while i <= nn:
        if nn % i == 0:
            t = t * i
        i = i + 2
    return t

def main():
    n = Nhap()
    print("Ket qua: ", Tinh(n))

if __name__ == "__main__":
    main()