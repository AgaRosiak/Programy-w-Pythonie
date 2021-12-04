#M=40
#T=90
def roznica_wieku(x,y):
    #if M<T :
        #roznica = M - T #tutaj jest błąb. powinno być T-M
    #elif T==M :
        #roznica = M - T
    #else:
    roznica = x - y
    return roznica
#wynik=roznica_wieku (M,T)
#print(wynik)

#test do tego zadania powyzej
def przetestuMojaFunkcje():
    #1, przygotuj dane testowe
    daneTestowe1 = 10
    daneTestowe2 = 20

 #2. uruchom testowana funkcje
    wynik = roznica_wieku(daneTestowe2, daneTestowe1)
    if wynik < 0:
        print("PROBLEM!")
    else:
        print("OK")
przetestuMojaFunkcje()

#Zadanie 1
#Napisz prosty kalkulator, użytkownik podaje dwie liczby, a do obliczeń wykorzystuje operatory
#arytmetyczne. Wykorzystaj do zadania funkcje.

Liczba1 = int(input("Zosia podaj liczbe 1: "))
Liczba2 = int(input("Zosia podaj liczbe 2: "))
dzialanie = 0

def oblicz_suma (x,y):
    suma = x+y
    return suma
wynik = oblicz_suma(Liczba1, Liczba2)
print(wynik)

def oblicz_roznica (x,y):
    roznica = x-y
    return roznica
wynik = oblicz_roznica(Liczba1, Liczba2)
print(wynik)

def oblicz_iloczyn(x,y):
    iloczyn = x*y
    return  iloczyn
wynik=oblicz_iloczyn(Liczba1,Liczba2)
print(wynik)

def oblicz_iloraz (x,y):
    iloraz = y/x
    return iloraz
wynik = oblicz_iloraz(Liczba1, Liczba2)
print(wynik)

#Zadanie 2
#Napisz program wykorzystujący funkcję do obliczenia czy liczba podana przez użytkownika
#jest parzysta czy nieparzysta. Należy zastosować dzielenie modulo %.

Liczba = int(input("Twoja ulubiona liczba to: "))
rodzaj = 0
def ulubiona_liczba (x):
    if Liczba % 2 == 0:
        print("parzysta")
    else:
        print("nieparzysta")
        return rodzaj
y=ulubiona_liczba(Liczba)
print(y)

#Zadanie 3
#Napisz program wyznaczający największą z dwóch liczb podanych przez użytkownika.
#Do wyznaczenia największej liczby zastosuj funkcję, która ma zwrócić największą liczbę i wypisać
#ją na ekran.

L1=int(input("Daj pierwszą "))
L2=int(input("Daj drugą "))
wynik=0
def ta_wieksza (x,y):
    if L1 < L2:
        print(L2)
    elif L1 > L2:
        print(L1)
    else:
        print("Są równe !")
    return wynik
z=ta_wieksza(L1,L2)
print(z)
#Zadanie 4
#Napisz funkcję, która obliczy sumę liczb z listy [2 ,5, 9, 6, 4] wypisze wynik na ekran.

zbior=[2,5,9,6,4]
suma=0
def policz_suma (zbior):
    for x in zbior:
       suma += x
    return suma
x=policz_suma(zbior)
print(x)

zbior=[2,5,9,6,4]
def policz_suma (zbior):
    suma = 0
    for x in zbior:
        suma += x
    return suma
x=policz_suma(zbior)
print(x)

#def dodaj()
#def odejmij()
#def pomnoz()
#def podziel()

#Zadanie 1
#Napisz prosty kalkulator, użytkownik podaje dwie liczby, a do obliczeń wykorzystuje operatory
#arytmetyczne. Wykorzystaj do zadania funkcje.

def pomnoz(x,y):
    return x*y


operacja = input("Podaj działanie:(*/+-)")
LiczbaA = int(input("podaj liczbę A: "))
LiczbaB = int(input("podaj liczbę B: "))

def wykonaj_dzialanie():
    if operacja == '*':
      #return pomnoz(LiczbaA, LiczbaB)

        z = pomnoz(LiczbaA, LiczbaB)
        print(z)
   #pobierzDane()
#x=wykonaj_dzialanie()
#print(x)
wykonaj_dzialanie()