#M=40
#T=90
def roznica_wieku(x,y):
    #if M<T :
        #roznica = M - T #tutaj jest błąb. powinno być T-M
    #elif T==M :
        #roznica = M - T
    #else:
    roznica = y-x
    return roznica
#wynik=roznica_wieku (M,T)
#print(wynik)

#test do tego zadania powyzej
def przetestuMojaFunkcje():
    #1, przygotuj dane testowe
    daneTestowe1 = 20
    daneTestowe2= 10

 #2. uruchom testowana funkcje
    wynik = roznica_wieku(daneTestowe2, daneTestowe1)
    if wynik < 0:
        print("PROBLEM!", wynik)
    else:
        print("OK", wynik)
przetestuMojaFunkcje()
