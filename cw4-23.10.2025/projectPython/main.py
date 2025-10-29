from PIL import Image
import numpy as np
from numpy import dtype


def rysuj_pasy_pionowe_szare(w,h,grub,kolor_paska, kolor):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[:]=kolor
    ile = int(w / grub)
    for k in range(0,w,2*grub):
        tab[:,k:k+grub] = kolor_paska
    return Image.fromarray(tab)



zadanie1b = rysuj_pasy_pionowe_szare(120, 60, 8, 100, 200)
#zadanie1b.show()

def zadanie5():
    a = rysuj_pasy_pionowe_szare(300,200,10, 100,200)
    a = np.array(a, dtype=np.uint8)
    b = rysuj_pasy_pionowe_szare(300, 200, 18, 100, 200)
    b = np.array(b, dtype=np.uint8)
    c = rysuj_pasy_pionowe_szare(300, 200, 26, 100, 200)
    c = np.array(c, dtype=np.uint8)

    resultArray = np.ones((300,200,3), dtype=np.uint8)

    for i in range(300):
        for j in range(200):
            resultArray[i,j,0] = a[i,j]
            resultArray[i,j,1] = b[i,j]
            resultArray[i,j,2] = c[i,j]


zadanie5()