tahun = int(input("masukan tahun: "))
kabisat = (tahun % 400 == 0) or (tahun % 4 == 0) and (tahun % 100 != 0)
if kabisat :
    print(f"tahun {tahun} termasuk kedalam tahun kabisat")
else:
    print(f"tahun {tahun} tidak termasuk ke dalam tahun kabisat")
