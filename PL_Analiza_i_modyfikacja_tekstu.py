# PROJEKT : ANALIZA I MODYFIKACJA TEKSTU
# DATA    : 5.12.2023
# KODOWAL : Kamil Sulewski

print()
print("PROGRAM DO ANALIZY I MODYFIKACJI LUB CENZUROWANIA TEKSTU W PLIKACH TEKSTOWYCH")
print(" _________________")
print("| 1 = ANALIZA     |")
print("| 2 = MODYFIKACJA |")
print("| 3 = CENZURA     |")
print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
typ=input("wybierz | 1 | albo | 2 | lub | 3 | : ")

try:
    if int(typ)!=1 and int(typ)!=2 and int(typ)!=3 :
        print()
        print("Ops... zle wpisales...")
        print("masz do wyboru tylko |1|, |2|, |3|")
        print("ZACZNIJMY JESZCZE RAZ")

    if int(typ)==1 :
        print("ANALIZA - Program ktory poda ilosc wystepowania wskazanej frazy")
        import os
        sciezka = os.getcwd()
        print()
        print("Obecnie znajdujesz sie w katalogu o sciezce dostepu :")
        print(sciezka)
        print()
        print("Jesli chcesz podac tylko nazwe pliku to musisz wybrany plik przegrac do katalogu obecnego czyli wyswietlonego wyzej...")
        print("W przeciwnym wypadku podaj pelna sciezke dostepu wraz z nazwa pliku...")
        analiza = input("Podaj sciezke dostepu do badanego pliku lub  nazwe: ")
        plik = open(analiza, "r")
        fraza = input("Podaj szukana fraze: ")
        test=plik.read()

        # definiujemy zmienne
        c = 0
        w = 0
        l = 0
        f = 0

        # wyliczamy ilosc fraz
        f = test.split(fraza)
        f = (len(f))-1
        if f==0 :
            print()
            print("  -----  UWAGA  -----")
            print("NIE ZNALEZIONO TWOJEJ FRAZY")
            print()
        else:
            print()
            print("Ilosc wyszukanych fraz ktora podales to: " + str(f))
            print()

        # wyliczamy ilosc znakow w pliku
        for element in test:
            c += 1
        print("Ilosc znakow w pliku to: " + str(c))

        # wyliczamy ilosc slow
        w = test.split()
        w = len(w)
        print("Ilosc wszystkich slow w tym pliku to: " + str(w))

        # wyliczamy % ktory stanowi wskazany wyraz w stosunku do calosci tekstu
        #policz = ((str(f))*100 )/ (str(w))
        #print("TWOJA FRAZA STANOWI"+policz+"% calosci")

        # wyliczamy ilosc linii
        l = len(test.splitlines())
        print("Ilosc linii w podanym pliku : " + str(l))
        print()

        # wyliczamy % ktory stanowi wskazany wyraz w stosunku do calosci tekstu
        if f>0:
            policz = f*100 / w
            print("TWOJA FRAZA STANOWI",round(policz, 2), "% w stosunku do wszystkich wyrazow w tekcie")


        plik.close()

    if int(typ)==2 :
        print("MODYFIKACJA - Program ktory znajdzie podana fraze i wymieni na nowa ktora wpiszesz")
        import os
        sciezka = os.getcwd()
        print()
        print("Obecnie znajdujesz sie w katalogu o sciezce dostepu :")
        print(sciezka)
        print()
        print("Jesli chcesz podac tylko nazwe pliku to musisz wybrany plik przegrac do katalogu obecnego czyli wyswietlonego wyzej...")
        print("W przeciwnym wypadku podaj pelna sciezke dostepu wraz z nazwa pliku...")
        modyfikacja = input("Podaj sciezke dostepu do badanego pliku lub  nazwe: ")
        plik = open(modyfikacja, "r")
        fraza = input("Podaj szukana fraze ktora ma byc zamieniona: ")
        test = plik.read()
        fraza2 = input("Podaj nowa fraze: ")

        modyfikacja2 = modyfikacja.replace(".", "new.")

        import re
        input = open(modyfikacja).read()
        output = open(modyfikacja2, "w")
        output.write(re.sub((fraza), (fraza2), input))
        output.close()
        print()
        print("GOTOWE! :) ")
        print()

        # definiujemy zmienna
        f = 0

        # wyliczamy ilosc fraz
        f = test.split(fraza)
        f = (len(f)) - 1

        if f==0 :
            print()
            print("  -----  UWAGA  -----")
            print("NIE ZNALEZIONO TWOJEJ FRAZY")
            print()
        else:
            print()
            print("Ilosc wyszukanych fraz ktora podales to: " + str(f))
            print()

            # wyliczamy ilosc slow
            w = test.split()
            w = len(w)

            # wyliczamy % ktory stanowi wskazany wyraz w stosunku do calosci tekstu
            if f > 0:
                policz = f * 100 / w
                print("TWOJA FRAZA STANOWI", round(policz, 2), "% w stosunku do wszystkich wyrazow w tekscie")

        print()
        print("Zmodyfikowany plik zostal zapisany w tym samym katalogu i w tym samym formacie z dopiskiem '*new.*' ")

    if int(typ) == 3:
        print("CENZURA - Program do cenzurowania textu w plikach")
        import os
        sciezka = os.getcwd()
        print()
        print("Obecnie znajdujesz sie w katalogu o sciezce dostepu :")
        print(sciezka)
        print()
        print("Jesli chcesz podac tylko nazwe pliku to musisz wybrany plik przegrac do katalogu obecnego czyli wyswietlonego wyzej...")
        print("W przeciwnym wypadku podaj pelna sciezke dostepu wraz z nazwa pliku...")
        cenzura = input("Podaj sciezke dostepu do  pliku lub  nazwe: ")
        plik = open(cenzura, "r")
        wyraz = input("Podaj wyrazy ktory chcesz ocenzurowac: ")
        test = plik.read()
        wyraz2 = input("Podaj czym chcesz zastapic wyrazy wulgarne: ")

        cenzura2 = cenzura.replace(".", "cenzura.")

        import re
        input = open(cenzura).read()
        output = open(cenzura2, "w")
        output.write(re.sub('|'.join(map(re.escape, substitutions.keys())),
                       lambda match: substitutions[match.group()],
                       text))
        #output.write(re.sub((wyraz),(wyraz2), input))
        output.close()




        # Przykładowe dane

        zamiana = {wyraz: wyraz2}








        print()
        print("GOTOWE! :) ")
        print()

        # definiujemy zmienna
        x = 0

        # wyliczamy ilosc wyrazow
        x = test.split(wyraz)
        x = (len(x)) - 1

        if x==0 :
            print()
            print("  -----  UWAGA  -----")
            print("NIE ZNALEZIONO TWOJEJ FRAZY")
            print("   BRAK DOKONANYCH ZMIAN   ")
        else:
            print()
            print("Ilosc ocenzurowanych wyrazow ktora podales: to " + str(x))
            print()

        # wyliczamy ilosc cenzur
        y=test.split()
        y=len(y)

        # wyliczamy % ktory stanowi wskazanq cenzura w stosunku do calosci tekstu
        if x > 0:
            policz = x * 100 / y
            print("TWOJA CENZURA STANOWI", round(policz, 2), "% w stosunku do wszystkich wyrazow w tekscie")

    print()
    print("Ocenzurowany plik zostal zapisany w tym samym katalogu i w tym samym formacie z dopiskiem '*cenzura.*' ")
except:
    print("Ops... cos poszlo nie tak...")
    print("Prawdopodobnie nie znaleziono pliku w danej sciezce lub zle wpisales wybor menu")
    print("OBSLUGA PLIKOW *.txt lub *.py")
    print("ZACZNIJMY JESZCZE RAZ")
