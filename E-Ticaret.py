import colorama                                # Yazı tipi rengini turuncu olarak değiştirdik.
from colorama import Fore, Back, Style
colorama.init()
print(Fore.YELLOW)
#print("Bu SARI bir yazıdır.")


class kullaniciislemler : # tüm işlemleri yapacağımız sınıfı oluşturduk
 
    def __init__(self,name,password,name2,password2,sepet,sekmeler,altsekmeler,urunler):   # sınıfımıza ilk değer atamasını yaptık
        self.name = name                   # kullanıcı isim kontrolü
        self.password = password           # kullanıcı şifre kontrolü
        self.name2 = name2                   # kullanıcı isim kontrolü
        self.password2 = password2           # kullanıcı şifre kontrolü
        self.sepet = sepet                 # sepet ürünleri mevcut
        self.sekmeler = sekmeler           # sekmeler ataması yapıldı
        self.altsekmeler = altsekmeler     # alt sekmeler ataması yapıldı   
        self.urunler = urunler             # urunler ataması yapıldı

    def kullanicigirisi(self):                                                  # sınıfımızın kullanıcı girişi sağlanmaktadır
        print("\n\n**** İstinye Online Market’e Hoşgeldiniz ****")
        print("\nLütfen kullanıcı kimlik bilgilerinizi sağlayarak giriş yapın:")
        adgiris = input("Kullanıcı adını giriniz: ")
        sifegiris = input("Şifre Giriniz: ")
        if (self.name == adgiris and self.password == sifegiris) or (self.name2 == adgiris and self.password2 == sifegiris):
            print("\nGiriş başarılı !")
            kullanici = adgiris
            print(f" \nHoşgeldiniz {kullanici}! Lütfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin.")     
        else :
            while True:
                print("\nKullanıcı adınız veya şifreniz doğru değil. Lütfen tekrar deneyin! ")
                adgiris = input("Kullanıcı adını giriniz: ")
                sifegiris = input("Şifre Giriniz: ")
                if (self.name == adgiris and self.password == sifegiris) or (self.name2 == adgiris and self.password2 == sifegiris):
                    break
            print(" \nGiriş Başarılı !")
            kullanici = adgiris
            print(f" \nHoşgeldiniz {kullanici}! Lütfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin.")
    
    def urunsekme(self):                          # urunlerin olduğu sekmedir 
        for i in self.sekmeler :
            print("-" + i)
             
        sekmesecim = int(input("\nSeçim yapınız: "))   #urun sekme şartları bulunuyor 
        if sekmesecim == 1:
            self.urunlersecim()
            
        elif sekmesecim == 2:
            self.sepettekiler()
        elif sekmesecim == 3:
            self.sepettekiler()
        elif sekmesecim == 4 :
            print("Oturum  başarıyla kapandı! tekrar giriş yapmak için kullanıcı adı ve şifrenizi girin: ")
            self.kullanicigirisi()
            self.urunsekme()
        elif sekmesecim == 5 :
            print("Oturum  başarıyla kapandı! tekrar giriş yapmak için kullanıcı adı ve şifrenizi girin: ")
            self.kullanicigirisi()
            self.urunsekme()
        pass
        


    def altsekme(self):                        #urunlerin alt sekmesidir 
        for i in self.altsekmeler :
            print("-" + i)           
        altsekmesecim = int(input("Seçim yapınız: "))     #sekme seçenekleri bulunuyor 
        if altsekmesecim == 1 :
            tutar = input("Yeni Tutarı Giriniz: ")
            print("Yeni tutar başarıyla Güncellendi Ana sekmeye yönlendiriliyorsunuz...")
            self.urunsekme()

        elif altsekmesecim == 2:
            kaldir = input("Kaldırmak istediğiniz öğeyi ismini giriniz: ")
            self.sepet.pop(kaldir)
            print("Ürün başarıyla kaldırıldı Ana menüye Yönlendiriliyorsunuz...")
            self.urunsekme()
        elif altsekmesecim == 3:
            print("Makbuzunuz işleniyor...")
            print("******* İstinye Online Market ********")
            print("*************************************")
            print("0850 283 6000")
            print("istinye.edu.tr")
            print("————————————————————————————————————")
            print(f"{self.sepet}")
            print("Toplam 22.0 $")
            print("————————————————————————————————————")
            print("2021/01/01 17:00")
            print("Online Market’imizi kullandığınız için teşekkür ederiz!\n")
            self.urunsekme()

        elif altsekmesecim == 4:
            self.urunsekme()
            pass
        
    def urunlersecim(self):      # urunsecme sekmesidir
        number = 1 
        urunliste = {}
        arama = input("Ne arıyorsunuz? :")
        for i in self.urunler:
            for j in i.split(" "):
                if j == arama:
                    if self.urunler[i][0]!=0:
                        urunliste[i]=str(self.urunler[i][1])
                    break

        if not urunliste:
            x = input("\nAradığınız kelime Sözlükte bulunamadı.Ana menüye dönmek için 0 Tekrar arama yapmak için 1 tuşlayınız: ")
            if (x == "1"):
                self.urunlersecim()
            else:
                self.urunsekme()
        
        else:
            for i in urunliste:
                print(f"{number}.  {i} ürün fiyatı {urunliste[i]}$")
                number += 1
            x = input("Ana menüye dönmek için 0 ürün seçmek için ürün numarasını giriniz.")
            if (x =="0"):
                self.urunlersecim()
            elif (int(x) <= number and int(x) >= 1):
                number = 1
                for i in urunliste:
                    if(number==int(x)):
                        self.sepet.append(i)
                        print(f"\n{i} Sepete Eklendi" )
                        print("Ana menüye geri dönülüyor...")
                        self.urunsekme()
                    number += 1
            else:
                print("Geçersiz tuşlmam yaptınız")
                self.urunlersecim()   



    def sepettekiler(self):     # sepet sekmesidir 
        if self.sepet==[]:
            print("\n\n--------------- Sepetiniz Boş Ana sekmeye Yönlendiriliyorsunuz...  \n\n")
            self.urunsekme()
        else :
            print(f"\n**********Sepetteki Mevcut ürünler********** \n{self.sepet}\n")
            self.altsekme()
                    


# ---------------------------------------------------- Veri girişlerinin bulunduğu bölümdür -----------------------------------------------------------

q1 = kullaniciislemler("ahmet","istinye123","meryem","4444",[],["1. Ürün ara" ,"2. Sepete git" ,"3. Satın al", "4. Oturum Kapat", "5. Çıkış yap" ],["1. Tutarı güncelleyin","2. Bir öğeyi kaldırın","3. Satın al","4. ana menüye dön"],{'kuşkonmaz': [10,5],'brokoli': [15,6],'havuç': [18,7],'elmalar': [20,5],'muz':[10, 8],'meyve': [30,3],'yumurta': [50,2],
    'karışık meyve suyu': [0,18],'balık çubukları':[25,12],'dondurma': [32,6],'elma suyu': [40,7],'portakal suyu': [30,8],'üzüm suyu':[10,9] })
q1.kullanicigirisi()
q1.urunsekme()




        