print("""\t***Garanti Bankasina Hosgeldiniz!!
      \t\tLutfen kartinizi takiniz yada kartsiz islemler menusune geciniz...""")





Veri_Tabani={"yesim_hesap":{
               "isim":"yesim",
               "soyisim":"ilter",
               "KartSifre": 1234,
               "HesapBakiye":9500,
               "KrediKartiBorc":5300,
               "KrediKartiBorcTarih":"27/12/2021"},
           
               "erdem_hesap":{
               "isim":"erdem",
               "soyisim":"alim",
               "KartSifre": 5678,
               "HesapBakiye":6500,
               "KrediKartiBorc":1300,
               "KrediKartiBorcTarih":"17/12/2021"}
                 }


Takilan_Kart=dict(Veri_Tabani.get("yesim_hesap"))



Hak=2


for i in range(0,3):
    Sifre=int(input("lutfen sifrenizi giriniz: "))
    if Sifre==Takilan_Kart.get("KartSifre"):
        print("""Merhaba Sayin {} {} hosgeldiniz
              Lutfen yapmak istediginiz islemi seciniz...""".
        format(Takilan_Kart.get("isim"),Takilan_Kart.get("soyisim")))
        Sec=input(""" 
              [1] BAKIYE SORGULAMA
              [2] KREDI KARTI BORC SORGULAMA
              [3] PARA CEKME
              [4] PARA YATIRMA
              [Q] KART IADE VE CIKIS\n""")
        break
    
    elif Sifre!=Takilan_Kart.get("KartSifre") and Hak!=0:
        print("Hatali sifre girdiniz, kalan giris hakkiniz {}".format(Hak))
        Hak-=1
    elif Sifre!=Takilan_Kart.get("KartSifre") and Hak==0:
        print("""Sifrenizi 3 kez yanlis girdiniz!!! kartiniz bloke olmustur,
              Lutfen en yakin subemize basvurunuz""")
        exit()

if Sec=="1":
        print("Hesap Bakiyeniz {} TL'dir ".format(Takilan_Kart.get("HesapBakiye")))
elif Sec=="2":
        print("""Kredi karti borcunuz: {} TL'dir,Son odeme tarihi: {} """
              .format(Takilan_Kart.get("KrediKartiBorc"),Takilan_Kart("KrediKartiBorcTarih")))
elif Sec=="3":
        Miktar1=int(input("Lutfen cekmek istediginiz tutari giriniz: "))
        if Takilan_Kart.get("HesapBakiye")<Miktar1:
            print("Yetersiz Bakiye!!!")
        else:
             print("Paraniz veriliyor....Lutfen once kartinizi sonra paranizi aliniz....")
             YeniBakiye1=Takilan_Kart.get("HesapBakiye")- Miktar1
             print("yeni bakiyeniz {} TL' dir".format(YeniBakiye1))
elif Sec=="4":
        Miktar2=int(input("Lutfen yatirmak istediginiz tutari giriniz :"))
        print("Paraniz hesabiniza yatirilmistir!!")
        YeniBakiye2=Takilan_Kart.get("HesapBakiye")+Miktar2
        print("Guncel bakiyeniz {}TL' dir".format(YeniBakiye2))
elif Sec=="Q" or Sec== "q":
        print("Talebiniz uzerine sistemden cikiliyor....iyi gunler dileriz")
       
         
else:
         print("lutfen gecerli bir islem giriniz!!!")        
        
    
    
    
          
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              