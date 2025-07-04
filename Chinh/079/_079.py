def Tinh(nn):
    s = 0
    t = 1
    i = 1
    while(i <= nn):
        t *= i
        s += i * t
        i += 1
    return s

def main():
    n = int(input("Nhap n: "))
    
    print("Ket qua: ", Tinh(n))

if __name__ == "__main__":
    main()
