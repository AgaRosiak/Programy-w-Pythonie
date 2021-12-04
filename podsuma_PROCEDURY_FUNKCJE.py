x=int(input("podaj liczbe1 "))
y=int(input("podaj liczbe2 "))
oblicz=0
def wykonaj_dzialanie (a,b):
    if x % y == 0:
        print("parzysta")
    else:
        print("nieparzysta")
   return oblicz
i=wykonaj_dzialanie(x,y)
print(i)


