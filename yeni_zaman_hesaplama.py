

def zaman_hesaplama():

    toplam_saniye = int(input("Lütfen bir saniye değeri giriniz :"))

    gun = toplam_saniye // 86400
    kalan_saniye = toplam_saniye % 86400

    saat = kalan_saniye // 3600
    kalan_saniye = kalan_saniye % 3600

    dakika = kalan_saniye // 60
    kalan_saniye %= 60

    print("{} saniye = {} gün {} saat {} dakika {} saniyeye eşittir.".format(toplam_saniye,gun,saat,dakika,kalan_saniye))


zaman_hesaplama()