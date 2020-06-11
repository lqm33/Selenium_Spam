"""Şimdi gelelim en kolay ve en işe yarar modülümüze
istediğin yere istediğin şekilde bot yazmanızı sağlayan modül
SELENİUM MODÜLÜ
selenium modülü ile sitelerin butonlarına text alanların vs istediğiniz herşeyi yaptıraiblirsiniz """
"""şimdi gelelim selenium modülü kurulumuna
cmd yi açıyoruz
pip install selenium yazıyoruz ve iniyor
fakat şimdi taraycımızın driverini indirmemiz gerekiyor
ben chrome kullanıyorum bu nedenle chrome driver indiricem
chrome driver yazarak indirme sayfamıza geliyoruz ve uygun olan sürümü bulup
indiriyoruz
https://chromedriver.chromium.org/downloads
peki uygun sürümü nasıl bulucam
hemen göstereyim
AYARLAR
CHROME HAKKINDA
CHROME VERSİYONU VAR
Google Chrome güncel durumda
83.0.4103.97 (Resmi Derleme) (64 bit) Sürümü
83 YANİ BEN DE 83 ü indiricem hemen indirelim
windows linux ve mac için ayrılıyor windows için
chromedriver_win32 yi seçip indiriyoruz
şimdi programımız ile aynı dizine koymalıyız
Zip den çıkarıcaz
evet programla aynı dizine attık şimdi hazırız
başlayalım"""













import time # time modülünü import ettik
from selenium import webdriver
## selenium modülü import ediyoruz
## şimdi webdriveri tanımlayalım
driver=webdriver.Chrome()#chrome kullandığımız için chrome yazdık
## driver a tanımladık
## şimdi istediğimiz bir sayfayı açtıralım
driver.get("https://instagram.com")#driver.get(URL) ile açtırıcaz mesela Instagram ı açtıralım

# çalıştıralım
## gördüğünüz gibi mükemmel ötesi bir modül yapacaklarınız hayal gücünüze bağlı
## e peki şimdi açık ne işe yaradı ?
## şimdi username password girdirebiliriz mesela


time.sleep(3)# sayfaya gittikten 3 saniye sonra bekle dedik
## time.sleep(saniye) yazdığınız saniye kadar bekler

username=driver.find_element_by_name("username")## şimdi burda niye name yazdık onu anlatıyım
## driver.find
#driver ın içinde element i name olan birşeyi buldurma anlamına geliyo
#name in parantezinin içine username i yazıcaz yani artık bu orda ki username alanı
# şimdi bunu bir değişkene atayalım
#artık username değişkenimiz de bu var
username.send_keys("iliberitana@fashionelect.com")
# şimdi gördüğünüz kodu anlatıyım
# username i tanımlamıştık username.send_keys
# send_keys demek oraya bunu yaz demek
# yani send_keys("lkgljkasdgjlk") oraya lkgljkasdgjlk yazıcak demektir
# biz oraya kullanıcı adımızı gönderdik
# şimdi bir de şifremizi girdirelim değil mi ?
#aynı şekilde
password=driver.find_element_by_name("password")# çünkü name değeri password
password.send_keys("123456ders")
## şimdi çalıştıralım
time.sleep(1)
## send_keysler tamam fakat giriş yap butonuna bastırmadık
## bunu nasıl yapıcaz ?
## AA BAKTIK VE BUNUN NAME DEĞERİ YOK
## o zaman şunu yapıyoruz
## o elemente gelip sağ tık yapıp copy diyip copy full xpath dedik
## xpathi kopyalamış olduk
#xpathimiz bu  xpath nedir ?
"""xpath : sayfalar da her  butonun ve text alanının bir xpathi vardır
yani biz giriş butonunun xpathini kopyalamış olduk
şimdi bunu programımız da kullanalım"""


giris=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div")
#########
##
## şimdi ilk olarak driver.find_element_by_xpath dedik ve xpath değerini girip
# buldurduk
# şimdi tıklattırmak kaldı
## ama ilk önce kodumuzun anlaşılması açısından bunu bir değişkene atıyalım
giris.click()# bu kod ise click yani tıklama demektir
# istediğimiz yere tıklattırabiliriz
# giris.click() yaptık ve giris e click yapmasını istedik
## fakat bazen program da sorun olabilir yani yazmadan tıklayabilir bu yüzden
## passwordu girdikten sonra 1 saniye bekletelim ki sorun olmasın
# şimdi çalıştıralım

#evet gördüğünüz gibi girdi
#bir daha ki derse spam bot yapıcaz

