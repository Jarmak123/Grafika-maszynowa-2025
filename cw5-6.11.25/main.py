from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("rms ", s.rms)  # pierwiastek średniokwadratowy
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe
    print("")

def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()

#ZADANIE 1
#a
img = Image.open("im.png")
img_tab = np.asarray(img)
#statystyki(img)
r_img_tab = img_tab[:,:,0].copy()
g_img_tab = img_tab[:,:,1].copy()
b_img_tab = img_tab[:,:,2].copy()
#rysuj_histogram_RGB(img)
#b
r= np.sum(img_tab[:,:,0] == 155)
g= np.sum(img_tab[:,:,1] == 155)
b= np.sum(img_tab[:,:,2] == 155)
#print(r,g,b)
#c
def zlicz_piksele(obraz,kolor):
    img = Image.open(obraz)
    kolor = np.array(kolor)
    img_tab = np.asarray(img)
    licznik=0

    for wiersz in img_tab:
        for piksel in wiersz:
            if np.array_equal(piksel, kolor):
                licznik += 1

    return licznik

#print(zlicz_piksele("im.png",[155,155,155]))

#ZADANIE2
#a
img_jpeg = Image.open("im.jpeg")
#statystyki(img_jpeg)
#print("Obrazy się różnią ze względu na ich rozszerzenia i możliwości tych rozszerzeń")
#b
img_chops=ImageChops.difference(img_jpeg, img)
#img_chops.show()
#c
img_jpegx2 = Image.open("im2x.jpeg")
#statystyki(img_jpegx2)
#print("Zmieniło się odchylenie standardowe, średnia oraz pierwiastek średniokwadratowy")

#ZADANIE3
#a
img = Image.open("im.png")
img_t = np.asarray(img)
t_r = img_t[:,:,0].copy()
t_g = img_t[:,:,1].copy()
t_b = img_t[:,:,2].copy()
img_r = Image.fromarray(t_r)
img_g = Image.fromarray(t_g)
img_b = Image.fromarray(t_b)
# img_r.save("im_r.png")
# img_g.save("im_g.png")
# img_b.save("im_b.png")
img_rr = Image.open("im_r.png")
img_gg = Image.open("im_g.png")
img_bb = Image.open("im_b.png")
im1 = Image.merge("RGB", (img_rr, img_gg, img_bb))
im1.show()
ImageChops.difference(img, im1).show()
#c
# przedstawienie 4 obrazów w jednym oknie plt
plt.figure(figsize=(16, 16))
plt.subplot(2,2,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(im1)
plt.axis('off')
plt.subplot(2,2,2)
plt.imshow(r, "gray")
plt.axis('off')
plt.subplot(2,2,3)
plt.imshow(g, "gray")
plt.axis('off')
plt.subplot(2,2,4)
plt.imshow(b, "gray")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('figura1.png')
plt.show()