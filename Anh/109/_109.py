def Euler():
    s=1
    m=1
    e=1
    i=1
    while(e>=10**-6):
        m=m*i
        e=1/m
        s+=e
        i+=1
    return s

def main():
    s=Euler()
    print("Euler =", s)

if __name__ == "__main__":
    main()

