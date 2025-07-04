def ktHoanThien(nn):
    s = 0
    i = 1
    while(i < nn):
        if(nn % i == 0):
            s += i
        i += 1
    if (s == nn): return True
    else : return False

def main():
    n = int(input("Nhap n:"))
    kt = ktHoanThien(n)
    if (kt == True): print("Hoan thien")
    else: print("Khong hoan thien")

if __name__ == "__main__":
    main()
