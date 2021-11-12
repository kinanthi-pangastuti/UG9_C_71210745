#soal 4 : perhitungan deret aritmatika
#suku ke- n = Un
#suku pertama
U1 = int(input("suku pertama : "))
#suku kedua
U2 = int(input("suku kedua : "))
               
#banyak suku deret = n
n = int(input("banyak suku : "))

#beda antarsuku = b
#               = U(n+1) - Un
b = U2 - U1
print("beda : ", b)

#jumlah suku ke(n)  = Sn
#                   = (n/2)*(2*U1+(n-1)*b)
Sn = (n / 2) * ((2 * U1) + (n - 1) * b)
print("jumlah suku ke-", n, "= ", Sn)
