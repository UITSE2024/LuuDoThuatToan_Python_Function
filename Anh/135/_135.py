def kiemtranhuan(nn):
    dk1= nn % 4 == 0 and nn % 100 != 0
    dk2 = nn % 400 == 0
    return dk1 or dk2


def main():
    n = int(input("Nhap nam: "))
    if(kiemtranhuan(n)):
        print("Nam", n, "la nam nhuan")
    else:
        print("Nam", n, "khong la nam nhuan")

if __name__ == "__main__":
    main()



