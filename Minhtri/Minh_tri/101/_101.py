def Tinh():
    s=0
    e=1
    i=1
    while (e>=0.000001):
        e=1/i
        s+=e
        i+=1
    return s
def main():
    print("Ket qua: ", Tinh())
