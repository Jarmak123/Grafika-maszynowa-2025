from PIL import Image
import numpy as np

print("Informacje o obrazie")

img = Image.open("C:/users/local/Documents/inicjaly.bmp")
print("tryb: ", img.mode)
print("format: ", img.format)
print("rozmiar: ", img.size)

#img.show()

print("\nInformacje o tablicy obrazu")

img_data = np.asarray(img)

print("typ danych tablicy: ", img_data.dtype)
print("rozmiar tablicy: ", img_data.shape)
print("liczba elementów: ", img_data.size)
print("wymiar tablicy: ", img_data.ndim)
print("rozmiar wyrazu tablicy: ", img_data.itemsize)

print("pierwszy wyraz: ", img_data[0][0])
print("drugi wyraz: ", img_data[1][0])
print(img_data)

#tworzenie obrazu z tablicy img_data

crt_img = Image.fromarray(img_data)
#crt_img.show()

#wczytanie obrazu do tablicy z jednoczenym określeniem typu danych
img_data2 = img_data * 1
img_data2 = img_data.astype(np.int_)
img_data2 = img_data.astype(np.uint8)
print(img_data2)

crt_img2 = Image.fromarray(img_data2)
#crt_img2.show()
#crt_img2.save("saved_image.bmp")

t1 = np.loadtxt("C:/users/local/Documents/dane.txt", dtype=np.bool_)
t2 = np.loadtxt("C:/users/local/Documents/dane.txt", dtype=np.int_)
t3 = np.loadtxt("C:/users/local/Documents/dane.txt", dtype=np.uint8)
print("typ: ", t1.dtype)
print("rozmiar: ", t1.shape)
print("wymiar: ", t1.ndim)

print("\ntyp: ", t2.dtype)
print("rozmiar: ", t2.shape)
print("wymiar: ", t2.ndim)

print("\ntyp: ", t3.dtype)
print("rozmiar: ", t3.shape)
print("wymiar: ", t3.ndim)

print(t1)
print(t2)
print(t3)

# t1_text = open("t1.txt", "w")
# for rows in t1:
#     for item in rows:
#         t1_text.write(str(item)+" ")
#     t1_text.write("\n")
#
# t1_text.close()

print("\nZadanie-1\n")
print("zrobione")
print("\nZadanie-2\n")
print("Informacje o obrazie")

img = Image.open("C:/users/local/Documents/inicjaly.bmp")
print("tryb: ", img.mode)
print("format: ", img.format)
print("rozmiar: ", img.size)
print("\nZadanie-3\n")
zo_img = np.asarray(img)
zo_img = zo_img * 1

zo_txt = open("inicjaly.txt", "w")
for rows in zo_img:
    for item in rows:
        zo_txt.write(str(item)+" ")
    zo_txt.write("\n")

zo_txt.close()
print(zo_img)
print("\nZadanie-4\n")
img_data = np.asarray(img)
print("Dowolne miejsce: ",img_data[17][42])
print("Miejsce (50,30): ",img_data[30][50])
print("Miejsce (90,40): ",img_data[40][90])
print("Miejsce (99,0): ",img_data[0][99])
print("\nZadanie-5\n")






