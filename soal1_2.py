masuk = input("masukan angka(str): ")
def sekali(txt):
    sendiri = []
    for i in txt:
        if txt.count(i) == 1:
            i = int(i)
            sendiri.append(i)
    return sendiri

print("angka yang muncul sekali :",sekali(masuk))

