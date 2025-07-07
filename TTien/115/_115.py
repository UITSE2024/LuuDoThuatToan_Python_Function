
def TinhAn(nn):
    att = -1
    at = 3
    i = 2
    if(nn==0):
        ahh=-1
    elif(nn==1):
        ahh=3
    else:
        while(i<=nn):
            ahh = 5*at + 6*att
            i+=1
            att=at
            at=ahh
    return ahh

def main():
    n = int(input("Nhap n: "))
    print("So hang thu n: ", TinhAn(n))

if __name__=="__main__":
    main()