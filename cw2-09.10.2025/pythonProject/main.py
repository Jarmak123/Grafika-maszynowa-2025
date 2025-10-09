from PIL import Image  # Python Imaging Library
import numpy as np

inicjaly = Image.open("../materials/bs.bmp")

# print(inicjaly.mode)
# print(inicjaly.format)
# print(inicjaly.size)
#
# t_inizjaly = np.asarray(inicjaly)
# print(t_inizjaly.dtype)
# print(t_inizjaly.shape)

#inicjaly.show()

def rysuj_paski_w_obrazie(obraz, grubosc):
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = tab_obraz.shape
    print(tab_obraz.shape)
    print(h)
    print(w)
    for i in range(h):
        for j in range(grubosc):
            tab_obraz[i][j]=0
        for j in range(w-grubosc,w):
            tab_obraz[i][j]=0
    tab = tab_obraz.astype(bool)
    return Image.fromarray(tab)

#rysuj_paski_w_obrazie(inicjaly,10).show()

def rysuj_ramke(w,h,grubosc):
    t = (h,w)
    tab = np.zeros(t,dtype=np.uint8)
    tab[grubosc:h - grubosc, grubosc: w - grubosc] = 1
    tab1 = tab.astype(np.bool_)
    return Image.fromarray(tab1)

#rysuj_ramke(200,100,20).show()

def rysuj_pasy_poziome(w,h,grub):
    t=(h,w)
    tab = np.ones(t,dtype=np.uint8)
    ile = int(h/grub)
    for k in range(ile):
        for g in range(grub):
            i=k*grub+g
            for j in range(w):
                tab[i,j] = k%2
    tab=tab*255
    return Image.fromarray(tab)

#rysuj_pasy_poziome(100,180,20).show()

def wstaw_obraz(w,h,m,n,obraz):
    tab_obraz = np.asarray(obraz).astype(np.int_)
    h0, w0 = tab_obraz.shape
    t = (h,w)
    tab=np.zeros(t,dtype = np.uint8)
    n_k = min(h,n+h0)
    m_k = min(w, m+w0)
    n_p = max(0,n)
    m_p = max(0,m)
    for i in range(n_p, n_k):
        for j in range(m_p,m_k):
            tab[i][j] = tab_obraz[i-n][j-m]
    tab = tab.astype(bool)
    return Image.fromarray(tab)

#wstaw_obraz(200,100,-20,40,inicjaly).show()


#zadanie1
obraz = Image.open("../materials/inicjaly.bmp")
print(obraz.mode)
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

#rysuj_ramke_w_obrazie(obraz,10).show()

#zadanie2.1

def rysuj_ramki(w,h,grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(h / grub)
    zm=0
    for i in range(ile):
        if ile%2==0: zm=0
        else: zm=1
        for i in range(h):
            for j in range(grub):
                tab[i][j] = zm
            for j in range(w - grub, w):
                tab[i][j] = zm
        for i in range(w):
            for j in range(grub):
                tab[j][i] = zm
            for j in range(h - grub, h):
                tab[j][i] = zm
        h=h-grub
        w=w-grub


    tab1 = tab.astype(np.bool_)
    return Image.fromarray(tab1)

rysuj_ramki(200,100,10).show()







