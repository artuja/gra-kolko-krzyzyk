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


DrukujPlansze(PlanszaDoGry)