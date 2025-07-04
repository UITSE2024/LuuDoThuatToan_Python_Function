def TonTaiChan(nn):
    flag = 0
    t = nn
    while(t != 0): 
        dv = t % 10
        if(dv % 2 == 0):
            flag = 1
        t //= 10
    if(flag == 1):
        return True
    return False

def main():
    n = int(input("Nhap n: "))
    
    if(TonTaiChan(n)):
        print("Ton tai.")
    else:
        print("Khong ton tai: ")

if __name__ == "__main__":
    main()