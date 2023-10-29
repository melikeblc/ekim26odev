# 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

# Verilen bilgiden yola çıkarak ilk iki elemanı "1" olan bir dizi tanımladık.
series = [1, 1]
n = 30


# Burada oluşturulan for döngüsü, fibonacci serisindeki bir sonraki sayıyı hesaplamak için kendisinden önceki 2 sayıyı toplar.
for x in range(2, n):
    next = series[x - 1] + series[x - 2]
    # döngü her döndüğünde ulaştığımız yeni sayıyı append methodu ile series dizisinin sonuna ekliyoruz.
    series.append(next)

print(series)
