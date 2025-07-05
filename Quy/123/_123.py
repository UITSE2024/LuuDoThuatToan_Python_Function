def Tinh(nn):
    if (nn == 1):
        return 2, 1
    at = 2
    bt = 1
    i = 2
    while (i <= nn):
        ahh = 3 * bt + 2 * at
        bhh = at + 3 * bt
        i = i + 1
        at = ahh
        bt = bhh
    return ahh, bhh

def main():
    n = int(input("Nhap n: "))
    print("An, Bn: ", Tinh(n))

if __name__ == "__main__":
    main()