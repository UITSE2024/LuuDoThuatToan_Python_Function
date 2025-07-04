def Tinh(nn):
    at = 2
    i = 2
    while(i <= nn):
        ahh = (-9 * at - 24) / (5 * at + 13)
        i += 1
        at = ahh
    return at

def main():
    n = int(input("Nhap n: "))
    
    print("Ket qua: ", Tinh(n))

if __name__ == "__main__":
    main()

