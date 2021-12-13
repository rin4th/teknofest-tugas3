print("""
        SOAL
1. half pyramid pattern
2. half inverted pyramid pattern
3. half pyramid pattern mirrored
4. full pyramid pattern
5. full pyramid pattern mirrored
        """)
pilih = int(input("pilih soal no berapa: "))
baris = int(input("input mau berapa baris: "))

def soal1(n):
    for i in range(1,n+1):
        for j in range(i):
            print("* ", end="")
        print()

def soal2(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("* ", end="")
        print()
def soal3(n):
    loop = int(input("pakai for atau while (1/0): "))
    if loop == 1:
        for i in range(1,n+1):
            for j in range(n,i,-1):
                print(" "*2, end="")
            for k in range(i):
                print("* ", end="")
            print()
    else:    
        i = 1
        while i <= n:
            space = ' '*((n-i)*2)
            stars = '* '*(i)
            print(space,stars, sep="")
            i += 1

def soal4(n):
    for i in range(1,n+1):
        for j in range(n,i,-1):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print()

def soal5(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for k in range(n,i,-1):
            print("* ", end="")
        print()

if pilih == 1:
    soal1(baris)
elif pilih == 2:
    soal2(baris)
elif pilih == 3:
    soal3(baris)
elif pilih == 4:
    soal4(baris)
elif pilih == 5:
    soal5(baris)
else:
    print("bukan termasuk soal")
