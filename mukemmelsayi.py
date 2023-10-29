# Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)
# Mükemmel sayı; bölenleri toplandığında kendisine eşit olan sayı.

toplam = 0
sayi = int(input("Bir sayı giriniz:"))
for i in range(1, sayi):
    if (sayi % i == 0):
        toplam = toplam + i
if (sayi == toplam):
    print("mukemmel sayidir")
else:
    print("sayisi mükemmel sayı değildir.")
