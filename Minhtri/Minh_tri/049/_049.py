def Lietkeuocso(n):
    i=1
    while (i<=n):
        if(n%i==0):
            print(i)
        i+=1
def main():
    n=int(input("Nhap n: "))
    Lietkeuocso(n)
if __name__=="__main__":
    main()
            