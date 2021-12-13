angka = input("masukan list angka: ").split()
angka = [int(i) for i in angka]
target = int(input("masukan angka target: "))
def sekali(a, t):
    output = []
    for i in a:
        for j in a:
            if (i + j == t) and (a.index(i) != a.index(j)):
                output.extend([a.index(i),a.index(j)])
                return output
print("kombinasi angkanya adalah :",sekali(angka, target))

