def LietKe(nn):
    i = 1
    while(i <= nn):
        if(nn % i == 0): 
            print(i, end=' ')
        i += 2

def main():
    n = int(input("Nhap n: "))
    
    print("Cac uoc le: ", end = ' ')
    LietKe(n)

if __name__ == "__main__":
    main()
