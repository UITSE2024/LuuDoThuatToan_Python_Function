
from tkinter import N


def kiemtraluythua3(nn):
    flag = 1
    t = nn 
    while(t > 1):
        du = t % 3
        if(du): flag = 0
        t = t//3
    return flag
def main():
    n = int(input())
    if(kiemtraluythua3(n)): print("La dang")
    else: print("Khong la dang")
if __name__ == "__main__":
    main()