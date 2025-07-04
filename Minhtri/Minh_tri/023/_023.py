def Hangchuc(n):
    return (n//10)%10

def main():
    n=int(input("Nhap n: "))
    print("Chu so hang chuc:", Hangchuc(n))

if __name__=="__main__":
    main()