def demSoLuong(nn):
    t = nn
    dem = 0
    while(t != 0):
        dem += 1
        t = t // 10

    return dem

def main():
    n = int(input("Nhap vao gia tri cua n: "))
    SLChuSo = demSoLuong(n);
    print("So luong chu so trong so n: {}".format(SLChuSo))

  
if __name__ == "__main__":
    main()
