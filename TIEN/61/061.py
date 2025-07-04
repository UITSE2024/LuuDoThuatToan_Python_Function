
def ChuSoLe(nn):
    dem = 0
    t = nn
    while(t):
        dv = t % 10
        if(dv%2): 
            dem+=1
        i+=1
        t=t//10
    return t
def main():
    n = int(input())
    print(ChuSoLe(n))
if __name__ == "__main__":
    main()

