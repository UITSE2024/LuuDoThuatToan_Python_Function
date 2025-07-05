
def TinhCapSoCong(nn):
    ahh = 2
    at = 2
    i = 2
    while(i <= nn):
        ahh = at + 2*i+1
        at = ahh
        i+=1
    return ahh
def main():
    n = int(input())

    print(TinhCapSoCong(n))
if __name__ == "__main__":
    main()
