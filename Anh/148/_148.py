def kiemtratoanchan(nn):
    flag=1
    t=nn
    while(t!=0):
        dv= t % 10
        if dv % 2 != 0:
            flag = 0
        t= t // 10
    if flag == 1:
        print("So", nn, "la so toan chan")
    else:
        print("So", nn, "khong la so toan chan")

def main():
    n = int(input("Nhap nam: "))
    kiemtratoanchan(n)

if __name__ == "__main__":
    main()



