
# Asal sayılar, sadece kendisine ve 1 sayısına kalansız bölünebilen, 1'den büyük sayma sayılarıdır
# Bu program kullanıcıdan alınan sayının asal olup olmadığını söyler

# Asal sayi kontrolü yapan fonksiyon oluşturuyoruz.
def sayiAsalMi(sayi):

    # 2 kez aynı mesajı yazmamak için değişken atıyoruz.
    mesaj = 'Asal sayı değildir.'
    # Girilen sayının 1'den küçük olup olmadığını kontrol ediyoruz.
    if sayi <= 1:
        return mesaj
    # 1'den büyük olan sayıların kontrolü için for döngüsü yazıyoruz.
    for i in range(2, sayi):
        if sayi % i == 0:
            return mesaj
    mesaj2 = 'Asal sayıdır.'
    return mesaj2


sayi = int(input("Bir sayı giriniz: "))
print(sayiAsalMi(sayi))
