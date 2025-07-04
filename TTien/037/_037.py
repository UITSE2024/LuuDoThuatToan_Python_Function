
def Tinh(nn):
    s = 0
    i = 1
    while(i<=nn):
        s = s + i**3
        i+=1
    return s

def main():
    n = int(input("Nhap n: "))
    print(Tinh(n))

if __name__=="__main__":
    main()


