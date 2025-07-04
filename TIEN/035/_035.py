
def TichLienTiep(nn):
    t = 1
    i = 1
    while(i <= nn):
        t*=i
        i+=1
    return t
def main():
    n = int(input())
    print(TichLienTiep(n))
if __name__ == "__main__":
    main()
