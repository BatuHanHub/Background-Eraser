__author__ = "Thunderbolt"
__version__ = 1.0

# Fast Libs {
import shutil
import time
import os
# }

# Terminal clear command {
opeSys = os.name
# clear = ""

if opeSys == "nt":
    clear = "cls"

else:
    clear = "clear"
# }

# Select language
while True:
    print("""=== WELCOME! ===
Select your language
          
[1] Türkçe
[2] English\n""")
    
    language = str(input("My language is: "))

    if language == "1":
        textTitle = "=== PİCTURE DOSYASI ==="
        textSelPic = "Resim"
        textNFPic = "Hata: Hedef fotograf bulunamadı."
        textWelcome = f"""Otomatik arka plan siliciye hoşgeldiniz! Bu program ücretsiz, çapraz platform ve açık kaynak kodludur. GPL 3 ve ardı. Sürüm: {__version__}"""
        textSavePic = "Resim kaydedildi."
        textWait = "Resim kütüphaneleri yükleniyor, sadece bir dakika bekleyin..."
        textDelBG = "Resiminizin arka planı siliniyor..."
        textDelBGFinish = 'Resiminizin arka planı silindi ve kaydedildi. "completed" dizinine bakın.'
        textImageError = "Lütfen resim seçiniz! Resim uzantınızın .png, .jpg, .jpeg olması gerekiyor."
        break

    elif language == "2":
        textTitle = "=== PICTURE FILE ==="
        textSelPic = "Picture"
        textNFPic = "Error: Target photo not found!"
        textWelcome = f"""Welcome to the automatic background remover! This program is free, cross-platform and open source. GPL 3 and later. Version: {__version__}"""
        textSavePic = "Picture saved."
        textWait = "Loading picture librarys, just a moment wait..."
        textDelBG = "Erasing the background of your picture..."
        textDelBGFinish = 'The background of your picture has been deleted and saved. Look at "completed" directory.',
        textImageError = "Please select a picture! Your image extension needs to be .png, .jpg, .jpeg."
        break

    else:
        print("Error: Please write language number!")
        continue

os.system(clear)
print(textWelcome)
time.sleep(5)
os.system(clear)

print(textWait)

# slow libs {
from rembg import remove
from PIL import Image, UnidentifiedImageError
# } 

os.system(clear) # clearing terminal

os.chdir("picture") # changed directory picture

# user select a picture {
def selectPicture(): 
    global selPicture
    print(f"\t{textTitle}")
    for picture in os.listdir():
        print(picture)

    selPicture = str(input(f"\n{textSelPic}: "))
# }

# delete background and move to completed dir {
def delBG(targetPicture):
    try:
        os.system(clear)
        print(textDelBG)
        image = Image.open(targetPicture)
        newPicture = remove(image)
        newPicture.save(newPictureName)
        shutil.move(newPictureName, "completed")
        os.system(clear)
        print(textDelBGFinish)
        time.sleep(5)
        os.system(clear)

    except UnidentifiedImageError:
        print(f"{textImageError}")
# }

# main process {
while True:
    selectPicture()
    if selPicture in os.listdir():
        os.system(clear)
        uzanti = selPicture[-4:]
        if uzanti != ".png": # if photo not a png
            newPictureName = selPicture.replace(uzanti, ".png") # convert to png. exp: photo.jpg -> photo.png
        
        else:
            pass

        delBG(selPicture)
        os.system(clear)

    else:
        os.system(clear)
        time.sleep(1)
        print(f"{textNFPic}")
        continue

# }