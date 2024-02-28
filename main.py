# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 30 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 16 -> 5, 65 -> 44 , 78 -> 67, 72 -> 61
# -- sarkanas kāpnes ved uz augšu, 13 -> 22, 37 -> 46, 31 -> 50, 85 -> 94 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

from random import randint

step1=1
step2=1
rounds=1
while True:

    input("Player 1 rolls the dice:")

    dice1 = [randint(1,6) for i in range(1)] #for - creates a sheet with one random number from 1 to 6 - Dice!

    step1 += sum(dice1)

    print("player 1:", dice1, step1)

    if step1 >= 100: #if - checks whether the player has reached 100 points - Victory!
        print("PLAYER 1 won:", step1,"points!")
        break
    
    #Player 1 stairs!
    if (step1==16):
        step1 = 5
        print("Player 1: Blue staircase leads down to", step1,"!")
    if (step1==65):
        step1 = 44
        print("Player 1: Blue staircase leads down to", step1,"!")
    if (step1==78):
        step1 = 67
        print("Player 1: Blue staircase leads down to", step1,"!")
    if (step1==72):
        step1 = 61
        print("Player 1: Blue staircase leads down to", step1,"!")
    if (step1==13):
        step1 = 22
        print("Player 1: Red staircase leads up to", step1,"!")
    if (step1==37):
        step1 = 46
        print("Player 1: Red staircase leads up to", step1,"!")
    if (step1==31):
        step1 = 50
        print("Player 1: Red staircase leads up to", step1,"!")
    if (step1==85):
        step1 = 94
        print("Player 1: Red staircase leads up to", step1,"!")

    input("Player 2 rolls the dice:")

    dice2 = [randint(1,6) for i in range(1)] #for - creates a sheet with one random number from 1 to 6 - Dice!

    step2 += sum(dice2)

    print("player 2:", dice2, step2)

    if step2 >= 100: #if - checks whether the player has reached 100 points - Victory!
        print("PLAYER 2 won:", step2,"points!")
        break

    #Player 2 stairs!
    if (step2==16):
        step2 = 5
        print("Player 2: Blue staircase leads down to", step2,"!")
    if (step2==65):
        step2 = 44
        print("Player 2: Blue staircase leads down to", step2,"!")
    if (step2==78):
        step2 = 67
        print("Player 2: Blue staircase leads down to", step2,"!")
    if (step2==72):
        step2 = 61
        print("Player 2: Blue staircase leads down to", step2,"!")
    if (step2==13):
        step2 = 22
        print("Player 2: Red staircase leads up to", step2,"!")
    if (step2==37):
        step2 = 46
        print("Player 2: Red staircase leads up to", step2,"!")
    if (step2==31):
        step2 = 50
        print("Player 2: Red staircase leads up to", step2,"!")
    if (step2==85):
        step2 = 94
        print("Player 2: Red staircase leads up to", step2,"!")

    rounds +=1
    if rounds >=31: #if - checks if the game has reached 30 rounds - Draw!
        print("Draw!")
        break

    