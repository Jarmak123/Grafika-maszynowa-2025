from PIL import Image
import numpy as np

#zadanie1
obraz = Image.open("inicjaly.bmp")
#print(obraz.mode)
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

def rysuj_ramki(w, h, grub):
    tab = np.zeros((h, w), dtype=np.uint8)
    liczba_ramek = min(w, h) // (2 * grub) + 1

    for k in range(liczba_ramek):
        if k % 2 == 0: kolor = 0
        else: kolor = 1
        tab[k * grub: h - k * grub, k * grub: w - k * grub] = kolor

    tab = tab.astype(np.bool_)
    return Image.fromarray(tab)

#rysuj_ramki(80,130,5).show()

#zadanie2.2

def rysuj_pasy_pionowe(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)
    for k in range(ile):
        for g in range(grub):
            j = k * grub + g
            for i in range(h):
                tab[i, j] = k % 2
    tab = tab * 255
    return Image.fromarray(tab)

#rysuj_pasy_pionowe(100,200,10).show()

#zadanie2.3

def rysuj_wlasne(w, h, grub):
    tab = np.ones((h, w), dtype=np.uint8)

    srodek_x = w // 2
    srodek_y = h // 2

    tab[h//4: h - (h//4), srodek_x - grub : srodek_x + grub + 1] = 0

    tab[srodek_y - grub : srodek_y + grub + 1, w//4: w - (w//4)] = 0

    tab = tab.astype(np.bool_)
    return Image.fromarray(tab)

#rysuj_wlasne(200, 150, 20).show()

#zadanie3

def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    tab_baz = np.asarray(obraz_bazowy).astype(np.uint8)
    tab_wst = np.asarray(obraz_wstawiany).astype(np.uint8)

    h_b, w_b = tab_baz.shape
    h_w, w_w = tab_wst.shape

    n_p = max(0, n)
    m_p = max(0, m)
    n_k = min(h_b, n + h_w)
    m_k = min(w_b, m + w_w)

    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab_baz[i][j] = tab_wst[i - n][j - m]

    tab_baz = tab_baz.astype(np.bool_)
    return Image.fromarray(tab_baz)



