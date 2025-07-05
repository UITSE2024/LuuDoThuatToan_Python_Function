def Nhap():
    nn = int(input("Nhap n: "))
    return nn

def ktCoDang(nn):
    flag = 1
    t = nn

    while t > 1:
        du = t % 2
        if (du != 0):
            flag = 0
        t = t // 2
        
    if (flag == 1):
        return True
    else:
        return False

def Xuat(flag, nn):
    if (flag == True):
        print("So " + str(nn) + " co dang 2^k")
    else:
        print("So " + str(nn) + " khong co dang 2^k")

def main():
    n = Nhap()
    flag = ktCoDang(n)
    Xuat(flag, n)

if __name__ == "__main__":
    main()