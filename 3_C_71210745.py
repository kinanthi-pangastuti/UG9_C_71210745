#soal 3 : menghitung jumlah sak semen
#alas atap = AA
#tinggi atap = TA
#tingi tembok = TT
AA = int(input("Masukkan alas atap: "))
TA = int(input ("Masukkan tinggi atap: "))
TT = int(input ("Masukkan tinggi tembok: "))

#luas atap  = LA
#           = 0.5 * (alat atap * tinggi atap)
LA = 0.5 * (AA * TA)
#luas tembok= LT
#           = tinggi tembok * tinggi tembok
LT = TT * TT
#luas total = L
L = LA + LT

#jumlah sak semen = luas total / 5
x = L / 5
print ("rumah tersebut membutuhkan", x,"sak semen")

