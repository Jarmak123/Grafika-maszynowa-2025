from PIL import Image
import numpy as np
from numpy import dtype


def rysuj_ramke_szare(w,h,grub,kolor_ramki, kolor): #kolor od 0 do 255
    t = (h,w)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor_ramki # wypełnienie szarym kolorem
    tab[grub:h-grub, grub:w-grub] = kolor #wypełnienie tablicy pozostałym kolorem o wartość kolor
    return Image.fromarray(tab)

im_ramka = rysuj_ramke_szare(120,60,8,100,200)
#im_ramka.show()

def rysuj_pasy_poziome_szare(w,h,grub,zmiana_koloru):
    t = (h,w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(h/grub)
    for k in range(ile):
        for g in range(grub):
            i =k*grub+g
            for j in range(w):
                tab[i,j]=(k+zmiana_koloru)%256

    return Image.fromarray(tab)

im_paski = rysuj_pasy_poziome_szare(100,246,1,10)
#im_paski.show()

def rysuj_ramke_kolor(w,h,grub,kolor_ramki,kolor_tla):
    t = (h,w,3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor_ramki
    tab[grub:h-grub, grub:w-grub, 0] = kolor_tla[0]
    tab[grub:h-grub, grub:w-grub, 1] = kolor_tla[1]
    tab[grub:h - grub, grub:w - grub, 2] = kolor_tla[2]

    return Image.fromarray(tab)

im_ramka_kolor = rysuj_ramke_kolor(120,60,8,[0,0,255],[100,200,0])
#im_ramka_kolor.show()

def rysuj_pasy_poziome_3kolory(w,h,grub):
    t = (h,w,3)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(h/grub)
    for k in range(ile):
        for g in range(grub):
            i = k*grub+g
            for j in range(w):
                if k%3==0:
                    tab[i,j]=[255,0,0]
                elif k%3==1:
                    tab[i,j]=[0,255,0]
                else:
                    tab[i,j]=[0,0,255]

    return Image.fromarray(tab)

obraz1 = rysuj_pasy_poziome_3kolory(200,100,10)
#obraz1.show()






#zadanie1

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

zadanie1a = rysuj_ramki_szare(120, 60, 8, 100, 200)
#zadanie1a.show()

def rysuj_pasy_pionowe_szare(w,h,grub,kolor_paska, kolor):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[:]=kolor
    ile = int(w / grub)
    for k in range(ile):
        tab[k:grub-k, grub:h - grub] = kolor_paska
    return Image.fromarray(tab)


zadanie1b = rysuj_pasy_pionowe_szare(120, 60, 8, 100, 200)
zadanie1b.show()


