def my_function(shopping):
  for x in shopping:
    print(x)
while True:
    print("Hoşgeldiniz, Alışveriş yapmak için 1'e, çıkış yapmak için 0'a basınız...")
    secim=input("Seçiminiz: ")
    if secim=='0':
        print("Çıkış yaptınız, teşekkür ederiz")
    elif secim=='1':
        print("Siteye hoşgeldiniz")
        shopping=['(1)CLothes','(2)Shoes', '(3)Accesories ', '(4)Makeup', '(5)Bags']
        my_function(shopping)
        kategori=input("Kategori giriniz:")
        if kategori=='1':
           clothes=['(1)Tshirts' ,'(2)Jeans','(3)Hoodies'] 
           my_function(clothes)
           altkategori=input("Alt kategori giriniz:")
           if altkategori=='1':
               tshirts=['(1)Bershka Cotton Tshirt 40TL','(2)Pull&Bear Crop Tshirt 35TL','(3)Stradivarius Pink Tshirt 50Tl','(4)Mavi Grey Tshirt 50TL','(5)Us Polo Tshirt 90Tl']
               my_function(tshirts)
               tshirt=input("Satın almak istediğiniz ürünü giriniz:")
               devam=input("Siparişiniz alındı. Alışverişe devam etmek ister misiniz? (1)Evet (2)Hayır")
               if devam=='1':
                   print("Yönlendiriliyorsunuz...")
               if devam=='2':
                   print("Lütfen müşteri bilgilerini giriniz:")
                   input("Ad Soyad:")
                   input("Telefon:")
                   input("E-posta:")
                   input("Adres:")
                   print("Sepetteki ürünler: "+tshirt)
                   choice=input("Ödeme Yöntemi: (1) Kapıda Ödeme (2) Kredi Kartı: ")
                   if choice=='1':
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
                   if choice=='2':
                       input("Kart No: ")
                       input("Son Kullanma Tarihi: ")
                       input("CVV: ")
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
           if altkategori=='2':
               jeans=['(1)Ltb Straight Jeans 200Tl','(2)Mavi Mom Jeans 130TL','(3)Addax SlimFit 60Tl','(4)Tendyolmilla Straigths 99TL','(5)Bershka Jeans 170TL']
               my_function(jeans)
               jean=input("Satın almak istediğiniz ürünü giriniz:")
               devam1=input("Siparişiniz alındı. Alışverişe devam etmek ister misiniz? (1)Evet (2)Hayır")
               if devam1=='1':
                    print("Yönlendiriliyorsunuz...")
               if devam1=='2':
                   print("Lütfen müşteri bilgilerini giriniz:")
                   input("Ad Soyad:")
                   input("Telefon:")
                   input("E-posta:")
                   input("Adres:")
                   print("Sepetteki ürünler: "+jean)
                   choice=input("Ödeme Yöntemi: (1) Kapıda Ödeme (2) Kredi Kartı: ")
                   if choice=='1':
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
                   if choice=='2':
                       input("Kart No: ")
                       input("Son Kullanma Tarihi: ")
                       input("CVV: ")
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
           if altkategori=='3':
               hoodies=['(1)Addax blue hoodies 75TL','(2)Mavi Hoodies 130TL','(3)Pull&Bear Hoodies 60Tl','(4)Tendyolmilla Hoodies 120TL','(5)Bershka Hoodies 170TL']
               my_function(hoodies)
               hoodie=input("Satın almak istediğiniz ürünü giriniz:")
               devam2=input("Siparişiniz alındı. Alışverişe devam etmek ister misiniz? (1)Evet (2)Hayır")
               if devam2=='1':
                    print("Yönlendiriliyorsunuz...")
               if devam2=='2':
                   print("Lütfen müşteri bilgilerini giriniz:")
                   input("Ad Soyad:")
                   input("Telefon:")
                   input("E-posta:")
                   input("Adres:")
                   print("Sepetteki ürünler: "+hoodie)
                   choice=input("Ödeme Yöntemi: (1) Kapıda Ödeme (2) Kredi Kartı: ")
                   if choice=='1':
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
                   if choice=='2':
                       input("Kart No: ")
                       input("Son Kullanma Tarihi: ")
                       input("CVV: ")
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
        if kategori=='2':
           shoes=['(1)Sneakers','(2)High Heels','(3)Wedges'] 
           my_function(shoes)
           shoesalt=input("Alt kategori giriniz:")
           if shoesalt=='1':
               sneakers=['(1)Nike 400TL','(2)Puma 360TL','(3)New Balance 500TL','(4)Tergan 250TL','(5)Adidas 600TL']
               my_function(sneakers)
               sneaker=input("Satın almak istediğiniz ürünü giriniz:")
               sec=input("Siparişiniz alındı. Alışverişe devam etmek ister misiniz? (1)Evet (2)Hayır")
               if sec=='1':
                    print("Yönlendiriliyorsunuz...")
               if sec=='2':
                   print("Lütfen müşteri bilgilerini giriniz:")
                   input("Ad Soyad:")
                   input("Telefon:")
                   input("E-posta:")
                   input("Adres:")
                   print("Sepetteki ürünler: "+sneaker)
                   choice=input("Ödeme Yöntemi: (1) Kapıda Ödeme (2) Kredi Kartı: ")
                   if choice=='1':
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
                   if choice=='2':
                       input("Kart No: ")
                       input("Son Kullanma Tarihi: ")
                       input("CVV: ")
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
           if shoesalt=='2':
               highheels=['(1)Tergan 400TL','(2)Elle 360TL','(3)Hotiç 500TL','(4)Ayakkabı Dünyası 250TL','(5)Greyder 600TL']
               my_function(highheels)
               highheel=input("Satın almak istediğiniz ürünü giriniz:")
               sec1=input("Siparişiniz alındı. Alışverişe devam etmek ister misiniz? (1)Evet (2)Hayır")
               if sec1=='1':
                    print("Yönlendiriliyorsunuz...")
               if sec1=='2':
                   print("Lütfen müşteri bilgilerini giriniz:")
                   input("Ad Soyad:")
                   input("Telefon:")
                   input("E-posta:")
                   input("Adres:")
                   print("Sepetteki ürünler: "+highheel)
                   choice=input("Ödeme Yöntemi: (1) Kapıda Ödeme (2) Kredi Kartı: ")
                   if choice=='1':
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
                   if choice=='2':
                       input("Kart No: ")
                       input("Son Kullanma Tarihi: ")
                       input("CVV: ")
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
           if shoesalt=='3':
               wedges=['(1)Tergan 200TL','(2)Elle 300TL','(3)Hotiç 700TL','(4)Ayakkabı Dünyası 100TL','(5)Greyder 200TL']
               my_function(wedges)
               wedge=input("Satın almak istediğiniz ürünü giriniz:")
               sec2=input("Siparişiniz alındı. Alışverişe devam etmek ister misiniz? (1)Evet (2)Hayır")
               if sec2=='1':
                   print("Yönlendiriliyorsunuz...")
               if sec2=='2':
                   print("Lütfen müşteri bilgilerini giriniz:")
                   input("Ad Soyad:")
                   input("Telefon:")
                   input("E-posta:")
                   input("Adres:")
                   print("Sepetteki ürünler: "+wedge)
                   choice=input("Ödeme Yöntemi: (1) Kapıda Ödeme (2) Kredi Kartı: ")
                   if choice=='1':
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
                   if choice=='2':
                       input("Kart No: ")
                       input("Son Kullanma Tarihi: ")
                       input("CVV: ")
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
        if kategori=='4':
           makeup=['(1)Mascara ,(2)LipStick, (3)Highlighter'] 
           my_function(makeup)
           makeupalt=input("Alt kategori giriniz:")
           if makeupalt=='1':
               mascara=['(1)Maybelline 40Tl','(2)NYX 36TL','(3)Note 50TL','(4)Farmasi 25TL','(5)Beaulis 22TL']
               my_function(mascara)
               mascaras=input("Satın almak istediğiniz ürünü giriniz:")
               msc=input("Siparişiniz alındı. Alışverişe devam etmek ister misiniz? (1)Evet (2)Hayır")
               if msc=='1':
                    print("Yönlendiriliyorsunuz...")
               if msc=='2':
                   print("Lütfen müşteri bilgilerini giriniz:")
                   input("Ad Soyad:")
                   input("Telefon:")
                   input("E-posta:")
                   input("Adres:")
                   print("Sepetteki ürünler: "+mascaras)
                   choice=input("Ödeme Yöntemi: (1) Kapıda Ödeme (2) Kredi Kartı: ")
                   if choice=='1':
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
                   if choice=='2':
                       input("Kart No: ")
                       input("Son Kullanma Tarihi: ")
                       input("CVV: ")
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
           if makeupalt=='2':
               lipstick=['(1)Mac 140TL','(2)Sephora 42TL','(3)Beaulis 15TL','(4)Wet&Wild 25TL','(5)Flormar 30TL']
               my_function(lipstick)
               lipsticks=input("Satın almak istediğiniz ürünü giriniz:")
               lps=input("Siparişiniz alındı. Alışverişe devam etmek ister misiniz? (1)Evet (2)Hayır")
               if lps=='1':
                    print("Yönlendiriliyorsunuz...")
               if lps=='2':
                   print("Lütfen müşteri bilgilerini giriniz:")
                   input("Ad Soyad:")
                   input("Telefon:")
                   input("E-posta:")
                   input("Adres:")
                   print("Sepetteki ürünler: "+lipsticks)
                   choice=input("Ödeme Yöntemi: (1) Kapıda Ödeme (2) Kredi Kartı: ")
                   if choice=='1':
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
                   if choice=='2':
                       input("Kart No: ")
                       input("Son Kullanma Tarihi: ")
                       input("CVV: ")
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
           if makeupalt=='3':
               highlighter=['(1)The balm 129TL','(2)Revlon 70TL','(3)Maybelline 50TL','(4)Nyx 100TL','(5)Mac 200TL']
               my_function(highlighter)
               highligters=input("Satın almak istediğiniz ürünü giriniz:")
               hgh=input("Siparişiniz alındı. Alışverişe devam etmek ister misiniz? (1)Evet (2)Hayır")
               if hgh=='1':
                    print("Yönlendiriliyorsunuz...")
               if hgh=='2':
                   print("Lütfen müşteri bilgilerini giriniz:")
                   input("Ad Soyad:")
                   input("Telefon:")
                   input("E-posta:")
                   input("Adres:")
                   print("Sepetteki ürünler: "+highligters)
                   choice=input("Ödeme Yöntemi: (1) Kapıda Ödeme (2) Kredi Kartı: ")
                   if choice=='1':
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
                   if choice=='2':
                       input("Kart No: ")
                       input("Son Kullanma Tarihi: ")
                       input("CVV: ")
                       print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
    else:
        print("1 veya 0 giriniz")