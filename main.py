# Tutaj będzie głowny kod gry
 
 # Definicja tablicy - plansza do gry
PlanszaDoGry = {'7': ' ', '8': ' ', '9': ' ',
                '4': ' ', '5': ' ', '6': ' ',
                '1': ' ', '2': ' ', '3': ' '}

KlawiszeGry = []

for key in PlanszaDoGry:
    KlawiszeGry.append(key)


# Drukuj plansze do gry
def DrukujPlansze(pole):
    print(f"{pole['7']}|{pole['8']}|{pole['9']}")
    print('-+-+-')
    print(f"{pole['4']}|{pole['5']}|{pole['6']}")
    print('-+-+-')
    print(f"{pole['1']}|{pole['2']}|{pole['3']}")


# DrukujPlansze(PlanszaDoGry)

def gra():
    gracz = "X"
    licznik = 0
    for i in range(10):
        DrukujPlansze(PlanszaDoGry)
        move = input(f'To jest twój ruch {gracz}. Wybierz gdzie chcesz postawic znak!')
        if PlanszaDoGry[move] == ' ':
            PlanszaDoGry[move] = gracz
            licznik  +=1
        else:
            print('Miejsce jest zajęte!\n Wstaw swój znak gdzieś indzej!')
            continue
        if licznik >= 5:
            if PlanszaDoGry['7'] == PlanszaDoGry['8'] == PlanszaDoGry['9'] != ' ':
                DrukujPlansze(PlanszaDoGry)
                print('\nKoniec gry!\n')
                print(f'Wygrał gracz: {gracz}')
                break
            elif PlanszaDoGry['4'] == PlanszaDoGry['5'] == PlanszaDoGry['6'] != ' ':
                DrukujPlansze(PlanszaDoGry)
                print('\nKoniec gry!\n')
                print(f'Wygrał gracz: {gracz}')
                break
            elif PlanszaDoGry['1'] == PlanszaDoGry['3'] == PlanszaDoGry['3'] != ' ':
                DrukujPlansze(PlanszaDoGry)
                print('\nKoniec gry!\n')
                print(f'Wygrał gracz: {gracz}')
                break
            elif PlanszaDoGry['7'] == PlanszaDoGry['4'] == PlanszaDoGry['1'] != ' ':
                DrukujPlansze(PlanszaDoGry)
                print('\nKoniec gry!\n')
                print(f'Wygrał gracz: {gracz}')
                break
            elif PlanszaDoGry['8'] == PlanszaDoGry['5'] == PlanszaDoGry['2'] != ' ':
                DrukujPlansze(PlanszaDoGry)
                print('\nKoniec gry!\n')
                print(f'Wygrał gracz: {gracz}')
                break
            elif PlanszaDoGry['9'] == PlanszaDoGry['6'] == PlanszaDoGry['3'] != ' ':
                DrukujPlansze(PlanszaDoGry)
                print('\nKoniec gry!\n')
                print(f'Wygrał gracz: {gracz}')
                break
            elif PlanszaDoGry['7'] == PlanszaDoGry['5'] == PlanszaDoGry['3'] != ' ':
                DrukujPlansze(PlanszaDoGry)
                print('\nKoniec gry!\n')
                print(f'Wygrał gracz: {gracz}')
                break
            elif PlanszaDoGry['9'] == PlanszaDoGry['5'] == PlanszaDoGry['1'] != ' ':
                DrukujPlansze(PlanszaDoGry)
                print('\nKoniec gry!\n')
                print(f'Wygrał gracz: {gracz}')
                break
            if licznik == 9:
                print('\n Gra zakończyła sie remisem!\n')
                DrukujPlansze(PlanszaDoGry)
            
        if gracz == 'X':
            gracz = 'O'
        else:
            gracz = 'X'
    restart  = input('Czy chcesz zagrać ponownie?/ (t/n)')
    if restart == 't' or restart == 'T':
        for key in KlawiszeGry:
            PlanszaDoGry[key] = ' '
        gra()

if __name__ == '__main__':
    gra()
