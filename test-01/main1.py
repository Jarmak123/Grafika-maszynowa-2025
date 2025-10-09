# from PIL import Image
# import numpy as np
#
# # Wykonaj funkcję rysuj_ramki(80, 130, 5). Zapisz obraz w formacie bmp.   Otwórz w Paint a następnie zapisz w formacie JPEG. Pobierz informacje o otrzymanym obrazie i jego tablicy.
# #
# # W odpowiedzi wpisz kolejno, oddzielając średnikiem następujące informacje:
# #
# # tryb obrazu; rozmiar tablicy; wymiar tablicy; liczba elementów tablicy
#
# #RGB; (130, 80, 3); 3; 31200
#
# ###########################
# # Zastosuj 2 razy funkcję wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n), gdzie
# #
# # obraz_bazowy powstaje w wyniku funkcji rysuj_paski_pionowe(300, 200, 15)
# #
# # obraz_wstawiany  to inicjały własne (z lab1)
# #
# # 1.  m = 250, n =100
# #
# # 2.  m = 0, n = 50
# #
# #
# #
# # W odpowiedzi wstaw dwa otrzymane obrazy.
#
#
# ##############################
# # Wykonaj funkcję rysuj_paski_pionowe(200, 100, 10). Zapisz obraz w formacie bmp.   Otwórz w Paint a następnie zapisz w formacie JPEG. Pobierz informacje o otrzymanym obrazie i jego tablicy.
# #
# # W odpowiedzi wpisz kolejno, oddzielając średnikiem następujące informacje:
# #
# # tryb obrazu; wartość piksela (66,13); wartość elementu tablicy (97,20)
#
# #RGB; [0 0 0]; [1 1 1]
#
# #RGB; [1 1 1]; [1 1 1]
# ###############################
# # Opisz wymagania oraz wklej kod funkcji  rysuj_wlasne. Utwórz obraz z własnej funkcji i wstaw.
# ###############################
# # wstaw plik z kodem oraz wklej poniżej kod zawierający wszystkie funkcje wymagane w lab2.
#
# # def rysuj_ramki(w, h, grub):
# #     """
# #     Funkcja tworzy obraz czarno-biały (tryb 1),
# #     w którym występują na przemian czarne i białe ramki
# #     o grubości 'grub', licząc od krawędzi zewnętrznych obrazu.
# #     """
# #     tab = np.zeros((h, w), dtype=np.uint8)  # czarny obraz
# #
# #     liczba_ramek = min(w, h) // (2 * grub) + 1  # ile ramek zmieści się w obrazie
# #
# #     for k in range(liczba_ramek):
# #         if k % 2 == 0:
# #             kolor = 1  # biała ramka
# #         else:
# #             kolor = 0  # czarna ramka
# #         tab[k * grub: h - k * grub, k * grub: w - k * grub] = kolor
# #
# #     tab = tab.astype(bool)
# #     return Image.fromarray(tab)
# #
# #
# # # --- wykonanie funkcji ---
# # obraz = rysuj_ramki(80, 130, 5)
# #
# # # zapis obrazu w formacie BMP
# # obraz.save("ramki1.bmp")
#
#
# # def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
# #     """
# #     Wstawia obraz_wstawiany (z tłem) w miejsce (m, n)
# #     obrazu_bazowego. W razie przekroczenia granic – przycina.
# #     """
# #     # konwersja do tablic numpy
# #     tab_baza = np.asarray(obraz_bazowy).astype(np.uint8)
# #     tab_wstaw = np.asarray(obraz_wstawiany).astype(np.uint8)
# #
# #     # wymiary obrazów
# #     h_b, w_b = tab_baza.shape
# #     h_w, w_w = tab_wstaw.shape
# #
# #     # obliczanie zakresów — z przycinaniem, gdy wychodzi poza ramkę
# #     n_p = max(0, n)
# #     m_p = max(0, m)
# #     n_k = min(h_b, n + h_w)
# #     m_k = min(w_b, m + w_w)
# #
# #     # kopiowanie pikseli obrazu wstawianego
# #     for i in range(n_p, n_k):
# #         for j in range(m_p, m_k):
# #             tab_baza[i][j] = tab_wstaw[i - n][j - m]
# #
# #     # konwersja z powrotem do obrazu czarno-białego
# #     tab_baza = tab_baza.astype(bool)
# #     return Image.fromarray(tab_baza)
# #
# # #
# def rysuj_pasy_pionowe(w, h, grub):  # w, h - rozmiar obrazu
#     t = (h, w)  # rozmiar tablicy
#     tab = np.ones(t, dtype=np.uint8)
#     # ile pasów o grubości grub
#     ile = int(w / grub)
#     for k in range(ile):
#         for g in range(grub):
#             j = k * grub + g  # j - indeks kolumny, i - indeks wiersza
#             for i in range(h):
#                 tab[i, j] = k % 2  # naprzemienne wypełnianie kolumn
#     tab = tab * 255  # uzyskanie obrazu w skali szarości
#     return Image.fromarray(tab)
#
# #rysuj_pasy_pionowe(200, 100, 10).save("pasy_pionn.bmp")
# img = Image.open('pasy_pionn.bmp')
# imgarr = np.array(img)
# print(img.mode)
# print(imgarr[13][66])
# print(imgarr[97][20])
#
#
# # baza = Image.open("pasy_pion.bmp")
# # inicjaly = Image.open("inicjaly.bmp")
# #
# # wstaw_obraz_w_obraz(baza, inicjaly, 250, 100).save("zadanie3.1.bmp")
# # wstaw_obraz_w_obraz(wstaw_obraz_w_obraz(baza, inicjaly, 250, 100), inicjaly, 0, 50).save("zadanie3.2.bmp")
#
# #rysuj_pasy_pionowe(200, 100, 10).save("paski.bmp")
#
# # img = Image.open("paski.jpg")
# # img_arr = np.asarray(img)
# # print(img.getpixel((66,13)))
# # for i in range(img_arr.shape[0]):      # wiersze (wysokość)
# #     for j in range(img_arr.shape[1]):  # kolumny (szerokość)
# #         print(f"img_arr[{i}][{j}] = {img_arr[i][j]}")
# #     print()  # odstęp między wierszami
#
# # def rysuj_wlasne(w, h, grub):
# #     tab = np.ones((h, w), dtype=np.uint8)
# #
# #     srodek_x = w // 2
# #     srodek_y = h // 2
# #
# #     tab[h//4: h - (h//4), srodek_x - grub : srodek_x + grub + 1] = 0
# #
# #     tab[srodek_y - grub : srodek_y + grub + 1, w//4: w - (w//4)] = 0
# #
# #     tab = tab.astype(np.bool_)
# #     return Image.fromarray(tab)
# #
# # obraz_krzyz = rysuj_wlasne(200, 150, 20)
# # obraz_krzyz.show()
#
# # def rysuj_wlasne(w, h, roz):
# #     tab = np.ones((h, w), dtype=np.uint8)
# #
# #     for y in range(0, h, roz):
# #         for x in range(0, w, roz):
# #             if ((x // roz) + (y // roz)) % 2 == 0:
# #                 tab[y:y+roz, x:x+roz] = 0
# #
# #     tab = tab.astype(np.bool_)
# #     return Image.fromarray(tab)
# #
# # img= rysuj_wlasne(100,50,10)
# # img.show()
# # img.save("szachy.bmp")