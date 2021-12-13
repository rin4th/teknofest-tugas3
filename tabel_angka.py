n = int(input())

def tabel(n):
    for i in range(1,n+1):
        for j in  range(1,n+1):
            print(i * j, end="")
        print()

if n >= 1 and n <= 30:
    tabel(n)
else:
    print("salah")
