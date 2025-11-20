from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#zadnaie1
obraz=Image.open("im.png")
inicjaly=Image.open("inicjaly.bmp")

#zadanie2
#a
def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):

    h_b, w_b= obraz.size
    h_w, w_w = inicjaly.size

    n_p = max(0, n)
    m_p = max(0, m)
    n_k = min(h_b, n + h_w)
    m_k = min(w_b, m + w_w)

    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            if inicjaly.getpixel((i-n, j-m)) == 0:
                obraz.putpixel( (i , j) , kolor)
    return obraz

# wstaw_inicjaly(obraz,inicjaly,1059,640,(255,0,0)).save("obraz1.png")
# wstaw_inicjaly(obraz,inicjaly,1059,640,(255,0,0)).show()

#b
def wstaw_inicjaly_maska(obraz, inicjaly, m, n):
    h_b, w_b = obraz.size
    h_w, w_w = inicjaly.size

    n_p = max(0, n)
    m_p = max(0, m)
    n_k = min(h_b, n + h_w)
    m_k = min(w_b, m + w_w)

    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            if inicjaly.getpixel((i - n, j - m)) == 0:
                obraz.putpixel((i, j), (255-obraz.getpixel((i, j))[0],255-obraz.getpixel((i, j))[1],255-obraz.getpixel((i, j))[2]))
    return obraz

wstaw_inicjaly_maska(obraz,inicjaly,529,320).show()

#zadnaie3
def wstaw_inicjaly_load(obraz, inicjaly, m, n,kolor):
    h_b, w_b= obraz.size
    h_w, w_w = inicjaly.size

    n_p = max(0, n)
    m_p = max(0, m)
    n_k = min(h_b, n + h_w)
    m_k = min(w_b, m + w_w)

    pix_obraz = obraz.load()
    pix_inicjaly = inicjaly.load()

    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            if inicjaly.getpixel((i-n, j-m)) == 0:
                obraz.putpixel( (i , j) , kolor)
    return obraz

def wstaw_inicjaly_maska(obraz,inicjaly,m,n,x,y,z):
    h_b, w_b = obraz.size
    h_w, w_w = inicjaly.size

    n_p = max(0, n)
    m_p = max(0, m)
    n_k = min(h_b, n + h_w)
    m_k = min(w_b, m + w_w)

    pix_obraz = obraz.load()
    pix_inicjaly = inicjaly.load()

    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            if pix_inicjaly[i-n][j - m] == 0:
                pix_obraz[i][j][0]= pix_obraz[i][j][0]-x
                pix_obraz[i][j][1] =pix_obraz[i][j][1]-y
                pix_obraz[i][j][2] =pix_obraz[i][j][2]-z
    return obraz



