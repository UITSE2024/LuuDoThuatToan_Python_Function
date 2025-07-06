
def Tinh():
    s = 0
    e = 0.5
    i = 2
    epsilon = 10**-6
    while(e>=epsilon):
        e=1/i
        s = s+e
        i = i+2
    return s

def main():
    print("Ket qua: ", Tinh())

if __name__=="__main__":
    main()