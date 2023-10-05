# blackjack 2.0
import random

num_de_carta_j = num_de_carta_c = 3
part_jug = manos_bjn = apuesta_tot = perd_may_j = perd_may_j_bjn = perd_may_j_bj = racha_max \
    = vic_j = vic_c = perd_j = suma_j = suma_c = ant_racha = racha = 0
deci_j = punt_fin_j = punt_fin_c = None
racha_croupier = 1


def generar_carta():
    palos = "Picas", "Corazón", "Diamante", "Trébol"  # Creamos La Tupla de los Palos
    num = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, "J", "Q", "K")  # creamos La Tupla de los Números de las cartas
    carta_num = random.choice(num)
    carta_pal = random.choice(palos)
    return carta_num, carta_pal


# juego en si
nombre = input("Ingrese nombre del jugador: ")

monto = int(input("Ingrese el monto con el que jugará (maximo de $100.000): "))
while monto > 100000 or monto < 0:
    monto = int(input("Por favor reingrese su monto (no mas de $100.000 ni menos de $0): "))
monto_max_j = monto
print("-" * 50)

opcion = 1
while opcion != 3:
    print("Menu de opciones:")
    print("1) Agregar fondos a su pozo")
    print("2) Jugar Mano")
    print("3) Salir")
    opcion = int(input("Ingrese el numero de opcion que desee realizar: "))
    while opcion < 1 or opcion > 3:
        opcion = int(input("Por favor ingrese una opcion valida: "))
    print("-" * 50)

    # opcion 1
    if opcion == 1:
        if monto > 100000:
            print("ya tiene mas de $100.000, no puede sumar mas a su pozo actualmente")
            print("-" * 50)
            continue
        pozo = int(input("Ingrese una cantidad a su pozo (sin superar los $100.000): "))
        monto += pozo
        while monto > 100000:
            monto -= pozo
            pozo = int(input("No puede superar los $100.000, por favor reingrese sus fondos: "))
            monto += pozo
        print("Su pozo actual es de: $", monto)
        print("-" * 50)

    # opcion 2
    if opcion == 2:
        if monto < 5:
            print("No tiene la cantidad minima necesaria para empezar a jugar, recargue su pozo")
            print("-" * 50)
        else:
            print("su pozo actual es de: $", monto)
            apuesta = int(input("Ingrese su apuesta (menor o igual a su pozo y multiplo de 5): "))
            if apuesta <= 0:
                if monto < 5:
                    print("no puede jugar, debe recargar su pozo")
                    print("-" * 50)
                    continue
                else:
                    apuesta = int(input("no puede apostar $0 o menos, por favor ingrese una apuesta valida: "))
            apuesta_tot += apuesta
            while apuesta % 5 != 0 or apuesta > monto:
                apuesta = int(input("Por favor ingrese una apuesta valida (menor o igual a su pozo y multiplo de 5): "))
                while apuesta == 0:
                    apuesta = int(input("no puede apostar $0, por favor ingrese una apuesta valida: "))
            monto -= apuesta
            print("pozo actual: $", monto)
            print("apuesta actual: $", apuesta)
            print("-" * 20)
            part_jug += 1
            print("ronda: ", part_jug)
            numero1j, palo1j = generar_carta()
            if numero1j == 11:
                print("La primera carta de ", nombre, ": 'As'", palo1j)
            else:
                print("La primera carta ", nombre, ": ", numero1j, palo1j)
            numero2j, palo2j = generar_carta()
            if numero2j == 11:
                print("2da carta ", nombre, ": 'As'", palo2j)
            else:
                print("2da carta ", nombre, ": ", numero2j, palo2j)

            if numero1j == "J" or numero1j == "Q" or numero1j == "K":
                numero1j = 10
            if numero2j == "J" or numero2j == "Q" or numero2j == "K":
                numero2j = 10
            if numero1j == 11 and numero2j == 11:
                numero2j = 1

            suma_j = numero1j + numero2j
            print("puntaje parcial de", nombre, ": ", suma_j)
            numero1c, palo1c = generar_carta()
            if numero1c == 11:
                print("\n1er carta croupier: 'As'", palo1c)
            else:
                print("\n1er carta croupier: ", numero1c, palo1c)
            if numero1c == "J" or numero1c == "Q" or numero1c == "K":
                numero1c = 10
            print("-" * 20)
            if suma_j < 21:
                deci_j = int(input("\nSi el jugador desea pedir otra carta coloque '0', sino coloque otro numero: "))
            if suma_j == 22:
                numero2j = 1
                suma_j = numero1j + numero2j
            punt_fin_j = suma_j
            punt_fin_c = numero1c
            # parte de carta extra jugador
            while deci_j == 0 and punt_fin_j < 21:
                carta_extra_num_j, carta_extra_pal_j = generar_carta()
                if carta_extra_num_j == 11:
                    print("\nla carta numero", num_de_carta_j, "de ", nombre, " es: 'As'", carta_extra_pal_j)
                else:
                    print("\nla carta numero", num_de_carta_j, "de ", nombre, " es:", carta_extra_num_j,
                          carta_extra_pal_j)
                num_de_carta_j += 1
                if carta_extra_num_j == "J" or carta_extra_num_j == "Q" or carta_extra_num_j == "K":
                    carta_extra_num_j = 10
                punt_fin_j += carta_extra_num_j
                if punt_fin_j > 21:
                    if numero1j == 11:
                        numero1j = 1
                        punt_fin_j -= 10
                    elif carta_extra_num_j == 11:
                        punt_fin_j -= 10
                    else:
                        break
                elif punt_fin_j == 21:
                    break
                print("puntaje parcial de ", nombre, ": ", punt_fin_j)
                deci_j = int(input("\nSi el jugador desea pedir otra carta coloque '0', sino coloque otro numero: "))
            print("\nel puntaje final de ", nombre, " es: ", punt_fin_j)
            print("-" * 20)
            # parte de cartas del croupier
            numero2c, palo2c = generar_carta()
            if numero2c == 11:
                print("\nla segunda carta del croupier es: 'As'", palo2c)
            else:
                print("\nla segunda carta del croupier es: ", numero2c, palo2c)

            if numero2c == "J" or numero2c == "Q" or numero2c == "K":
                numero2c = 10

            suma_c = numero1c + numero2c
            if suma_c == 22:
                numero2c = 1
                suma_c = numero1c + numero2c
            punt_fin_c = suma_c
            while punt_fin_c < 17:
                carta_extra_num_c, carta_extra_pal_c = generar_carta()
                if carta_extra_num_c == 11:
                    print("\nla carta numero", num_de_carta_c, "del croupier es: 'As'", carta_extra_pal_c)
                else:
                    print("\nla carta numero", num_de_carta_c, "del croupier es:", carta_extra_num_c, carta_extra_pal_c)
                num_de_carta_c += 1
                if carta_extra_num_c == "J" or carta_extra_num_c == "Q" or carta_extra_num_c == "K":
                    carta_extra_num_c = 10
                punt_fin_c += carta_extra_num_c
                if punt_fin_c > 21:
                    if numero1c == 11:
                        numero1c = 1
                        punt_fin_c -= 10
                    if carta_extra_num_c == 11:
                        punt_fin_c -= 10
                if punt_fin_c == 21:
                    break
            print("\npuntaje final del croupier es: ", punt_fin_c)
            print("-" * 50)
            num_de_carta_j = 3
            num_de_carta_c = 3
            # ganador
            if suma_j == 21 and suma_c == 21:
                monto += apuesta
                manos_bjn += 1
                print("\tel ", nombre, " y el croupier empataron con BlackJack Natural !!!")
                print("su pozo actual es de: $", monto)
                print("-" * 50)
                racha = 1
            elif suma_j == 21 and suma_c != 21:
                vic_j += 1
                monto += apuesta * 2
                manos_bjn += 1
                print("\tgana ", nombre, " por BlackJack Natural !!!")
                print("su pozo actual es de: $", monto)
                print("-" * 50)
                racha = 1
            elif suma_c == 21 and suma_j != 21:
                vic_c += 1
                manos_bjn += 1
                perd_j += 1
                if perd_j == 1:
                    perd_may_j_bjn = apuesta
                elif apuesta > perd_may_j_bjn:
                    perd_may_j_bjn = apuesta
                print("\tgana el croupier por BlackJack Natural !!!")
                print("su pozo actual es de: $", monto)
                print("-" * 50)
                racha = 2
            elif punt_fin_j == punt_fin_c and punt_fin_j < 22 and punt_fin_c < 22:
                monto += apuesta
                print("\t ", nombre, " y el croupier empataron")
                print("su pozo actual es de: $", monto)
                print("-" * 50)
                racha = 1
            elif punt_fin_j > 21 or punt_fin_j < punt_fin_c < 22:
                vic_c += 1
                if perd_j == 1:
                    perd_may_j_bj = apuesta
                elif apuesta > perd_may_j_bj:
                    perd_may_j_bj = apuesta
                print("\tgana el croupier !!!")
                print("su pozo actual es de: $", monto)
                print("-" * 50)
                racha = 2
            elif 22 > punt_fin_j or punt_fin_c < punt_fin_j or punt_fin_c > 21:
                vic_j += 1
                monto += apuesta * 2
                print("\tgana ", nombre, " !!!")
                print("su pozo actual es de: $", monto)
                print("-" * 50)
                racha = 1
            if racha == 2 and ant_racha == 2:
                racha_croupier += 1
                if racha_croupier > racha_max:
                    racha_max = racha_croupier
            elif racha == 2 and ant_racha != 2:
                racha_croupier = 1
                if racha_croupier > racha_max:
                    racha_max = racha_croupier
            else:
                racha_croupier = 0
            ant_racha = racha

    if monto > monto_max_j:
        monto_max_j = monto

    if perd_may_j_bjn > perd_may_j_bj:
        perd_may_j = perd_may_j_bjn
    else:
        perd_may_j = perd_may_j_bj

        # opcion 3
    if opcion == 3:
        porc_v_j = vic_j * 100 / part_jug
        print("Porcentaje de victorias de ", nombre, ": ", porc_v_j, "%")
        print("Racha mas larga de victorias del croupier: ", racha_max)
        print("Cantidad de manos con BlackJack natural: ", manos_bjn)
        print("Monto maximo de ", nombre, " en el pozo: $", monto_max_j)
        apuesta_prom = apuesta_tot / part_jug
        print("Apuesta promedio de ", nombre, ": $", apuesta_prom)
        print("Perdida mas grande de ", nombre, ": $", perd_may_j)
