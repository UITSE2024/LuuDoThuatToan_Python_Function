def Nhap():
    nn = int(input("Nhap n = "))
    return nn

def Tinh(nn):
    s = 0
    i = 0 
    while i <= nn:
        s = s + 1 / (i * (i + 1))
        i = i + 1
    return s

def main():
    n = Nhap()
    print("Ket qua: ", Tinh(n))

if __name__ == "__main__":
    main()
