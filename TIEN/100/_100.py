
def TongCan(nn):
    s = 0
    t = 1
    i = 1
    while(i <= nn):
        t*=i
        s = pow(t+s, 1/i+1)
        i+=1
    return s
def main():
    n = int(input())
    print(TongCan(n))
if __name__ == "__main__":
    main()
