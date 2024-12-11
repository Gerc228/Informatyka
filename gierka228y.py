from random import randint, choice 

name = input('podaj swoie imie :')
life = 200
szczęście = 200
print(f" witam ciebie {name} ")
print("jestes nwm gdzie ale fajnie tu jest ))")
print("jako biznesmen masz różne ataki takie jak ")
print("Tu mogła byc wasza reklamka:)")
print(szczęście)
print(life)

def zwykły_atak():
    return randint(1,5)

def atak_money():
    global szczęście
    if szczęście < 10:
        print("-"*40)
        print("niemasz siły na użycie tego ataku ")
        return 0 
    szczęście -= 10
    return randint(8,20)

def atak_dolars():
    global szczęście
    if szczęście < 5:
        print("-"*40)
        print("niemasz siły do użycia tego ataku ")
        return 0 
    szczęście -= 4 
    return randint(0,10)

def atak_euro():
    global szczęście
    if szczęście < 4:
        print("-"*40)
        print("niemasz siły do użycia tego fajnego ataku")
        return 0 
    szczęście -= 5
    return randint(4,8)

def atak_dircham():
    global szczęście 
    if szczęście < 1:
        print("-"*40)
        print("niemasz wystarczającej siły bo to jest za droge")
        return 0 
    szczęście -= 3
    return randint(1,4)

def atak_mieczem():
    global szczęście 
    if szczęście < 2:
        print("-"*40)
        print("niemasz siły by podnieść mieczu")
        return 0 
    szczęście -= 2 
    return randint(2, 8)

def atak_lukiem():
    global szczęście 
    if szczęście < 1:
        print("-"*40)
        print("nie starczy ci siły by puszczyc strzałe")
        return 0 
    szczęście -= 1 
    return randint(4, 18)

def napij_się_koli():
    global szczęście 
    if szczęście < 100:
        print("-"*40)
        return 0
    szczęście += 5
    return(5)

def napij_się_wody():
    global szczęście
    if szczęście < 100:
        print("-"*40)
        return 0 
    szczęście += 10
    return(10)

def napij_się_fanty():
    global szczęście 
    if szczęście < 100:
        print("-"*40)
        return 0
    szczęście += 6
    return(6)

def napij_się_sosu():
    global szczęście 
    if szczęście < 100:
        print("-"*40)
        return 0
    szczęście += 1
    return(1)

def napij_się_herbatki():
    global szczęście 
    if szczęście < 100:
        print("-"*40)
        return 0
    szczęście += 2
    return(2)

def napij_się_kawy():
    global szczęście 
    if szczęście < 100:
        print("-"*40)
        return 0
    szczęście += 3
    return(3)

def petarda():
    global szczęście 
    if szczęście < 100:
        print("-"*40)
        return 0
    szczęście += 5
    return(3)

def mega_petarda():
    global szczęście 
    if szczęście < 100:
        print("-"*40)
        return 0
    szczęście += 7
    return(5)

def super_petarda():
    global szczęście 
    if szczęście < 100:
        print("-"*40)
        return 0
    szczęście += 9
    return(7)

def bomba():
    global szczęście 
    if szczęście < 100:
        print("-"*40)
        return 0
    szczęście += 10
    return(8)

def super_bomba():
    global szczęście 
    if szczęście < 100:
        print("-"*40)
        return 0
    szczęście += 15
    return(13)

def mega_bomba():
    global szczęście 
    if szczęście < 100:
        print("-"*40)
        return 0
    szczęście += 20
    return(20)

def Kula_z_powierzem():
    global szczęście 
    if szczęście < 100:
        print("-"*40)
        return 0
    szczęście += 1
    return(5)

def Kula_z_ogniem():
    global szczęście 
    if szczęście < 100:
        print("-"*40)
        return 0
    szczęście += 1
    return(10)


    

