
def TichSoLe(nn):
    tich = 1
    t = nn
    while(t!=0):
        dv = t%10
        if(dv%2!=0):
            tich = tich*dv
        t = t//10
    return tich

def main():
    n = int(input("Nhap n: "))
    print("Tich cac chu so le: ", TichSoLe(n))

if __name__=="__main__":
    main()
    