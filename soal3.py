kata = input("masukan list kata: ").split()
def appear(lst):
    muncul = {}
    for i in lst:
        muncul[i] = lst.count(i)
    muncul = dict(sorted(muncul.items(), key = lambda item: item[1]))
    for j, k in muncul.items():
        print(f"{j} : {k}")

appear(kata)





