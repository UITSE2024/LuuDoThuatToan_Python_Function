
def ChuSoDau(nn):
    dt=abs(nn)
    while(dt>=10):
        dt=dt//10
    return dt

def main():
    n = int(input("Nhap n: "))
    print("Chu so dau tien: ", ChuSoDau(n))

if __name__=="__main__":
    main()
