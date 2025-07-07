
def TongUocSo(nn):
    s = 0
    i = 1
    while(i<=nn):
        if(nn%i==0):
            s = s+i
        i = i + 1
    return s

def main():
    n = int(input("Nhap n: "))
    print("Tong cac uoc so: ", TongUocSo(n))

if __name__ == "__main__":
    main()