def wybieranie_ataków():
    print("wybierz atak:")
    print("-"*40)
    print("A wykonaj zwykły atak")
    print("-"*40)
    print("B wykonaj atak money")
    print("-"*40)
    print("C wykonaj atak dolars")
    print("-"*40)
    print("D wykonaj atak euro")
    print("-"*40)
    print("E wykonaj atak dircham")
    print("-"*40)
    print("F wykonaj atak mieczem ")
    print("-"*40)
    print("H wykonaj atak łukiem")
    print("-"*40)
    print("przywróć siłe :")
    print("-"*40)
    print("I napij się koli ")
    print("-"*40)
    print("J napij się wody ")
    print("-"*40)
    print("K napij się fanty ")
    print("-"*40)
    print("L napij się sosu ")
    print("-"*40)
    print("Z napij się herbatki ")
    print("-"*40)
    print("X napij się kawy ")
    print("-"*40)
    print("C napij podpal petarde ")
    print("-"*40)
    print("V napij podpal mega petarde ")
    print("-"*40)
    print("B napij podpal super petarde ")
    print("-"*40)
    print("N napij podpal bombe ")
    print("-"*40)
    print("M napij podpal super bombe ")
    print("-"*40)
    print("SUPER podpal mega bombe ")
    print("-"*40)
    print("KULA1 zrob kule z powietrzem ")
    print("-"*40)
    print("KULA2 zrob kule z ogniem")
    print("-"*40)
    co = input().upper()
    if co == 'A':
        return zwykły_atak()
    elif co == 'B':
        return atak_money()
    elif co == 'C':
        return atak_dolars()
    elif co == 'D':
        return atak_euro()
    elif co == 'E':
        return atak_dircham()
    elif co == 'F':
        return atak_mieczem()
    elif co == 'H':
        return atak_lukiem()
    elif co == 'I':
        return napij_się_koli()
    elif co == 'J':
        return napij_się_wody()
    elif co == 'K':
        return napij_się_fanty()
    elif co == 'L':
        return napij_się_sosu()
    elif co == 'Z':
        return napij_się_herbatki()
    elif co == 'X':
        return napij_się_kawy()
    elif co == 'C':
        return petarda()
    elif co == 'V':
        return mega_petarda()
    elif co == 'B':
        return super_petarda()
    elif co == 'N':
        return bomba()
    elif co == 'M':
        return super_bomba()
    elif co == 'SUPER':
        return mega_bomba()
    elif co == 'KULA1':
        return Kula_z_powierzem()
    elif co == 'KULA2':
        return Kula_z_ogniem()
    else:
        print("co ty nic nie wybrałes")
        return 0 


def wybieranie_przeciwnikow():
    opponent = [
        ["kot" , 15,1,3],
        ["pies", 20,7,3],
        ["drakon", 16,4,3],
        ["verybigmoney", 3, 8, 13]
    ]
    return choice(opponent)

liczba_pokonanych_wrogów = 0 

def biznesmen ():
    if opponent > 29:
        biznesmen = [
            ["biznesmen", 25, 40,30]
        ]

while life > 0:
    opponent = wybieranie_przeciwnikow()
    print("-"*40)

    while opponent[1] > 0 and life > 0:
        print(f"{name} chce zabic {opponent[0]}")
        print(f"noname ma  {opponent[1]} HP i zadaje ci {opponent[2]} ")

        life -= opponent[2]
        if life <= 0:
            break
        elif liczba_pokonanych_wrogów >= 30:
            print("ale jesteś mocny")

        print(f"Masz {life} HP i {szczęście} szczęścia")
        atak = wybieranie_ataków()
        opponent[1] = atak
        print(f"Zadałeś {atak} mocy")

    if opponent[1] <= 0:
        print('Zrobiłeś to!')
        liczba_pokonanych_wrogów += 1

    if liczba_pokonanych_wrogów > 20:
        print("dałeś rade) ")
    elif liczba_pokonanych_wrogów > 15:
        print("Ale fajnie!")
    elif liczba_pokonanych_wrogów > 10:
        print("No prawie")
    elif liczba_pokonanych_wrogów > 5:
        print("Ale slabo")
    elif liczba_pokonanych_wrogów < 5:
        print(" No i nic nie zrobiłeś  ")

print("KONIEC TEGO")
print(f"Zabiłeś {liczba_pokonanych_wrogów} nie fajnych ludzi")