# evet şimdi gelelim spam aracı yazmaya
#en son girişimizi yaptırmıştık
# tekrar bakalım
#şimdi bu çıkan şeyi kapatma kodunumuzu yazalım
time.sleep(2)# 2 saniye bekleyelim ki sorun çıkmasın
#hesap kaydetme
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()### bu kod ile değişkene atamadan tıklattırabiliyoruz.
time.sleep(2)# bu şeyi kapattıktan sonra 2 saniye bekleyelim ki hata çıkmasın
#bildirim
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
#şimdi bunu da kapattıktan sonra ne yapacğaız ona bakalım
## arama yerine kurbanın adını yazmalıyız
# bunun için input yani kullanıcıdan veri alıcaz
kurban=input("Kimi Şikayet etmek istersiniz...:")#kimi şikayet etmek istiyorsunuz
#adında da bir input aldırdık
"""ara=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
ara.send_keys(kurban)
# şimdi ara diye bir değişken atadık ve arama kutusunun xpathini verdik
# ara.send_keys(kurban) kurban adında input aldırmıştık onu oraya yazdırdık
# bakalım şimdi
# buraya kadar sorunsuz çalışıyor değil mi ?
time.sleep(1)# 1 saniye bekletelim ki ekran da istenilen şey çıksın 
#şimdi orda bulunan yani yazdıktan sonra çıkan kullancıya tıklattıralım
driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]").click()
# şimdi tıklattırdıktan sonra ne olduğuna bakalım
# evet şimdi hata aldık
#hata kodumuza bakalım
# NoSuchElementException yani istenilen element (xpathimiz) sayfa da bulunmadı dedi
#bunu demesinin sebebi o an ekran bulunmaması o yüzden time.sleep(1) ekliyelim ve
#hatayı giderelim
#evet istenilen sayfaya gittik fakat şimdi boşuna kod yazarak zaman kaybetmeyelim
# yani işimiz az kodla çok iş yapmak
# o yüzden şöyle birşey farkettim
#https://www.instagram.com/reynmen/
# yani instagram kullanıcı adını url e yansıtmış
# burda yapacağımız şey şöyle olablir"""
##############################################
driver.get("https://www.instagram.com/"+kurban)
# yani instagram kullanıcı adını url e yansıttığı için
# direk kullanıcı adını alıp
# instagram.com'un sonuna ekleyip
# driver.get yaptığım için
# direk o kişinin sayfasına gidicek
# çalıştıralım
# bu arada arkada ki açık chromeları kapatayım ram yemesin
# https://www.instagram.comreynmen/ evet böyle bir url olmadığı için
#bir yere gitmedi o yüzden sonuna / koymalıyız
# bir de şimdi deniyelim
# evet gördüğünüz gibi çalıştı ve böylece daha kolay bir şekilde işlemimizi
# halletmiş olduk
# şimdi spam işlemline geçelim
#
#
# ... (üç nokt) ya bastırdık 
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button").click()
# kullanıcıyı şikayet et' e bastırdık
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/button[3]").click()
# spam a bastırdık
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[1]/div").click()
#şimdi yaptığım işlemleri anlatayım ilk olarak
print("Başarılı bir şekilde Spam atıldı")
########################################
# yani burda da program bitince print ile bilgilendirme yaptık
# fakat tıklarken arada 1 saniye time.sleep vermek iyi olur örnek
#burda  NoSuchElementException almamak için time.sleep gerekmekte


# evet hata aldık bu çok normal çünkü selenium modülü ile proje yaparken
# hata alacağız
# ben orda iconun xpathini almışım böyle şeyler çok normal
#bir daha ki video da görüşmek üzere
#ders 3 https://www.dosya.tc/server29/wccnmr/2020-06-07_19-48-09.mkv.html











































"""evet şimdi hata verdi bu çok normal çünkü aradığımız şeyi sayfa da bulamadık
niye bulamadık ?
sayfa tam yüklenmedi diye
şimdi sayfa tam yüklelene kadar bekletelim değil mi ?
bunu yapmak için pythonun modülü olan
TİME modülünü kullanıcaz"""


"""incele yaparak elementleri bulucaz
mesela kullancı adı elementini bulalım
hemen şöyle yapıyoruz
burda çıkan yer oranın elementleridir
şimdi bunlarla ne yapabilirz izleyin
name=username olduğunu gördük
name="password"
yani
name değeri
username e eşitmiş
birde şifre değerini bulalım
name password
passwordun name değeri password muş
şimdi bunları kullanarak giriş yaptırabilirz
hemen bir hesap açalım rastgele


iliberitana@fashionelect.com


123456ders
evet şimdi hesap açtık gelelim kodlarımızı kullanmaaya

"""




















