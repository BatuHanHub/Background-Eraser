# NASIL ÇALIŞIR?
1 - picture adlı dizine arka planını silmek istediğiniz fotografı atın <br>
2 - .py ya da .exe dosyasını çalıştırınız <br>
3 - dilinizi seçiniz <br>
4 - arka planını silmek istediğiniz fotografın adını ve uzantısını yazınız
örneğin: resim1.png ya da resim2.jpg<br>
5 - arka planının silinmesini bekleyin<br>
6- arka planı silinmiş fotografınız picture dizininin completed dizininden bulabilirsiniz

# PİCTURE = ARKA PLANI SİLİNECEK RESİMİN DİZİNİ<br>
# COMPLETED = ARKA PLANI SİLİNMİŞ RESİMİN DİZİNİ

# KAYNAK KODLARINDAN ÇALIŞTIRMA
Eğer programı .exe olarak kullanmayacaksanız şu program ve kütüphaneleri kurmanız gerekir:

1. Python 3 -> https://www.python.org/downloads/
### NOT: Python 3'ü kurarken "Add Python 3.? to PATH" kısmını tikleyin:
![](https://opensource.com/sites/default/files/uploads/win-python-path.jpg)

2. CMD ve ya terminalinizi açın ve şu komutları giriniz: <br>
`pip install pillow` <br>
`pip install rembg` <br>

### Neden bu kütüphaneleri kuruyoruz?
Çünkü Python(bu programda kullanılmış programlama dili) ek kütüphanelere(programlama dilinin eklentisi gibi düşünebilirsiniz) ihtiyaç duyar. Bu program ise resim kütüphanesine ve o resmin arka planını silmemize yarayan kütüphane bir nevi programlama dili eklentisine ihtiyaç duyar. Eğer bu kütüphaneler kurulmazlarsa program hata verir ve çalışmaz.

3. CMD ve ya terminalimizi programın olduğu dizine(klasöre) getiriyoruz.<br> 
`cd <dosya_yolu>`<br>
eğer Windows Terminal kullanıyorsanız <sağ tık> Terminal'de aç seçeneğini seçebilirsiniz.

4. CMD veya terminalimize `python main.py` yazarak programımızı çalıştırıyoruz.
