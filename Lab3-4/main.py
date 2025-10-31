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

def koloruj_w_paski(obraz, grub):
    if(obraz.mode!='1'):
        return None
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape

    tab = np.ones((h, w, 3), dtype=np.uint8) * 255

    rgb = [[255, 0, 0],[0, 255, 0],[0, 0, 255]]

    k = 0
    for i in range(h):
        if i % grub == 0 and i!=0:
            k = (k + 1) % len(rgb)
        for j in range(w):
            if t_obraz[i, j] == 0:
                tab[i, j] = rgb[k]

    return Image.fromarray(tab)

def rysuj_pasy_pionowe_szare(w,h,grub,kolor_paska, kolor):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[:]=kolor
    ile = int(w / grub)
    for k in range(0,w,2*grub):
        tab[:,k:k+grub] = kolor_paska
    return Image.fromarray(tab)

r = np.asarray(rysuj_pasy_pionowe_szare(300, 200, 10, 100, 200))
g = np.asarray(rysuj_pasy_pionowe_szare(300, 200, 18, 100, 200))
b = np.asarray(rysuj_pasy_pionowe_szare(300, 200, 26, 100, 200))

tab_rgb = np.zeros((200, 300, 3), dtype=np.uint8)

tab_rgb[:, :, 0] = r
tab_rgb[:, :, 1] = g
tab_rgb[:, :, 2] = b

# obraz_rgb = Image.fromarray(tab_rgb)
# obraz_rgb.save('obraz6.png')
# obraz_rgb.show()
# r = Image.fromarray(r)
# g = Image.fromarray(g)
# b = Image.fromarray(b)
# r.show()
# g.show()
# b.show()
# print(obraz_rgb.mode)

def rysuj_po_skosie_szare(w,h, a, b):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a*i + b*j) % 256
    return tab

a = rysuj_po_skosie_szare(300, 200, 5, 11)
a_ext = np.expand_dims(a, axis=-1)
combined = np.concatenate((tab_rgb, a_ext), axis=-1)
rgba_img = Image.fromarray(combined)
# rgba_img.show()
# rgba_img.save('obraz7.png')


def rgb_to_cmyk(rgb_array):
    # Przekształć wartości RGB na zakres [0, 1]
    rgb = rgb_array.astype(float) / 255
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]

    # Oblicz kanał Kk (black)
    k = 1 - np.max(rgb, axis=2)

    # Uniknij dzielenia przez zero
    c = (1 - r - k) / (1 - k + 1e-8)
    m = (1 - g - k) / (1 - k + 1e-8)
    y = (1 - b - k) / (1 - k + 1e-8)

    # Zastąp NaN (dla czystej czerni) zerami
    c[np.isnan(c)] = 0
    m[np.isnan(m)] = 0
    y[np.isnan(y)] = 0

    # Przekształć na zakres [0, 255]
    cmyk = np.stack((c, m, y, k), axis=2) * 255
    return cmyk.astype(np.uint8)

t_cmyk = rgb_to_cmyk(tab_rgb)

img_cmyk = Image.fromarray(t_cmyk, mode='CMYK')
img_cmyk.show()
img_cmyk.save("obraz8.tiff")
tab_rgb_r = tab_rgb[:, :, 0]
img_rgb_r = Image.fromarray(tab_rgb_r)
img_rgb_r.save("r.png")
img_cmyk_c = t_cmyk[:, :, 0]
img_cmyk_c = Image.fromarray(img_cmyk_c)
img_cmyk_c.save("c.png")