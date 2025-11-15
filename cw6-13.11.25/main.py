from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint

#zadanie6
def czy_identyczne(obraz1, obraz2):
    img1_tab = np.array(obraz1)
    img2_tab = np.array(obraz2)

    if(obraz1.mode != obraz2.mode):
        return "Obrazy nie są identyczne - obrazy mają różne tryby"
    if(obraz1.size != obraz2.size):
        return "Obrazy nie są identyczne - obrazy mają różne wielkości"
    if np.array_equal(img1_tab, img2_tab):
        return "Obrazy są identyczne"
    else:
        return "Obrazy nie są identyczne - różne wartości pikseli"
#a
bek1 = Image.open("beksinski.png")
bek2 = Image.open("beksinski1.png")
bek3 = Image.open("beksinski2.png")
bek4 = Image.open("beksinski3.png")

print(czy_identyczne(bek1, bek1))
print(czy_identyczne(bek1, bek2))
print(czy_identyczne(bek1, bek3))
print(czy_identyczne(bek1, bek4))

#zadanie7
def pokaz_roznice(obraz_wejsciowy):
    t_obraz_wejsciowy = np.asarray(obraz_wejsciowy)
    h,w,d = t_obraz_wejsciowy.shape
    obraz_wynikowy = np.zeros((h, w, d))

    for i in range(h):
        for j in range(w):
                obraz_wynikowy[i][j] = (t_obraz_wejsciowy[i][j]/np.max(t_obraz_wejsciowy[i][j])) * 255

    Image.fromarray(obraz_wynikowy)
    return obraz_wynikowy
#a
# im_jpg3 = Image.open("im_jpg3.jpg")
# im = Image.open("im.jpg")
# print(czy_identyczne(im, im_jpg3))
# diff = ImageChops.difference(im_jpg3, im)
# #diff.save("diff.jpg")
# pokaz_roznice(diff)
