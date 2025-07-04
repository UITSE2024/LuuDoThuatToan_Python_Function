
def Nhap():
    n = int(input("Nhap n: "))
    return n

def SoHangTram(nn):
    ht=(nn//100)%10
    return ht

def main():
    n = Nhap()
    print("Chu so hang tram: ", SoHangTram(n))

if __name__ == "__main__":
    main()

