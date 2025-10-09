from PIL import Image
import numpy as np

#Z pliku tablica.txt utwórz obraz w trybie '1'.  W odpowiedzi wklej polecenia, które prowadziły do utworzenia obrazu.
#Zastosuj do tego obrazu funkcję rysuj_ramke_w_obrazie(obraz, 40) oraz wstaw otrzymany obraz.

img = np.loadtxt('tablica.txt', dtype=np.bool_)

crt_img = Image.fromarray(img)
#crt_img.save('test.bmp')

def rysuj_ramke_w_obrazie(obraz, grub):
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h,w = tab_obraz.shape
    for i in range(h):
        for j in range(grub):
            tab_obraz[i][j]=0
        for j in range(w-grub,w):
            tab_obraz[i][j]=0
    for i in range(w):
        for j in range(grub):
            tab_obraz[j][i]=0
        for j in range(h-grub,h):
            tab_obraz[j][i]=0

    tab1 = tab_obraz.astype(np.bool_)
    return Image.fromarray(tab1)

rysuj_ramke_w_obrazie(crt_img, 20).save('crt.bmp')
