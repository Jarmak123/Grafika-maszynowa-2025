from PIL import Image
import numpy as np
from numpy import dtype

def rysuj_ramki_szare(w,h,grub, kolor_ramki, kolor):
    mem = kolor_ramki
    t = (h,w)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor
    ile = int(min(h,w)/(2*grub)+1)
    for i in range(ile):
        if i%2==0:
            kolor_ramki=mem
        else:
            kolor_ramki=kolor
        tab[i*grub:h-i*grub,i*grub: w-i*grub] = kolor_ramki

    return Image.fromarray(tab)

img1=rysuj_ramki_szare(300,300,1, 200, 100)
#img1.save("ramki.bmp")

def rysuj_pasy_pionowe_szare(w,h,grub,kolor_paska, kolor):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[:]=kolor
    ile = int(w / grub)
    for k in range(0,w,2*grub):
        tab[:,k:k+grub] = kolor_paska
    return Image.fromarray(tab)

img2 = rysuj_pasy_pionowe_szare(120, 60, 8, 100, 200)
#img2.save("paski.bmp")

def negatyw(obraz):
    if (obraz.mode not in ('RGB','1','L')):
        return None

    tab = np.asarray(obraz)
    tab = tab.copy()
    for i in range(tab.shape[0]):
        for j in range(tab.shape[1]):
            if(obraz.mode=='1'):
                if (tab[i,j] == 0):
                    tab[i,j] = 1
                else:
                    tab[i,j] = 0
            else:
                tab[i,j] = 255 - tab[i,j]

    return Image.fromarray(tab)







