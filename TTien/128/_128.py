
def XuatTangDan(aa, bb):
    if(aa>bb):
        tmp=aa
        aa=bb
        bb=tmp
    return aa, bb

def main():
    a = float(input("Nhap a: "))
    b = float(input("Nhap b: "))
    print(XuatTangDan(a, b))

if __name__=="__main__":
    main()